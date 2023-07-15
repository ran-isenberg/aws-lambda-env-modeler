import os
from functools import lru_cache, wraps
from typing import Any, Callable, Dict, Type

from aws_lambda_env_modeler.types import Model


def get_environment_variables(model: Type[Model]) -> Model:
    """
    This function receives a model of type Model, uses it to validate the environment variables, and returns the
    validated model.

    Args:
        model (Type[Model]): A Pydantic model that defines the structure and types of the expected environment variables.

    Returns:
        Model: An instance of the provided model filled with the values of the validated environment variables.
    """
    return __parse_model(model)


def init_environment_variables(model: Type[Model]):
    """
    A decorator function for AWS Lambda handler functions that initializes environment variables based on the given Pydantic model before executing
    the decorated function. The decorator validates the environment variables according to the model structure before
    running the handler.

    Args:
        model (Type[Model]): A Pydantic model that defines the structure and types of the expected environment variables.

    Returns:
        Callable: A decorated function that first initializes the environment variables and then runs the function.
    """

    def decorator(lambda_handler_function: Callable):

        @wraps(lambda_handler_function)
        def wrapper(event: Dict[str, Any], context):
            __parse_model(model)
            return lambda_handler_function(event, context)

        return wrapper

    return decorator


@lru_cache
def __parse_model(model: Type[Model]) -> Model:
    """
    A helper function to validate and parse environment variables based on a given Pydantic model. This function is
    also cached to improve performance in successive calls.

    Args:
        model (Type[Model]): A Pydantic model that defines the structure and types of the expected environment variables.

    Returns:
        Model: An instance of the provided model filled with the values of the validated environment variables.

    Raises:
        ValueError: If the environment variables do not match the structure of the model or cannot be validated.
    """
    try:
        return model.model_validate(os.environ)
    except Exception as exc:
        raise ValueError(f'failed to load environment variables, exception={str(exc)}') from exc
