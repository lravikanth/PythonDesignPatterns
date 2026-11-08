# Python Design Patterns

Small, runnable examples of classic design patterns in Python, grouped by category.
Each pattern lives in its own module, with a short docstring explaining the idea,
a demo under `if __name__ == "__main__":`, and unit tests in `tests/`.

## Patterns

| Folder | Category | Patterns |
|---|---|---|
| `creational/` | How objects are created | [Singleton](creational/singleton.py) |
| `structural/` | How objects are composed | _coming soon_ |
| `behavioral/` | How objects communicate | _coming soon_ |

### Singleton

Ensures a class has only one instance and provides a global point of access to it
(typical uses: configuration, logging, connection pools).

[`creational/singleton.py`](creational/singleton.py) implements it as a thread-safe
metaclass, `SingletonMeta`, using double-checked locking. Any class becomes a
singleton by declaring it as its metaclass:

```python
from creational.singleton import SingletonMeta

class Logger(metaclass=SingletonMeta):
    pass

assert Logger() is Logger()
```

The module includes an example singleton, `AppConfig`, that holds application-wide settings.

## Requirements

Python 3.8 or later. No third-party dependencies.

## Run

Run commands from the repository root.

Run a pattern's demo:

```bash
python -m creational.singleton
```

Expected output:

```
Same instance: True
debug from second: True
```

Run the tests:

```bash
python -m unittest discover tests
```

## Project layout

```
creational/    creational patterns (one module per pattern)
structural/    structural patterns
behavioral/    behavioral patterns
tests/         unit tests, one test_<pattern>.py per pattern
```

## Adding a pattern

1. Create `<category>/<pattern>.py` with a module docstring that explains the pattern,
   the implementation, and a demo under `if __name__ == "__main__":`.
2. Add `tests/test_<pattern>.py` using `unittest`.
3. Add the pattern to the table above.
