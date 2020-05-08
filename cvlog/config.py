from enum import Enum
import os

class Mode(Enum):
    NONE = 0
    DEBUG = 1
    LOG = 2

class Level(Enum):
    ERROR = 0
    INFO = 1
    TRACE = 2

class Config:
    def __new__(cls):
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance.__initialised = False
        return cls.instance

    def __init__(self):
        if not self.__initialised:
            self.__initialised = True
            self.__log_path = "log"
            self.__level = None
            self.__mode = None
            self.__rotate_log = True

    def log_path(self):
        env_var = os.environ.get("CVLOG_PATH")
        if env_var is not None and env_var.strip():
            return env_var
        return self.__log_path

    def log_time(self):
        return self.__log_time

    def rotate_log(self):
        return self.__rotate_log

    def set_curent_mode(self, mode):
        self.__mode = self.__get_enum(mode, Mode)

    def set_curent_level(self, mode):
        self.__level = self.__get_enum(mode, Level)

    def set_log_path(self, path):
        self.__log_path = path

    def set_rotate_log(self, is_rotate_log):
        self.__log_path = is_rotate_log

    def curent_mode(self):
        return self.__osenv_or_else("CVLOG_MODE", Mode, self.__mode)

    def curent_level(self):
        return self.__osenv_or_else("CVLOG_LEVEL", Level, self.__level)

    def __osenv_or_else(self, name, enum, current_value):
        env_var = os.environ.get(name)
        if env_var is not None and env_var.strip():
            current_value = self.__get_enum(env_var, enum)
        if current_value is None:
            current_value = enum(0)
        return current_value

    def __get_enum(self, value, enum):
        if type(value) == enum:
            return value
        elif type(value) == str and value in enum.__members__:
            return enum[value]
        raise Exception("Invalid " + value)

def set_mode(mode):
    return Config().set_curent_mode(mode)

def set_level(level):
    return Config().set_curent_level(level)

def set_path(path):
    return Config().set_log_path(path)

def set_rotate_log(is_rotate_log: bool = True):
    return Config().set_rotate_log(is_rotate_log)
