import os
from typing import Optional, Union, Dict

from pydantic import BaseModel, Field


class APIConfig(BaseModel):
    access_token: Optional[str] = os.environ.get("VLESERVER_BASIC_AUTH_BASE64", 'YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA==')
    base_path: str = os.environ.get("VLESERVER_HOST", "http://localhost:8984")
    verify: Union[bool, str] = True

    def get_access_token(self) -> Optional[str]:
        return self.access_token

    def set_access_token(self, value: str):
       self.access_token = value


class HTTPException(Exception):
    def __init__(self, status_code: int, message: str, details: Dict):
        self.status_code = status_code
        self.message = message
        self.details = details
        super().__init__(f"{status_code} {message}: {details['detail']}")

    def __str__(self):
        return f"{self.status_code} {self.message}: {self.details['detail']}"
