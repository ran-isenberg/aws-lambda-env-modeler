import os
from typing import Literal
from unittest.mock import patch

from aws_lambda_env_modeler.modeler import get_environment_variables
from aws_lambda_env_modeler.types import BaseModel


class TestModel(BaseModel):
    LOG_LEVEL: Literal['DEBUG', 'INFO', 'ERROR', 'CRITICAL', 'WARNING', 'EXCEPTION']


@patch.dict('os.environ', {'LAMBDA_ENV_MODELER_DISABLE_CACHE': 'false', 'LOG_LEVEL': 'DEBUG'}, clear=True)
def test_get_environment_variables_cache_enabled_then_disabled():
    # Given: Cache is enabled, LAMBDA_ENV_MODELER_DISABLE_CACHE is false

    # When: get_environment_variables is called
    env_vars = get_environment_variables(TestModel)

    # Then: log level is 'DEBUG'
    assert env_vars.LOG_LEVEL == 'DEBUG'

    # Given: first, we change log level to INFO', due to enabled cache, we still get DEBUG
    os.environ['LOG_LEVEL'] = 'INFO'
    env_vars = get_environment_variables(TestModel)
    assert env_vars.LOG_LEVEL == 'DEBUG'
    # When disabling cache
    os.environ['LAMBDA_ENV_MODELER_DISABLE_CACHE'] = 'true'

    # Then: log level should be 'INFO' instead of 'DEBUG'
    env_vars = get_environment_variables(TestModel)
    assert env_vars.LOG_LEVEL == 'INFO'


@patch.dict('os.environ', {'LOG_LEVEL': 'DEBUG'}, clear=True)
def test_get_environment_variables_cache_enabled_by_default():
    # Given: Cache is enabled even when LAMBDA_ENV_MODELER_DISABLE_CACHE is not defined

    # When: get_environment_variables is called
    env_vars = get_environment_variables(TestModel)

    # Then: log level is 'DEBUG'
    assert env_vars.LOG_LEVEL == 'DEBUG'

    # Given: first, we change log level to INFO'
    os.environ['LOG_LEVEL'] = 'INFO'
    env_vars = get_environment_variables(TestModel)

    # Then: log level should be 'DEBUG' instead of 'INFO' due to enabled cache with previous debug value in cache
    assert env_vars.LOG_LEVEL == 'DEBUG'


@patch.dict('os.environ', {'LAMBDA_ENV_MODELER_DISABLE_CACHE': 'true', 'LOG_LEVEL': 'DEBUG'}, clear=True)
def test_get_environment_variables_cache_disabled():
    # Given: Cache is disabled, LAMBDA_ENV_MODELER_DISABLE_CACHE is true

    # When: get_environment_variables is called
    env_vars = get_environment_variables(TestModel)

    # Then: log level is 'DEBUG'
    assert env_vars.LOG_LEVEL == 'DEBUG'

    # Given: we change log level to INFO
    os.environ['LOG_LEVEL'] = 'INFO'
    env_vars = get_environment_variables(TestModel)

    # Then: log level should be 'INFO' instead of 'DEBUG' due to disabled cache
    assert env_vars.LOG_LEVEL == 'INFO'
