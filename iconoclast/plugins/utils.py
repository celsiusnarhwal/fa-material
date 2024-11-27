from __future__ import annotations

import inspect
import logging
import os
import subprocess
import sys
from pathlib import Path

from mkdocs.commands.build import DuplicateFilter
from mkdocs.config.defaults import MkDocsConfig
from rich.console import Console


def ansify(text: str):
    console = Console(file=open(os.devnull, "w"), record=True)
    console.print(text)
    return console.export_text(styles=True)


def get_or_install_package(config: MkDocsConfig = None) -> Path:
    try:
        import fontawesomepro
    except ImportError:
        if config:
            plugin_config = config.plugins["iconoclast"].config

            if plugin_config.auto:
                index_url = f"https://dl.fontawesome.com/{plugin_config.token}/fontawesome-pro/python/simple"

                subprocess.run(
                    [*plugin_config.installer_args, "fontawesomepro", "-i", index_url]
                )

                return get_or_install_package()

        log.error(
            ansify(
                "Font Awesome Pro is not installed. "
                "Run [cyan]iconoclast install[/] to install it."
            )
        )
        sys.exit(1)
    else:
        return (
            Path(inspect.getfile(fontawesomepro)).parent / "static" / "fontawesomepro"
        )


log = logging.getLogger("mkdocs")
log.addFilter(DuplicateFilter())
