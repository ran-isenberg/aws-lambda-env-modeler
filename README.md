
# AWS Lambda Environment Variables Modeler (Python)

[![license](https://img.shields.io/github/license/ran-isenberg/aws-lambda-env-modeler)](https://github.com/ran-isenberg/aws-lambda-env-modeler/blob/master/LICENSE)
![PythonSupport](https://img.shields.io/static/v1?label=python&message=%203.8.17|%203.9|%203.10|%203.11&color=blue?style=flat-square&logo=python)
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
from pydantic import BaseModel

class MyEnvVariables(BaseModel):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
```

You must first use the `@init_environment_variables` decorator to automatically validate and initialize the environment variables before executing a function:

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
