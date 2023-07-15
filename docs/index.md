---
title: Homepage
description: AWS Lambda Environment Variables Parser Cookbook
---
## **AWS Lambda Environment Variables Parser Cookbook**

[<img alt="alt_text" src="./media/banner.png" />](https://www.ranthebuilder.cloud/)

AWS-Lambda-Env-Modeler is a Python library designed to simplify the process of managing and validating environment variables in your AWS Lambda functions.

It leverages the power of [Pydantic](https://pydantic-docs.helpmanual.io/){:target="_blank" rel="noopener"} models to define the expected structure and types of the environment variables.

This library is especially handy for serverless applications where managing configuration via environment variables is a common practice.

## **The Problem**

Environment variables are often viewed as an essential utility. They serve as static AWS Lambda function configuration.

Their values are set during the Lambda deployment, and the only way to change them is to redeploy the Lambda function with updated values.

However, many engineers use them unsafely despite being such an integral and fundamental part of any AWS Lambda function deployment.

This usage may cause nasty bugs or even crashes in production.

This library allows you to correctly parse, validate, and use your environment variables in your Python AWS Lambda code.

Read more about it [here](https://www.ranthebuilder.cloud/post/aws-lambda-cookbook-environment-variables){:target="_blank" rel="noopener"}

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

Then, you can fetch and validate the environment variables with your model:

```python hl_lines="8 18 20" title="my_handler.py"
--8<-- "docs/snippets/my_handler.py"
```

## License

This library is licensed under the MIT License. See the [LICENSE](https://github.com/ran-isenberg/aws-lambda-env-modeler/blob/main/LICENSE) file.
