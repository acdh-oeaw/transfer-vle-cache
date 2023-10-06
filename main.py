from typing import Dict, List
import asyncio
import nest_asyncio

nest_asyncio.apply()

from dboeannotation.services.async_api_token_auth_service import api_token_auth_create
from dboeannotation.services.async_api_service import api_documents_list, api_documents_change
from dboeannotation.api_config import APIConfig as dboeannotationAPIConfig
from vleserver.services.async_entries_service import _getDictDictNameEntries, _changeEntries
from vleserver.api_config import HTTPException

access_config = dboeannotationAPIConfig()

async def getXmlFromCache() -> Dict:
    response = await api_token_auth_create({'username': 'vle', 'password': 'changeme_please'}, access_config)
    # print(response['token'])
    access_config.set_access_token(response['token'])
    return await api_documents_list(cache_only=True, page_size=50, api_config_override=access_config)

# There is a limit on how many ids can be passed in one query.
max_num_of_ids = 50

async def sendUpdate(cachedData: Dict, es_ids: List, by: str) -> List:
    cachedXML = dict((result['es_id'], result['xml']) for result in cachedData['results'])
    # print(cachedXML)
    try:
      vleData = await _getDictDictNameEntries(dict_name='_qdb-TEI-02', pageSize=max_num_of_ids, ids=','.join(es_ids), lock=5)
    except HTTPException as error:
        # print(error.message, error.details)
        return [error.details]
    # print(vleData['_embedded']['entries'])
    for id in cachedXML.keys():
        l = [entry for entry in vleData['_embedded']['entries'] if entry['id'] == id]
        entry = l[0] if len(l) == 1 else None
        if entry is not None:
            entry['entry'] = cachedXML[id]
    #for id in cachedXML.keys():
    #    print((id, [e for e in vleData['_embedded']['entries'] if e['id'] == id]))
    try:
        res = await _changeEntries(dict_name='_qdb-TEI-02', as_user=by, data=vleData['_embedded'])
        ids = [entry['id'] for entry in res['_embedded']['entries']]
        changeData = [result for result in cachedData['results'] if result['es_id'] in ids]
        for change in changeData:
            change['xml'] = ''
        await api_documents_change(changeData, api_config_override=access_config)
        return [res]
    except HTTPException as error:
        if len(es_ids) == 1:
            changeData = [result for result in cachedData['results'] if result['es_id'] == es_ids[0]]
            changeData[0]['xml_error_message'] = error.details['detail']
            await api_documents_change(changeData, api_config_override=access_config)
            return [error.details]
        else:
            res = []
            for es_id in es_ids:
                res.append(*(await sendUpdate(cachedData, [es_id], by)))
            return res

async def main():
    from vleserver.api_config import APIConfig;
    cachedData = await getXmlFromCache()
    # print(cachedData)
    for by in {result["xml_modified_by"] for result in cachedData["results"]}:
        es_ids = [result['es_id'] for result in cachedData['results'] if result["xml_modified_by"] == by][:max_num_of_ids]
        print({by: await sendUpdate(cachedData, es_ids, by)})

if __name__ == '__main__':
    asyncio.run(main())
