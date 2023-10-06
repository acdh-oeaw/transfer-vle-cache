from typing import Dict, List
import asyncio
import nest_asyncio

nest_asyncio.apply()

from dboeannotation.services.async_api_token_auth_service import api_token_auth_create
from dboeannotation.services.async_api_service import api_documents_list
from vleserver.services.async_entries_service import _getDictDictNameEntries
from vleserver.services.async_entries_service import _changeEntries
from vleserver.api_config import HTTPException

async def getXmlFromCache() -> Dict:
    from dboeannotation.api_config import APIConfig;
    config = APIConfig()
    response = await api_token_auth_create({'username': 'vle', 'password': 'changeme_please'}, config)
    # print(response['token'])
    config.set_access_token(response['token'])
    return await api_documents_list(cache_only=True, page_size=50, api_config_override=config)

# There is a limit on how many ids can be passed in one query.
max_num_of_ids = 50

async def sendUpdate(cachedXML: Dict, es_ids: List, by: str) -> List:
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
        return [await _changeEntries(dict_name='_qdb-TEI-02', as_user=by, data=vleData['_embedded'])]
    except HTTPException as error:
        if len(es_ids) == 1:
            return [error.details]
        else:
            res = []
            for es_id in es_ids:
                res.append(*(await sendUpdate(cachedXML, [es_id], by)))
            return res

async def main():
    from vleserver.api_config import APIConfig;
    cachedData = await getXmlFromCache()
    # print(cachedData)
    for by in {result["xml_modified_by"] for result in cachedData["results"]}:
        es_ids = [result['es_id'] for result in cachedData['results'] if result["xml_modified_by"] == by][:max_num_of_ids]
        cachedXML = dict((result['es_id'], result['xml']) for result in cachedData['results'])
        # print(cachedXML)
        print({by: await sendUpdate(cachedXML, es_ids, by)})

if __name__ == '__main__':
    asyncio.run(main())
