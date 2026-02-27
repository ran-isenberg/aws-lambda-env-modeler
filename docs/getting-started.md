---
title: Getting Started
description: Install and start using AWS Lambda Env Modeler
---

## Installation

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
