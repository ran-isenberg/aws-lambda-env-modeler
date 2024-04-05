import json
from http import HTTPStatus
from typing import Any, Dict, Literal
from unittest.mock import patch

from pydantic import BaseModel

from aws_lambda_env_modeler import LAMBDA_ENV_MODELER_DISABLE_CACHE, get_environment_variables, init_environment_variables


class MyHandlerEnvVars(BaseModel):
    LOG_LEVEL: Literal['DEBUG', 'INFO', 'ERROR', 'CRITICAL', 'WARNING', 'EXCEPTION']


@init_environment_variables(model=MyHandlerEnvVars)
def my_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    env_vars = get_environment_variables(model=MyHandlerEnvVars)  # noqa: F841
    # can access directly env_vars.LOG_LEVEL as dataclass
    return {
        'statusCode': HTTPStatus.OK,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message': 'success'}),
    }


@patch.dict('os.environ', {LAMBDA_ENV_MODELER_DISABLE_CACHE: 'true', 'LOG_LEVEL': 'DEBUG'})
def test_my_handler():
    response = my_handler({}, None)
    assert response['statusCode'] == HTTPStatus.OK
    assert response['headers'] == {'Content-Type': 'application/json'}
    assert json.loads(response['body']) == {'message': 'success'}
