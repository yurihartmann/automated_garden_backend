import uuid
from datetime import datetime
from typing import Dict

from app.utils.singleton import SingletonMeta
from fastapi import WebSocket


AUTO: str = "AUTO"
MANUAL: str = "MANUAL"
CONNECTING: str = "CONNECTING"
RECONNECTING: str = "RECONNECTING"


class ModeManager(metaclass=SingletonMeta):

    __mode: str = CONNECTING
    __last_set_mode = datetime.utcnow()

    def get_mode(self) -> str:
        if self.__mode == CONNECTING:
            return self.__mode
        if abs((self.__last_set_mode - datetime.utcnow()).seconds) > 10:
            self.__mode = RECONNECTING

        return self.__mode

    def set_mode(self, mode):
        if mode in [AUTO, MANUAL, CONNECTING, RECONNECTING]:
            self.__mode = mode
            self.__last_set_mode = datetime.utcnow()
