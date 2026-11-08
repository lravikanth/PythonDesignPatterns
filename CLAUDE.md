# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Small, runnable examples of classic design patterns in pure Python (stdlib only, Python 3.8+). No build step, linter, or dependency manifest is configured.

## Commands

Run everything from the repository root; modules are run with `-m` so package imports resolve.

- Run a pattern's demo: `python -m creational.singleton`
- Run all tests: `python -m unittest discover tests`
- Run one test file: `python -m unittest tests.test_singleton`
- Run one test: `python -m unittest tests.test_singleton.SingletonTest.test_thread_safe`

## Structure and conventions

- Top-level packages are pattern categories: `creational/`, `structural/`, `behavioral/`. Each package's `__init__.py` holds only a docstring naming the category and its patterns.
- One module per pattern (`<category>/<pattern>.py`). Each module has a docstring explaining the pattern and its typical uses, the reusable implementation, a concrete example class, and a demo under `if __name__ == "__main__":`.
- Tests use `unittest`, one file per pattern: `tests/test_<pattern>.py`.
- When adding a pattern, also update the pattern table in `README.md` (the `structural/` and `behavioral/` rows are currently "_coming soon_").

## Gotchas

- `SingletonMeta` (`creational/singleton.py`) stores instances in a class-level `_instances` dict shared by every class that uses it, and nothing resets it. Singleton state such as `AppConfig` settings therefore carries over between tests in the same process. Tests that need isolation define their own local singleton class instead of reusing `AppConfig`.
