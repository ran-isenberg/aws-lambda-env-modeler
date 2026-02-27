---
title: Usage
description: Schema definition, decorator, and getter function usage
---

## Schema Definition

Define a Pydantic model for your environment variables:

```python title="schema.py"
--8<-- "docs/snippets/schema.py"
```

Notice how you can use advanced types and value assertions and not just plain strings.

## Decorator

Before executing a function, you must use the `@init_environment_variables` decorator to validate and initialize the environment variables automatically.

The decorator guarantees that the function will run with the correct variable configuration.

Then, you can fetch the environment variables using the global getter function, 'get_environment_variables,' and use them just like a data class. At this point, they are parsed and validated.

```python hl_lines="7 18 20" title="my_handler.py"
--8<-- "docs/snippets/my_handler.py"
```
