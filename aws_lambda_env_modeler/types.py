from typing import TypeVar

from pydantic import BaseModel

Model = TypeVar('Model', bound=BaseModel)

__all__ = ['Model', 'BaseModel']
