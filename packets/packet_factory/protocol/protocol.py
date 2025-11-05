from ....datatypes import *
from ....model import *
from ....enums import *

from typing import *


class Protocol:
    def __init__(self):
        self.models: Dict[int, Dict[int, Type[Model]]] = {}

    def register(self, state: State, id: int, model: Model):
        self.models[state] = self.models.get(state, {})
        self.models[state][id] = model

    def get_model(self, state: State, id: int) -> Type[Model]:
        return self.models[state][id]