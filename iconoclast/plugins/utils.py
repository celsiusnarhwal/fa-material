from __future__ import annotations

import inspect
import logging
import os
import sys

from mkdocs.commands.build import DuplicateFilter
from path import Path
from rich.console import Console


def ansify(text: str):
    console = Console(file=open(os.devnull, "w"), record=True)
    console.print(text)
    return console.export_text(styles=True)


def get_package_path() -> Path:
    try:
        import fontawesomepro
    except ImportError:
        log.error(
            ansify(
                "Font Awesome Pro is [bold underline red]not installed[/]. Run [bold underline green]icl setup[/]."
            )
        )
        sys.exit(1)
    else:
        return (
            Path(inspect.getfile(fontawesomepro)).parent / "static" / "fontawesomepro"
        )


log = logging.getLogger("mkdocs")
log.addFilter(DuplicateFilter())
