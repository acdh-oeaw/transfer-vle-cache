import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException


async def _createDictBackup(
    dict_name: Any,
    Content_Type: Optional[Any] = None,
    Accept: Optional[Any] = None,
    Authorization: Optional[Any] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/restvle/dicts/{dict_name}/backup"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
        "Content-Type": Content_Type,
        "Accept": Accept,
        "Authorization": Authorization,
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "post",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def _getDictDictName(dict_name: Any, api_config_override: Optional[APIConfig] = None) -> Any:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/restvle/dicts/{dict_name}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "get",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return response


async def _deleteDictDictName(
    dict_name: Any, Authorization: Optional[Any] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/restvle/dicts/{dict_name}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
        "Authorization": Authorization,
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def _getDictDictNameDictUsers(api_config_override: Optional[APIConfig] = None) -> Any:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/restvle/dicts/dict_users"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "get",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return response


async def _restoreDict(
    data: Dict[str, Any],
    Content_Type: Optional[Any] = None,
    Accept: Optional[Any] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/restvle/dicts/restore"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
        "Content-Type": Content_Type,
        "Accept": Accept,
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def _getDicts(
    page: Optional[Any] = None, pageSize: Optional[Any] = None, api_config_override: Optional[APIConfig] = None
) -> Any:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/restvle/dicts"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "pageSize": pageSize}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "get",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return response


async def _createDict(
    data: Dict[str, Any],
    Content_Type: Optional[Any] = None,
    Accept: Optional[Any] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/restvle/dicts"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
        "Content-Type": Content_Type,
        "Accept": Accept,
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None
