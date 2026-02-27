---
title: Testing
description: How to disable cache and test with different environment variables
---

## Disabling Cache for Testing

By default, the modeler uses cache - the parsed model is cached for performance improvement for multiple 'get' calls.

In some cases, such as during testing, you may want to turn off the cache. You can do this by setting the `LAMBDA_ENV_MODELER_DISABLE_CACHE` environment variable to 'True.'

This is especially useful in tests where you want to run multiple tests concurrently, each with a different set of environment variables.

Here's an example of how you can use this in a pytest test:

```python hl_lines="8 26" title="pytest.py"
--8<-- "docs/snippets/pytest.py"
```
