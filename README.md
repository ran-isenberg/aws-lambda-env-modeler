
# AWS Lambda Environment Variables Modeler (Python)

[![license](https://img.shields.io/github/license/ran-isenberg/aws-lambda-env-modeler)](https://github.com/ran-isenberg/aws-lambda-env-modeler/blob/master/LICENSE)
![PythonSupport](https://img.shields.io/static/v1?label=python&message=%203.8.17|%203.9|%203.10|%203.11|%203.12&color=blue?style=flat-square&logo=python)
![PyPI version](https://badge.fury.io/py/aws-lambda-env-modeler.svg)
![PyPi monthly downloads](https://img.shields.io/pypi/dm/aws-lambda-env-modeler)
[![codecov](https://codecov.io/gh/ran-isenberg/aws-lambda-env-modeler/branch/main/graph/badge.svg?token=P2K7K4KICF)](https://codecov.io/gh/ran-isenberg/aws-lambda-env-modeler)
![version](https://img.shields.io/github/v/release/ran-isenberg/aws-lambda-env-modeler)
![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/ran-isenberg/aws-lambda-env-modeler/badge)
![issues](https://img.shields.io/github/issues/ran-isenberg/aws-lambda-env-modeler)

![alt text](https://github.com/ran-isenberg/aws-lambda-env-modeler/blob/main/docs/media/banner.png?raw=true)

AWS-Lambda-Env-Modeler is a Python library designed to simplify the process of managing and validating environment variables in your AWS Lambda functions.

It leverages the power of [Pydantic](https://pydantic-docs.helpmanual.io/) models to define the expected structure and types of the environment variables.

This library is especially handy for serverless applications where managing configuration via environment variables is a common practice.

**[📜Documentation](https://ran-isenberg.github.io/aws-lambda-env-modeler/)** | **[Blogs website](https://www.ranthebuilder.cloud)**
> **Contact details | ran.isenberg@ranthebuilder.cloud**


## **The Problem**

Environment variables are often viewed as an essential utility. They serve as static AWS Lambda function configuration.

Their values are set during the Lambda deployment, and the only way to change them is to redeploy the Lambda function with updated values.

However, many engineers use them unsafely despite being such an integral and fundamental part of any AWS Lambda function deployment.

This usage may cause nasty bugs or even crashes in production.


This library allows you to correctly parse, validate, and use your environment variables in your Python AWS Lambda code.

Read more about it [here](https://www.ranthebuilder.cloud/post/aws-lambda-cookbook-environment-variables)

### **Features**

- Validates the environment variables against a Pydantic model: define both semantic and syntactic validation.
- Serializes the string environment variables into complex classes and types.
- Provides means to access the environment variables safely with a global getter function in every part of the function.
- Provides a decorator to initialize the environment variables before executing a function.
- Caches the parsed model for performance improvement for multiple 'get' calls.


## Installation

You can install it using pip:

```bash
pip install aws-lambda-env-modeler
```

## Getting started
Head over to the complete project documentation pages at GitHub pages at [https://ran-isenberg.github.io/aws-lambda-env-modeler](https://ran-isenberg.github.io/aws-lambda-env-modeler/)


## Usage
First, define a Pydantic model for your environment variables:

```python
from pydantic import BaseModel, HttpUrl

class MyEnvVariables(BaseModel):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    FLAG_X:  bool
    API_URL: HttpUrl
```

Before executing a function, you must use the `@init_environment_variables` decorator to validate and initialize the environment variables automatically.

The decorator guarantees that the function will run with the correct variable configuration.

Then, you can fetch the environment variables using the global getter function, 'get_environment_variables,' and use them just like a data class. At this point, they are parsed and validated.

```python
from aws_lambda_env_modeler import init_environment_variables

@init_environment_variables(MyEnvVariables)
def my_handler_entry_function(event, context):
    # At this point, environment variables are already validated and initialized
    pass
```

Then, you can fetch and validate the environment variables with your model:

```python
from aws_lambda_env_modeler import get_environment_variables

env_vars = get_environment_variables(MyEnvVariables)
print(env_vars.DB_HOST)
```

## Disabling Cache for Testing

By default, the modeler uses cache - the parsed model is cached for performance improvement for multiple 'get' calls.

In some cases, such as during testing, you may want to turn off the cache. You can do this by setting the `LAMBDA_ENV_MODELER_DISABLE_CACHE` environment variable to 'True.'

This is especially useful in tests where you want to run multiple tests concurrently, each with a different set of environment variables.

Here's an example of how you can use this in a pytest test:

```python
import json
from http import HTTPStatus
from typing import Any, Dict
from unittest.mock import patch

from pydantic import BaseModel
from typing_extensions import Literal

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
```

## Code Contributions
Code contributions are welcomed. Read this [guide.](https://github.com/ran-isenberg/aws-lambda-env-modeler/blob/main/CONTRIBUTING.md)

## Code of Conduct
Read our code of conduct [here.](https://github.com/ran-isenberg/aws-lambda-env-modeler/blob/main/CODE_OF_CONDUCT.md)

## Connect
* Email: [ran.isenberg@ranthebuilder.cloud](mailto:ran.isenberg@ranthebuilder.cloud)
* Blog Website [RanTheBuilder](https://www.ranthebuilder.cloud)
* LinkedIn: [ranisenberg](https://www.linkedin.com/in/ranisenberg/)
* Twitter: [IsenbergRan](https://twitter.com/IsenbergRan)


## License
This library is licensed under the MIT License. See the [LICENSE](https://github.com/ran-isenberg/aws-lambda-env-modeler/blob/main/LICENSE) file.
