from __future__ import annotations

import inspect
import logging
import os
import sys
from typing import Optional, Tuple

from dict_deep import deep_get, deep_set
from mkdocs.commands.build import DuplicateFilter
from mkdocs.config import config_options as c
from mkdocs.config.base import Config, ConfigErrors, ConfigWarnings
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from path import Path

from iconoclast.plugins import new_console

symlink = Path(__file__).parent / ".overrides" / ".icons" / "fontawesome"


class IconokitConfig(Config):
    name = c.Type(str, default="")
    token = c.Type(str, default=os.getenv("FONTAWESOME_API_TOKEN") or "")
    enabled = c.Private()

    def validate(self) -> Tuple[ConfigWarnings, ConfigErrors]:
        warnings, errors = super().validate()
        self.enabled = bool(self.name and self.token)
        return warnings, errors


class IconoclastConfig(Config):
    css = c.Type(bool, default=False)
    kit: IconokitConfig = c.SubConfig(IconokitConfig)


class IconoclastPlugin(BasePlugin[IconoclastConfig]):
    def on_config(self, config: MkDocsConfig) -> Optional[Config]:
        icon_dirs = [symlink]
        css = "iconoclast.min.css"

        symlink.unlink_p()
        symlink.parent.makedirs_p()

        (get_package_path() / "svgs").symlink(symlink)

        if self.config.kit.enabled:
            try:
                import iconokit
            except ImportError:
                with new_console() as console:
                    console.print(
                        "You haven't installed a Font Awesome kit. "
                        "Run [cyan]iconoclast install[/] or change your settings "
                        "for the [magenta]iconoclast[/] plugin.",
                    )
                    log.error(console.export_text(styles=True))
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
        symlink.parent.parent.rmtree_p()

        if self.config.css and not self.config.kit.enabled:
            fa_path = get_package_path()
            site_dir = Path(config.site_dir)

            (fa_path / "css" / "all.min.css").copy(site_dir / "iconoclast.min.css")
            (fa_path / "webfonts").copytree(site_dir / "webfonts")


def get_package_path() -> Path:
    try:
        import fontawesomepro
    except ImportError:
        with new_console() as console:
            console.print(
                "Font Awesome Pro is not installed. Install it or remove the [magenta]iconoclast[/] plugin."
            )
            log.error(console.export_text(styles=True))
            sys.exit(1)
    else:
        return (
            Path(inspect.getfile(fontawesomepro)).parent / "static" / "fontawesomepro"
        )


log = logging.getLogger("mkdocs")
log.addFilter(DuplicateFilter())
