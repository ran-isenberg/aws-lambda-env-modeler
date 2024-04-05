from functools import wraps
from typing import Any, Callable, Dict, Type

from aws_lambda_env_modeler.modeler_impl import __get_environment_variables_impl
from aws_lambda_env_modeler.types import Model


def init_environment_variables(model: Type[Model]):
    """
    A decorator for AWS Lambda handler functions. It initializes and validates environment variables based on the provided Pydantic model before the execution of the decorated function.
    It uses LRU Cache by model class type to optimize parsing time. Cache can be disabled by setting the environment variable 'LAMBDA_ENV_MODELER_DISABLE_CACHE' to FALSE (default: cache is enabled)

    Args:
        model (Type[Model]): A Pydantic model that outlines the structure and types of the expected environment variables.

    Returns:
        Callable: A decorated function that first initializes and validates the environment variables, then executes the original function.

    Raises:
        ValueError: If the environment variables do not align with the model's structure or fail validation.
    """

    def decorator(lambda_handler_function: Callable):
        @wraps(lambda_handler_function)
        def wrapper(event: Dict[str, Any], context, **kwargs):
            # Initialize and validate environment variables before executing the lambda handler function
            __get_environment_variables_impl(model)
            return lambda_handler_function(event, context, **kwargs)

        return wrapper

    return decorator


def get_environment_variables(model: Type[Model]) -> Model:
    """
    Retrieves and validates environment variables based on the provided Pydantic model.
    It uses LRU Cache by model class type to optimize parsing time. Cache can be disabled by setting the environment variable 'LAMBDA_ENV_MODELER_DISABLE_CACHE' to FALSE (default: cache is enabled)
    It's recommended to use anywhere in the function's after init_environment_variables decorator was used on the handler function.

    Args:
        model (Type[Model]): A Pydantic model that outlines the structure and types of the expected environment variables.

    Returns:
        Model: An instance of the provided model populated with the values of the validated environment variables.

    Raises:
        ValueError: If the environment variables do not align with the model's structure or fail validation.
    """
    return __get_environment_variables_impl(model)
