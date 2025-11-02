from .state_manager import StateManager
from ...enums import *

from threading import *


class LockedStateManager(StateManager):
    def __init__(self, initial_state: int = State.HANDSHAKE):
        self._state = initial_state
        self.lock = Lock()

    @property
    def state(self) -> int:
        with self.lock:
            return self._state
        
    @state.setter
    def state(self, state: int):
        with self.lock:
            self._state = state