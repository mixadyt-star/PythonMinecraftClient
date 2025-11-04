from ..context import *
from .path import Path

from typing import *


class ContextPath(Path):
    def __init__(self, path: Optional[List[Any]] = None):
        self.path = [] if (path is None) else path

    def join(self, key: Any) -> 'Path':
        return Path(self.path + [key])

    def apply(self, traversal: Context) -> Context:
        current = traversal

        for key in self.path:
            current = current.get(key)

        return current