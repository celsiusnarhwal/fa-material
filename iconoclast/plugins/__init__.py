import os
from contextlib import contextmanager

from rich.console import Console


@contextmanager
def new_console() -> Console:
    yield Console(file=open(os.devnull, "w"), record=True)
