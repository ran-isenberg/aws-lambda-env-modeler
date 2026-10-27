---
title: Getting Started
description: Install and start using AWS Lambda Env Modeler
---

## Installation

Supported Python versions: 3.11, 3.12, 3.13, 3.14 and 3.15. Python 3.10 is no longer supported, as it is deprecated. See the [AWS Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html){:target="_blank" rel="noopener"} page for further information.

=== "pip"

    ```bash
    pip install aws-lambda-env-modeler
    ```

=== "uv"

    ```bash
    uv add aws-lambda-env-modeler
    ```

=== "poetry"

    ```bash
    poetry add aws-lambda-env-modeler
    ```

## Quick Start

Define a Pydantic model, decorate your handler, and access validated environment variables:

```python
from typing import Any, Dict, Literal

from pydantic import BaseModel

from aws_lambda_env_modeler import get_environment_variables, init_environment_variables


class MyEnvVars(BaseModel):
    LOG_LEVEL: Literal['DEBUG', 'INFO', 'ERROR', 'CRITICAL', 'WARNING', 'EXCEPTION']


@init_environment_variables(model=MyEnvVars)
def my_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    env_vars = get_environment_variables(model=MyEnvVars)
    # env_vars.LOG_LEVEL is now typed and validated
    return {'statusCode': 200}
```
