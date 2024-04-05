import sys
from typing import TypeVar

from pydantic import BaseModel

Model = TypeVar('Model', bound=BaseModel)


if sys.version_info >= (3, 9):
    from typing import Annotated
else:
    from typing_extensions import Annotated

__all__ = ['Model', 'BaseModel', 'Annotated']
