from typing import Dict
import asyncio
import nest_asyncio

nest_asyncio.apply()

from dboeannotation.services.async_api_token_auth_service import api_token_auth_create
from dboeannotation.services.async_api_service import api_documents_list
from vleserver.services.async_entries_service import _getDictDictNameEntries
from vleserver.services.async_entries_service import _changeEntries

async def getXmlFromCache() -> Dict:
    from dboeannotation.api_config import APIConfig;
    config = APIConfig()
    response = await api_token_auth_create({'username': 'vle', 'password': 'changeme_please'}, config)
    # print(response['token'])
    config.set_access_token(response['token'])
    return await api_documents_list(cache_only=True, page_size=50, api_config_override=config)


async def main():
    from vleserver.api_config import APIConfig;
    cachedData = await getXmlFromCache()
    # print(cachedData)
    es_ids = ','.join([result['es_id'] for result in cachedData['results']])
    cachedXML = dict((result['es_id'], result['xml']) for result in cachedData['results'])
    # print(cachedXML)
    vleData = await _getDictDictNameEntries(dict_name='_qdb-TEI-02', pageSize=50, ids=es_ids, lock=5)
    # print(vleData['_embedded']['entries'])
    for id in cachedXML.keys():
        l = [entry for entry in vleData['_embedded']['entries'] if entry['id'] == id]
        entry = l[0] if len(l) == 1 else None
        if entry is not None:
            entry['entry'] = cachedXML[id]
    # for id in cachedXML.keys():
    #     print((id, [e for e in vleData['_embedded']['entries'] if e['id'] == id]))
    await _changeEntries(dict_name='_qdb-TEI-02', as_user='another-user', data=vleData['_embedded'])

if __name__ == '__main__':
    asyncio.run(main())
