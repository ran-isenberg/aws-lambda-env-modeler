import json
from http import HTTPStatus
from typing import Any, Dict

from pydantic import BaseModel, Field, HttpUrl
from typing_extensions import Annotated, Literal

from aws_lambda_env_modeler import get_environment_variables, init_environment_variables


class MyHandlerEnvVars(BaseModel):
    REST_API: HttpUrl
    ROLE_ARN: Annotated[str, Field(min_length=20, max_length=2048)]
    POWERTOOLS_SERVICE_NAME: Annotated[str, Field(min_length=1)]
    LOG_LEVEL: Literal['DEBUG', 'INFO', 'ERROR', 'CRITICAL', 'WARNING', 'EXCEPTION']


@init_environment_variables(model=MyHandlerEnvVars)
def my_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    env_vars = get_environment_variables(model=MyHandlerEnvVars)  # noqa: F841
    # can access directly env_vars.REST_API, env_vars.ROLE_ARN as dataclass
    return {
        'statusCode': HTTPStatus.OK,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message': 'success'}),
    }
