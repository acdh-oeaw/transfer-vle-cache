from typing import Dict
import asyncio
import nest_asyncio

nest_asyncio.apply()

from dboeannotation.api_config import APIConfig;
from dboeannotation.services.async_api_token_auth_service import api_token_auth_create
from dboeannotation.services.async_api_service import api_documents_list
async def getXmlFromCache() -> Dict:
    config = APIConfig()
    response = await api_token_auth_create({'username': 'vle', 'password': 'changeme_please'}, config)
    # print(response['token'])
    config.set_access_token(response['token'])
    return await api_documents_list(cache_only=True, page_size=50, api_config_override=config)


async def main():
    print(await getXmlFromCache())

if __name__ == '__main__':
    asyncio.run(main())
