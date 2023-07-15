import os
from functools import lru_cache, wraps
from typing import Any, Callable, Dict, Type, TypeVar

from pydantic import BaseModel

Model = TypeVar('Model', bound=BaseModel)


@lru_cache
def __parse_model(model: Type[Model]) -> Model:
    try:
        return model.model_validate(os.environ)
    except Exception as exc:
        raise ValueError(f'failed to load environment variables, exception={str(exc)}') from exc


def get_environment_variables(model: Type[Model]) -> Model:
    """_summary_

    Args:
        model (Type[Model]): _description_

    Returns:
        Model: _description_
    """
    return __parse_model(model)


def init_environment_variables(model: Type[Model]):
    """_summary_

    Args:
        model (Model): _description_
    """

    def decorator(lambda_handler_function: Callable):

        @wraps(lambda_handler_function)
        def wrapper(event: Dict[str, Any], context):
            __parse_model(model)
            return lambda_handler_function(event, context)

        return wrapper

    return decorator
