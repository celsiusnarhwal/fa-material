import importlib
import inspect
from typing import Optional

from dict_deep import deep_get, deep_set
from mkdocs.config.base import Config
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from path import Path

symlink = Path(__file__).parent / ".overrides" / ".icons" / "fontawesome"


class FontAwesomePlugin(BasePlugin):
    def on_config(self, config: MkDocsConfig) -> Optional[Config]:
        try:
            fontawesome = importlib.import_module("fontawesomepro")
        except ImportError:
            return config

        symlink.unlink_p()
        symlink.parent.makedirs_p()

        fa_path = Path(inspect.getfile(fontawesome)).parent
        (fa_path / "static" / "fontawesomepro" / "svgs").symlink(symlink)

        key = "mdx_configs|pymdownx.emoji|options|custom_icons"

        custom_icons = (deep_get(config, key, sep="|") or []) + [str(symlink.parent)]
        deep_set(config, key, custom_icons, sep="|")

        config.theme.dirs.insert(1, str(symlink.parent.parent))

        return config

    def on_post_build(self, *, config: MkDocsConfig) -> None:
        symlink.parent.parent.rmtree_p()
