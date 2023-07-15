from typing import Annotated

from pydantic import Field, HttpUrl, BaseModel


class MyHandlerEnvVars(BaseModel):
    REST_API: HttpUrl
    ROLE_ARN: Annotated[str, Field(min_length=20, max_length=2048)]
