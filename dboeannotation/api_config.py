import os
from typing import Optional, Union

from pydantic import BaseModel, Field


class APIConfig(BaseModel):
    access_token: Optional[str] = None
    base_path: str = os.environ.get("DBOEANNOTATION_HOST", "https://dboeannotation-test.acdh-dev.oeaw.ac.at")
    verify: Union[bool, str] = True

    def get_access_token(self) -> Optional[str]:
        return self.access_token

    def set_access_token(self, value: str):
       self.access_token = value


class HTTPException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"{status_code} {message}")

    def __str__(self):
        return f"{self.status_code} {self.message}"
