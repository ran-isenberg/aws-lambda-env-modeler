import os
from functools import lru_cache
from typing import Type

from aws_lambda_env_modeler.types import Model

# Environment variable to control caching
LAMBDA_ENV_MODELER_DISABLE_CACHE = 'LAMBDA_ENV_MODELER_DISABLE_CACHE'


def __get_environment_variables_impl(model: Type[Model]) -> Model:
    # Check if the environment variable for disabling cache is set to true
    disable_cache = True if os.getenv(LAMBDA_ENV_MODELER_DISABLE_CACHE, 'false').lower() == 'true' else False
    if disable_cache:
        # If LAMBDA_ENV_MODELER_DISABLE_CACHE is true, parse the model without cache
        return __parse_model_impl(model)
    # If LAMBDA_ENV_MODELER_DISABLE_CACHE is not true, parse the model with cache
    return __parse_model_with_cache(model)


@lru_cache
def __parse_model_with_cache(model: Type[Model]) -> Model:
    # Parse the model with cache enabled
    return __parse_model_impl(model)


def __parse_model_impl(model: Type[Model]) -> Model:
    try:
        # Validate the model with the environment variables
        return model.model_validate(os.environ)
    except Exception as exc:
        # If validation fails, raise an exception with the error message
        raise ValueError(f'failed to load environment variables, exception={str(exc)}') from exc
