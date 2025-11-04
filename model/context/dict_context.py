from .context import Context

from typing import *


class DictContext(Context):
    def __init__(self, context: Optional[Dict[str, Any]] = None):
        self.context: Dict[str, Any] = {} if (context is None) else context

    def append(self, key, value):
        self.context[key] = value

    def get(self, key):
        return self.context[key]