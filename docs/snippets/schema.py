from typing import Literal

from pydantic import BaseModel, Field, HttpUrl

from aws_lambda_env_modeler.types import Annotated


class MyEnvVariables(BaseModel):
    REST_API: HttpUrl
    ROLE_ARN: Annotated[str, Field(min_length=20, max_length=2048)]
    POWERTOOLS_SERVICE_NAME: Annotated[str, Field(min_length=1)]
    LOG_LEVEL: Literal['DEBUG', 'INFO', 'ERROR', 'CRITICAL', 'WARNING', 'EXCEPTION']
