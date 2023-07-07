from typing import Dict
import asyncio
import nest_asyncio

nest_asyncio.apply()

from dboeannotation.services.async_api_token_auth_service import api_token_auth_create
from dboeannotation.services.async_api_service import api_documents_list, api_documents_update
from vleserver.services.async_entries_service import _getDictDictNameEntries, _changeEntries, _getDictDictNameEntry

async def getXmlFromCache() -> Dict:
    # response = await api_token_auth_create({'username': 'vle', 'password': 'changeme_please'}, config)
    # print(response['token'])
    # token is read from env access_token
    return await api_documents_list(cache_only=True, page_size=50)


async def main():
    from vleserver.api_config import APIConfig;
    from vleserver.api_config import HTTPException;
    cachedData = await getXmlFromCache()
    # print(cachedData)
    es_ids = ','.join([result['es_id'] for result in cachedData['results']])
    cachedXML = dict((result['es_id'], result['xml']) for result in cachedData['results'])
    cachedXMLModifiedBy = dict((result['es_id'], result['xml_modified_by'] if result['xml_modified_by'] else None) for result in cachedData['results'])
    modifiedByCachedXml = {}
    for k, v in cachedXMLModifiedBy.items():
        modifiedByCachedXml[v] = modifiedByCachedXml.get(v, []) + [k]
    # print(cachedXML)
    # print(cachedXMLModifiedBy)
    # print(modifiedByCachedXml)
    vleData = await _getDictDictNameEntries(dict_name='_qdb-TEI-02', pageSize=50, ids=es_ids, lock=5)
    # print(vleData['_embedded']['entries'])
    for id in cachedXML.keys():
        l = [entry for entry in vleData['_embedded']['entries'] if entry['id'] == id]
        entry = l[0] if len(l) == 1 else None
        if entry is not None:
            entry['entry'] = cachedXML[id]
    for user in modifiedByCachedXml.keys():
        cachedXMLByUser = dict((xml_id, xml) for xml_id, xml in cachedXML.items() if xml_id in modifiedByCachedXml[user])
        print(cachedXMLByUser)
        # for id in cachedXML.keys():
        #     print((id, [e for e in vleData['_embedded']['entries'] if e['id'] == id]))
        try:
          await _changeEntries(dict_name='_qdb-TEI-02', as_user=user if user is not None else 'sschwaiger', data=vleData['_embedded'])
        except HTTPException as e:
          if e.details['status'] == '422':
              await tryEachEntry(cachedXMLByUser, user if user is not None else 'sschwaiger')
          else:
              raise e

async def tryEachEntry(cachedXMLByUser: Dict, user: str):
    from vleserver.api_config import HTTPException
    for id in cachedXMLByUser.keys():
        try:
            entry = await _getDictDictNameEntry(dict_name='_qdb-TEI-02', id=id, lock=5)
            entry['entry'] = cachedXMLByUser[id]
            try:
                res = await _changeEntries(dict_name='_qdb-TEI-02', as_user=user, data={"entries": [entry]})
                print(res)
            except HTTPException as e:
                await api_documents_update(data=[{"es_id": id, "xml": entry['entry'], "xml_error_message": e.details['detail']}])
                print({id: e.message})
        except HTTPException as e:
            await api_documents_update(data=[{"es_id": id, "xml": entry['entry'], "xml_error_message": e.details['detail']}])
            print({id: e.message})
if __name__ == '__main__':
    asyncio.run(main())
