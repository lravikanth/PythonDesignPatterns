"""Singleton pattern.

Ensures a class has only one instance and gives a global point of access to it.
Typical uses: configuration, logging, connection pools.

This module implements it with a thread-safe metaclass, so any class can become
a singleton by declaring ``metaclass=SingletonMeta``.
"""

import threading


class SingletonMeta(type):
    """Metaclass that creates at most one instance per class."""

    _instances: dict = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # Double-checked locking: skip the lock once the instance exists.
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppConfig(metaclass=SingletonMeta):
    """Example singleton: application-wide settings."""

    def __init__(self):
        self._settings = {}

    def set(self, key, value):
        self._settings[key] = value

    def get(self, key, default=None):
        return self._settings.get(key, default)


if __name__ == "__main__":
    first = AppConfig()
    first.set("debug", True)

    second = AppConfig()
    print("Same instance:", first is second)        # True
    print("debug from second:", second.get("debug"))  # True
