import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def api_token_auth_create(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> Dict:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api-token-auth/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return response
