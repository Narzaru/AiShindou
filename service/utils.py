import json
import functools
import time


class Time(object):

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Time, cls).__new__(cls)
        return cls

    @staticmethod
    def performing_time(func, *args, **kwargs):
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Finished {func.__name__!r} in {run_time:.8f} secs")
            return value
        return wrapper_timer()

    @staticmethod
    def server_time():
        return time.localtime()


class TemplateColours:

    __JsonShell = None

    @classmethod
    def __init__(cls, path):
        cls.__JsonShell = JsonShell(path)

    @classmethod
    def get_colour(cls, colour):
        return cls.__toNumber(
            cls.__JsonShell.get_data_by_key("colours")[colour]
        )

    @staticmethod
    def __toNumber(string):
        return int(string, 16)

    @property
    def Green(self):
        return self.get_colour("green")

    @property
    def Red(self):
        return self.get_colour("red")

    @property
    def Yellow(self):
        return self.get_colour("yellow")


class ThreadObserver:

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Time, cls).__new__(cls)
        return cls

    __is_blocked = False

    @classmethod
    def Is_blocked(cls):
        return cls.__is_blocked

    @classmethod
    def lock(cls):
        cls.__is_blocked = True

    @classmethod
    def unlock(cls):
        cls.__is_blocked = False

    @staticmethod
    def wait(func):
        @functools.wraps(func)
        def wrapper_wait(*args, **kwargs):
            while ThreadObserver.Is_blocked():
                pass
            ThreadObserver.lock()
            result = func(*args, **kwargs)
            ThreadObserver.unlock()
            return result
        return wrapper_wait


class JsonShell:

    def __init__(self, filePath: str(), encoding="utf-8"):
        self.__filePath = filePath
        self.__encoding = encoding

    @ThreadObserver.wait
    def __open(self):
        with open(file=self.__filePath, mode='r', encoding=self.__encoding) as file:
            return json.load(file)

    def get_data(self):
        return self.__open()

    def get_data_by_key(self, key: str()):
        return (self.get_data())[key]
