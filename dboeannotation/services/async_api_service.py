import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def api_annotations_list(
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    collection: Optional[str] = None,
    category: Optional[str] = None,
    created_by: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/annotations"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "page": page,
        "page_size": page_size,
        "title": title,
        "description": description,
        "collection": collection,
        "category": category,
        "created_by": created_by,
    }

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

            return None


async def api_annotations_create(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/annotations"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_annotations_read(
    id: int,
    title: Optional[str] = None,
    description: Optional[str] = None,
    collection: Optional[str] = None,
    category: Optional[str] = None,
    created_by: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/annotations/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "title": title,
        "description": description,
        "collection": collection,
        "category": category,
        "created_by": created_by,
    }

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

            return None


async def api_annotations_update(
    id: int,
    data: Dict[str, Any],
    title: Optional[str] = None,
    description: Optional[str] = None,
    collection: Optional[str] = None,
    category: Optional[str] = None,
    created_by: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/annotations/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "title": title,
        "description": description,
        "collection": collection,
        "category": category,
        "created_by": created_by,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("put", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_annotations_delete(
    id: int,
    title: Optional[str] = None,
    description: Optional[str] = None,
    collection: Optional[str] = None,
    category: Optional[str] = None,
    created_by: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/annotations/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "title": title,
        "description": description,
        "collection": collection,
        "category": category,
        "created_by": created_by,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_annotations_partial_update(
    id: int,
    data: Dict[str, Any],
    title: Optional[str] = None,
    description: Optional[str] = None,
    collection: Optional[str] = None,
    category: Optional[str] = None,
    created_by: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/annotations/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "title": title,
        "description": description,
        "collection": collection,
        "category": category,
        "created_by": created_by,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("patch", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_article_edits_list(
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    deadline: Optional[str] = None,
    step: Optional[str] = None,
    status: Optional[str] = None,
    last_edited: Optional[str] = None,
    current: Optional[str] = None,
    user: Optional[str] = None,
    lemma: Optional[str] = None,
    finished_date: Optional[str] = None,
    begin_time: Optional[str] = None,
    reporting: Optional[str] = None,
    lemma__id: Optional[str] = None,
    date: Optional[str] = None,
    currentstatus: Optional[str] = None,
    mytasks: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/article_edits"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "page": page,
        "page_size": page_size,
        "deadline": deadline,
        "step": step,
        "status": status,
        "last_edited": last_edited,
        "current": current,
        "user": user,
        "lemma": lemma,
        "finished_date": finished_date,
        "begin_time": begin_time,
        "reporting": reporting,
        "lemma__id": lemma__id,
        "date": date,
        "currentstatus": currentstatus,
        "mytasks": mytasks,
        "ordering": ordering,
    }

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

            return None


async def api_article_edits_create(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/article_edits"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_article_edits_read(
    id: int,
    deadline: Optional[str] = None,
    step: Optional[str] = None,
    status: Optional[str] = None,
    last_edited: Optional[str] = None,
    current: Optional[str] = None,
    user: Optional[str] = None,
    lemma: Optional[str] = None,
    finished_date: Optional[str] = None,
    begin_time: Optional[str] = None,
    reporting: Optional[str] = None,
    lemma__id: Optional[str] = None,
    date: Optional[str] = None,
    currentstatus: Optional[str] = None,
    mytasks: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/article_edits/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "deadline": deadline,
        "step": step,
        "status": status,
        "last_edited": last_edited,
        "current": current,
        "user": user,
        "lemma": lemma,
        "finished_date": finished_date,
        "begin_time": begin_time,
        "reporting": reporting,
        "lemma__id": lemma__id,
        "date": date,
        "currentstatus": currentstatus,
        "mytasks": mytasks,
        "ordering": ordering,
    }

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

            return None


async def api_article_edits_update(
    id: int,
    data: Dict[str, Any],
    deadline: Optional[str] = None,
    step: Optional[str] = None,
    status: Optional[str] = None,
    last_edited: Optional[str] = None,
    current: Optional[str] = None,
    user: Optional[str] = None,
    lemma: Optional[str] = None,
    finished_date: Optional[str] = None,
    begin_time: Optional[str] = None,
    reporting: Optional[str] = None,
    lemma__id: Optional[str] = None,
    date: Optional[str] = None,
    currentstatus: Optional[str] = None,
    mytasks: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/article_edits/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "deadline": deadline,
        "step": step,
        "status": status,
        "last_edited": last_edited,
        "current": current,
        "user": user,
        "lemma": lemma,
        "finished_date": finished_date,
        "begin_time": begin_time,
        "reporting": reporting,
        "lemma__id": lemma__id,
        "date": date,
        "currentstatus": currentstatus,
        "mytasks": mytasks,
        "ordering": ordering,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("put", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_article_edits_delete(
    id: int,
    deadline: Optional[str] = None,
    step: Optional[str] = None,
    status: Optional[str] = None,
    last_edited: Optional[str] = None,
    current: Optional[str] = None,
    user: Optional[str] = None,
    lemma: Optional[str] = None,
    finished_date: Optional[str] = None,
    begin_time: Optional[str] = None,
    reporting: Optional[str] = None,
    lemma__id: Optional[str] = None,
    date: Optional[str] = None,
    currentstatus: Optional[str] = None,
    mytasks: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/article_edits/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "deadline": deadline,
        "step": step,
        "status": status,
        "last_edited": last_edited,
        "current": current,
        "user": user,
        "lemma": lemma,
        "finished_date": finished_date,
        "begin_time": begin_time,
        "reporting": reporting,
        "lemma__id": lemma__id,
        "date": date,
        "currentstatus": currentstatus,
        "mytasks": mytasks,
        "ordering": ordering,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_article_edits_partial_update(
    id: int,
    data: Dict[str, Any],
    deadline: Optional[str] = None,
    step: Optional[str] = None,
    status: Optional[str] = None,
    last_edited: Optional[str] = None,
    current: Optional[str] = None,
    user: Optional[str] = None,
    lemma: Optional[str] = None,
    finished_date: Optional[str] = None,
    begin_time: Optional[str] = None,
    reporting: Optional[str] = None,
    lemma__id: Optional[str] = None,
    date: Optional[str] = None,
    currentstatus: Optional[str] = None,
    mytasks: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/article_edits/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "deadline": deadline,
        "step": step,
        "status": status,
        "last_edited": last_edited,
        "current": current,
        "user": user,
        "lemma": lemma,
        "finished_date": finished_date,
        "begin_time": begin_time,
        "reporting": reporting,
        "lemma__id": lemma__id,
        "date": date,
        "currentstatus": currentstatus,
        "mytasks": mytasks,
        "ordering": ordering,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("patch", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_author_artikel_list(
    page: Optional[int] = None, page_size: Optional[int] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/author_artikel"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "page_size": page_size}

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

            return None


async def api_author_artikel_create(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/author_artikel"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_author_artikel_read(id: int, api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/author_artikel/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
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

            return None


async def api_author_artikel_update(
    id: int, data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/author_artikel/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("put", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_author_artikel_delete(id: int, api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/author_artikel/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
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
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_author_artikel_partial_update(
    id: int, data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/author_artikel/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("patch", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_categories_list(
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    name: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/categories"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "page_size": page_size, "name": name}

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

            return None


async def api_categories_create(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/categories"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_categories_read(
    id: int, name: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/categories/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"name": name}

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

            return None


async def api_categories_update(
    id: int, data: Dict[str, Any], name: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/categories/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"name": name}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("put", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_categories_delete(
    id: int, name: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/categories/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"name": name}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_categories_partial_update(
    id: int, data: Dict[str, Any], name: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/categories/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"name": name}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("patch", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_collections_list(
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    id: Optional[float] = None,
    id__contains: Optional[float] = None,
    created_by: Optional[str] = None,
    public: Optional[str] = None,
    annotations: Optional[str] = None,
    deleted: Optional[str] = None,
    lemma_id: Optional[str] = None,
    lemma_id__isnull: Optional[str] = None,
    title: Optional[str] = None,
    annotations__category: Optional[str] = None,
    tag: Optional[str] = None,
    category: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/collections"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "page": page,
        "page_size": page_size,
        "id": id,
        "id__contains": id__contains,
        "created_by": created_by,
        "public": public,
        "annotations": annotations,
        "deleted": deleted,
        "lemma_id": lemma_id,
        "lemma_id__isnull": lemma_id__isnull,
        "title": title,
        "annotations__category": annotations__category,
        "tag": tag,
        "category": category,
        "ordering": ordering,
    }

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

            return None


async def api_collections_create(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/collections"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_collections_read(
    id: int,
    _id: Optional[float] = None,
    id__contains: Optional[float] = None,
    created_by: Optional[str] = None,
    public: Optional[str] = None,
    annotations: Optional[str] = None,
    deleted: Optional[str] = None,
    lemma_id: Optional[str] = None,
    lemma_id__isnull: Optional[str] = None,
    title: Optional[str] = None,
    annotations__category: Optional[str] = None,
    tag: Optional[str] = None,
    category: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/collections/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "_id": _id,
        "id__contains": id__contains,
        "created_by": created_by,
        "public": public,
        "annotations": annotations,
        "deleted": deleted,
        "lemma_id": lemma_id,
        "lemma_id__isnull": lemma_id__isnull,
        "title": title,
        "annotations__category": annotations__category,
        "tag": tag,
        "category": category,
        "ordering": ordering,
    }

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

            return None


async def api_collections_update(
    id: int,
    data: Dict[str, Any],
    _id: Optional[float] = None,
    id__contains: Optional[float] = None,
    created_by: Optional[str] = None,
    public: Optional[str] = None,
    annotations: Optional[str] = None,
    deleted: Optional[str] = None,
    lemma_id: Optional[str] = None,
    lemma_id__isnull: Optional[str] = None,
    title: Optional[str] = None,
    annotations__category: Optional[str] = None,
    tag: Optional[str] = None,
    category: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/collections/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "_id": _id,
        "id__contains": id__contains,
        "created_by": created_by,
        "public": public,
        "annotations": annotations,
        "deleted": deleted,
        "lemma_id": lemma_id,
        "lemma_id__isnull": lemma_id__isnull,
        "title": title,
        "annotations__category": annotations__category,
        "tag": tag,
        "category": category,
        "ordering": ordering,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("put", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_collections_delete(
    id: int,
    _id: Optional[float] = None,
    id__contains: Optional[float] = None,
    created_by: Optional[str] = None,
    public: Optional[str] = None,
    annotations: Optional[str] = None,
    deleted: Optional[str] = None,
    lemma_id: Optional[str] = None,
    lemma_id__isnull: Optional[str] = None,
    title: Optional[str] = None,
    annotations__category: Optional[str] = None,
    tag: Optional[str] = None,
    category: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/collections/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "_id": _id,
        "id__contains": id__contains,
        "created_by": created_by,
        "public": public,
        "annotations": annotations,
        "deleted": deleted,
        "lemma_id": lemma_id,
        "lemma_id__isnull": lemma_id__isnull,
        "title": title,
        "annotations__category": annotations__category,
        "tag": tag,
        "category": category,
        "ordering": ordering,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_collections_partial_update(
    id: int,
    data: Dict[str, Any],
    _id: Optional[float] = None,
    id__contains: Optional[float] = None,
    created_by: Optional[str] = None,
    public: Optional[str] = None,
    annotations: Optional[str] = None,
    deleted: Optional[str] = None,
    lemma_id: Optional[str] = None,
    lemma_id__isnull: Optional[str] = None,
    title: Optional[str] = None,
    annotations__category: Optional[str] = None,
    tag: Optional[str] = None,
    category: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/collections/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "_id": _id,
        "id__contains": id__contains,
        "created_by": created_by,
        "public": public,
        "annotations": annotations,
        "deleted": deleted,
        "lemma_id": lemma_id,
        "lemma_id__isnull": lemma_id__isnull,
        "title": title,
        "annotations__category": annotations__category,
        "tag": tag,
        "category": category,
        "ordering": ordering,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("patch", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_dboe_query_list(api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/dboe-query"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
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

            return None


async def api_documents_list(
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    cache_only: Optional[bool] = None,
    es_id: Optional[str] = None,
    index: Optional[str] = None,
    version: Optional[float] = None,
    in_collections: Optional[str] = None,
    tag: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/documents"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "page": page,
        "page_size": page_size,
        "cache_only": str(cache_only),
        "es_id": es_id,
        "index": index,
        "version": version,
        "in_collections": in_collections,
        "tag": tag,
    }

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


async def api_documents_create(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/documents"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_documents_read(
    id: int,
    es_id: Optional[str] = None,
    index: Optional[str] = None,
    version: Optional[float] = None,
    in_collections: Optional[str] = None,
    tag: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/documents/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "es_id": es_id,
        "index": index,
        "version": version,
        "in_collections": in_collections,
        "tag": tag,
    }

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

            return None
async def api_documents_update(
    data: Dict[str, Any],
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/documents"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("put", base_path + path, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            await inital_response.json(content_type='')

            return None
async def _api_documents_update(
    id: int,
    data: Dict[str, Any],
    es_id: Optional[str] = None,
    index: Optional[str] = None,
    version: Optional[float] = None,
    in_collections: Optional[str] = None,
    tag: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/documents/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "es_id": es_id,
        "index": index,
        "version": version,
        "in_collections": in_collections,
        "tag": tag,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("put", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_documents_delete(
    id: int,
    es_id: Optional[str] = None,
    index: Optional[str] = None,
    version: Optional[float] = None,
    in_collections: Optional[str] = None,
    tag: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/documents/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "es_id": es_id,
        "index": index,
        "version": version,
        "in_collections": in_collections,
        "tag": tag,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_documents_partial_update(
    id: int,
    data: Dict[str, Any],
    es_id: Optional[str] = None,
    index: Optional[str] = None,
    version: Optional[float] = None,
    in_collections: Optional[str] = None,
    tag: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/documents/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "es_id": es_id,
        "index": index,
        "version": version,
        "in_collections": in_collections,
        "tag": tag,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("patch", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_lemmas_list(
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    org: Optional[str] = None,
    norm: Optional[str] = None,
    filename: Optional[str] = None,
    count: Optional[float] = None,
    simplex: Optional[str] = None,
    task: Optional[str] = None,
    lemmatisierung: Optional[str] = None,
    users: Optional[str] = None,
    id: Optional[float] = None,
    simplex__lemmatisierung: Optional[str] = None,
    count__gt: Optional[float] = None,
    count__lt: Optional[float] = None,
    has__norm: Optional[str] = None,
    collection: Optional[str] = None,
    has__simplex: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/lemmas"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "page": page,
        "page_size": page_size,
        "org": org,
        "norm": norm,
        "filename": filename,
        "count": count,
        "simplex": simplex,
        "task": task,
        "lemmatisierung": lemmatisierung,
        "users": users,
        "id": id,
        "simplex__lemmatisierung": simplex__lemmatisierung,
        "count__gt": count__gt,
        "count__lt": count__lt,
        "has__norm": has__norm,
        "collection": collection,
        "has__simplex": has__simplex,
        "ordering": ordering,
    }

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

            return None


async def api_lemmas_create(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/lemmas"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_lemmas_read(
    id: int,
    org: Optional[str] = None,
    norm: Optional[str] = None,
    filename: Optional[str] = None,
    count: Optional[float] = None,
    simplex: Optional[str] = None,
    task: Optional[str] = None,
    lemmatisierung: Optional[str] = None,
    users: Optional[str] = None,
    _id: Optional[float] = None,
    simplex__lemmatisierung: Optional[str] = None,
    count__gt: Optional[float] = None,
    count__lt: Optional[float] = None,
    has__norm: Optional[str] = None,
    collection: Optional[str] = None,
    has__simplex: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/lemmas/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "org": org,
        "norm": norm,
        "filename": filename,
        "count": count,
        "simplex": simplex,
        "task": task,
        "lemmatisierung": lemmatisierung,
        "users": users,
        "_id": _id,
        "simplex__lemmatisierung": simplex__lemmatisierung,
        "count__gt": count__gt,
        "count__lt": count__lt,
        "has__norm": has__norm,
        "collection": collection,
        "has__simplex": has__simplex,
        "ordering": ordering,
    }

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

            return None


async def api_lemmas_update(
    id: int,
    data: Dict[str, Any],
    org: Optional[str] = None,
    norm: Optional[str] = None,
    filename: Optional[str] = None,
    count: Optional[float] = None,
    simplex: Optional[str] = None,
    task: Optional[str] = None,
    lemmatisierung: Optional[str] = None,
    users: Optional[str] = None,
    _id: Optional[float] = None,
    simplex__lemmatisierung: Optional[str] = None,
    count__gt: Optional[float] = None,
    count__lt: Optional[float] = None,
    has__norm: Optional[str] = None,
    collection: Optional[str] = None,
    has__simplex: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/lemmas/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "org": org,
        "norm": norm,
        "filename": filename,
        "count": count,
        "simplex": simplex,
        "task": task,
        "lemmatisierung": lemmatisierung,
        "users": users,
        "_id": _id,
        "simplex__lemmatisierung": simplex__lemmatisierung,
        "count__gt": count__gt,
        "count__lt": count__lt,
        "has__norm": has__norm,
        "collection": collection,
        "has__simplex": has__simplex,
        "ordering": ordering,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("put", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_lemmas_delete(
    id: int,
    org: Optional[str] = None,
    norm: Optional[str] = None,
    filename: Optional[str] = None,
    count: Optional[float] = None,
    simplex: Optional[str] = None,
    task: Optional[str] = None,
    lemmatisierung: Optional[str] = None,
    users: Optional[str] = None,
    _id: Optional[float] = None,
    simplex__lemmatisierung: Optional[str] = None,
    count__gt: Optional[float] = None,
    count__lt: Optional[float] = None,
    has__norm: Optional[str] = None,
    collection: Optional[str] = None,
    has__simplex: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/lemmas/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "org": org,
        "norm": norm,
        "filename": filename,
        "count": count,
        "simplex": simplex,
        "task": task,
        "lemmatisierung": lemmatisierung,
        "users": users,
        "_id": _id,
        "simplex__lemmatisierung": simplex__lemmatisierung,
        "count__gt": count__gt,
        "count__lt": count__lt,
        "has__norm": has__norm,
        "collection": collection,
        "has__simplex": has__simplex,
        "ordering": ordering,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_lemmas_partial_update(
    id: int,
    data: Dict[str, Any],
    org: Optional[str] = None,
    norm: Optional[str] = None,
    filename: Optional[str] = None,
    count: Optional[float] = None,
    simplex: Optional[str] = None,
    task: Optional[str] = None,
    lemmatisierung: Optional[str] = None,
    users: Optional[str] = None,
    _id: Optional[float] = None,
    simplex__lemmatisierung: Optional[str] = None,
    count__gt: Optional[float] = None,
    count__lt: Optional[float] = None,
    has__norm: Optional[str] = None,
    collection: Optional[str] = None,
    has__simplex: Optional[str] = None,
    ordering: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/lemmas/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "org": org,
        "norm": norm,
        "filename": filename,
        "count": count,
        "simplex": simplex,
        "task": task,
        "lemmatisierung": lemmatisierung,
        "users": users,
        "_id": _id,
        "simplex__lemmatisierung": simplex__lemmatisierung,
        "count__gt": count__gt,
        "count__lt": count__lt,
        "has__norm": has__norm,
        "collection": collection,
        "has__simplex": has__simplex,
        "ordering": ordering,
    }

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("patch", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_tags_list(
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    name: Optional[str] = None,
    color: Optional[str] = None,
    emoji: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/tags"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "page_size": page_size, "name": name, "color": color, "emoji": emoji}

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

            return None


async def api_tags_create(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/tags"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_tags_read(
    id: int,
    name: Optional[str] = None,
    color: Optional[str] = None,
    emoji: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/tags/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"name": name, "color": color, "emoji": emoji}

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

            return None


async def api_tags_update(
    id: int,
    data: Dict[str, Any],
    name: Optional[str] = None,
    color: Optional[str] = None,
    emoji: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/tags/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"name": name, "color": color, "emoji": emoji}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("put", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_tags_delete(
    id: int,
    name: Optional[str] = None,
    color: Optional[str] = None,
    emoji: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/tags/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"name": name, "color": color, "emoji": emoji}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_tags_partial_update(
    id: int,
    data: Dict[str, Any],
    name: Optional[str] = None,
    color: Optional[str] = None,
    emoji: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/tags/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"name": name, "color": color, "emoji": emoji}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("patch", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_users_list(
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    username: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/users"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "page_size": page_size, "username": username}

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

            return None


async def api_users_create(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/users"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("post", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_users_read(
    id: int, username: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/users/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"username": username}

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

            return None


async def api_users_update(
    id: int, data: Dict[str, Any], username: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/users/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"username": username}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("put", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_users_delete(
    id: int, username: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/users/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"username": username}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None


async def api_users_partial_update(
    id: int, data: Dict[str, Any], username: Optional[str] = None, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/api/users/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"username": username}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request("patch", base_path + path, params=query_params, json=data) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(inital_response.status, f" failed with status code: {inital_response.status}")
            response = await inital_response.json()

            return None
