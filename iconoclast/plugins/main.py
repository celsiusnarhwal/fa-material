from __future__ import annotations

import logging
import os
import shutil
import sys
from pathlib import Path
from typing import Optional, Tuple

from dict_deep import deep_get, deep_set
from mkdocs.commands.build import DuplicateFilter
from mkdocs.config import config_options as c
from mkdocs.config.base import Config, ConfigErrors, ConfigWarnings
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin

from iconoclast.plugins import utils

symlink = Path(__file__).parent / ".overrides" / ".icons" / "fontawesome"


class IconokitConfig(Config):
    name = c.Type(str, default="")
    token = c.Type(str, default=os.getenv("FONTAWESOME_API_TOKEN", ""))
    enabled = c.Private()

    def validate(self) -> Tuple[ConfigWarnings, ConfigErrors]:
        warnings, errors = super().validate()
        self.enabled = self.name and self.token
        return warnings, errors


class IconoclastConfig(Config):
    css = c.Type(bool, default=False)
    token = c.Type(
        str,
        default=os.getenv(
            "FONTAWESOME_PKG_TOKEN", os.getenv("FONTAWESOME_NPM_AUTH_TOKEN", "")
        ),
    )
    kit: IconokitConfig = c.SubConfig(IconokitConfig)


class IconoclastPlugin(BasePlugin[IconoclastConfig]):
    def on_config(self, config: MkDocsConfig) -> Optional[Config]:
        if config.theme.name != "material":
            log.error(
                utils.ansify(
                    "Iconoclast requires requires that your MkDocs theme "
                    "be set to [bold underline green]Material for MkDocs[/].",
                )
            )
            sys.exit(1)

        icon_dirs = [symlink]
        css = "fontawesome.min.css"

        symlink.unlink(missing_ok=True)
        symlink.parent.mkdir(parents=True, exist_ok=True)

        symlink.symlink_to(utils.get_package_path() / "svgs")

        if self.config.kit.enabled:
            try:
                # noinspection PyUnresolvedReferences
                import iconokit
            except ImportError:
                log.error(
                    utils.ansify(
                        "You've configured a Font Awesome kit, but haven't installed it. "
                        "Run [bold underline cyan]iconoclast install[/], then try again."
                    )
                )
                sys.exit(1)
            else:
                icon_dirs.append(iconokit.icons())
                css = iconokit.kit("css")

        key = "mdx_configs|pymdownx.emoji|options|custom_icons"

        for icon_dir in icon_dirs:
            custom_icons = (deep_get(config, key, sep="|") or []) + [
                str(icon_dir.parent)
            ]
            deep_set(config, key, custom_icons, sep="|")

            config.theme.dirs.insert(1, str(icon_dir.parent.parent))

        if self.config.css:
            config.extra_css.append(css)

        return config

    def on_post_build(self, *, config: MkDocsConfig) -> None:
        shutil.rmtree(symlink.parent.parent)

        if self.config.css and not self.config.kit.enabled:
            fa_path = utils.get_package_path()
            site_dir = Path(config.site_dir)

            shutil.copy(
                fa_path / "css" / "all.min.css", site_dir / "fontawesome.min.css"
            )
            shutil.copytree(fa_path / "webfonts", site_dir / "webfonts")


log = logging.getLogger("mkdocs")
log.addFilter(DuplicateFilter())
