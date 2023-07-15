from typing import Any, Dict
from aws_lambda_env_vars_parser.parser import init_environment_variables, get_environment_variables
from service.handlers.schemas.env_vars import MyHandlerEnvVars


@init_environment_variables(model=MyHandlerEnvVars)
def handle_sqs_batch(event: Dict[str, Any], context) -> None:
    get_environment_variables(model=MyHandlerEnvVars)
