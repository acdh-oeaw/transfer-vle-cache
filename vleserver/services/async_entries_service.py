import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException


async def _getDictDictNameEntry(
    dict_name: Any,
    id: Any,
    lock: Optional[Any] = None,
    format: Optional[Any] = None,
    Accept: Optional[Any] = None,
    Authorization: Optional[Any] = None,
    api_config_override: Optional[APIConfig] = None,
) -> Any:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/restvle/dicts/{dict_name}/entries/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.wde.v2+json",
        "Authorization": f"Basic { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"lock": lock, "format": format}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "get",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 200:
                error_response = await inital_response.json()
                raise HTTPException(inital_response.status, error_response['title'])
            response = await inital_response.json()

            return response


async def _changeEntry(
    dict_name: Any,
    id: Any,
    data: Dict[str, Any],
    Content_Type: Optional[Any] = None,
    Accept: Optional[Any] = None,
    Authorization: Optional[Any] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/restvle/dicts/{dict_name}/entries/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.wde.v2+json",
        "Authorization": f"Basic { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("put", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                error_response = await inital_response.json()
                raise HTTPException(inital_response.status, error_response['title'])
            response = await inital_response.json()

            return response


async def _deleteDictDictNameEntry(
    dict_name: Any, id: Any, Authorization: Optional[Any] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/restvle/dicts/{dict_name}/entries/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.wde.v2+json",
        "Authorization": f"Basic { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                error_response = await inital_response.json()
                raise HTTPException(inital_response.status, error_response['title'])

            return None


async def _getDictDictNameEntries(
    dict_name: Any,
    page: Optional[Any] = None,
    pageSize: Optional[Any] = None,
    id: Optional[Any] = None,
    ids: Optional[Any] = None,
    q: Optional[Any] = None,
    sort: Optional[Any] = None,
    altLemma: Optional[Any] = None,
    lock: Optional[Any] = None,
    format: Optional[Any] = None,
    Authorization: Optional[Any] = None,
    Accept: Optional[Any] = None,
    api_config_override: Optional[APIConfig] = None,
) -> Any:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/restvle/dicts/{dict_name}/entries"
    headers = {
        "Accept": "application/vnd.wde.v2+json",
        "Authorization": f"Basic { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "page": page,
        "pageSize": pageSize,
        "id": id,
        "ids": ids,
        "q": q,
        "sort": sort,
        "altLemma": altLemma,
        "lock": lock,
        "format": format,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "get",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 200:
                error_response = await inital_response.json()
                raise HTTPException(inital_response.status, error_response['title'], error_response)
            response = await inital_response.json()

            return response


async def _createEntry(
    dict_name: Any,
    Authorization: Any,
    data: Dict[str, Any],
    Content_Type: Optional[Any] = None,
    Accept: Optional[Any] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/restvle/dicts/{dict_name}/entries"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.wde.v2+json",
        "Authorization": f"Basic { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 201:
                error_response = await inital_response.json()
                raise HTTPException(inital_response.status, error_response['title'], error_response)

            return None


async def _changeEntries(
    dict_name: Any,
    data: Dict[str, Any],
    as_user: Optional[Any] = None,
    Content_Type: Optional[Any] = None,
    Accept: Optional[Any] = None,
    Authorization: Optional[Any] = None,
    api_config_override: Optional[APIConfig] = None,
) -> Dict:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/restvle/dicts/{dict_name}/entries"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.wde.v2+json",
        "Authorization": f"Basic { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"as-user": as_user}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("patch", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                error_response = await inital_response.json()
                raise HTTPException(inital_response.status, error_response['title'], error_response)
            response = await inital_response.json()

            return response
