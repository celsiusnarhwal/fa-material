import importlib
import inspect
from typing import Optional, Tuple

from dict_deep import deep_get, deep_set
from mkdocs.config.base import Config, ConfigErrors, ConfigWarnings, ValidationError
from mkdocs.config.config_options import Type as Option
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from path import Path

symlink = Path(__file__).parent / ".overrides" / ".icons" / "fontawesome"


class FontAwesomePluginConfig(Config):
    version = Option(int, default=6)

    def validate(self) -> Tuple[ConfigWarnings, ConfigErrors]:
        warnings, errors = super().validate()

        if self.version not in (5, 6):
            raise ValidationError(
                f"Font Awesome version must be 5 or 6, not {self.version}"
            )

        return warnings, errors


class FontAwesomePlugin(BasePlugin[FontAwesomePluginConfig]):
    def on_config(self, config: MkDocsConfig) -> Optional[Config]:
        package = "fontawesome-pro" if self.config.version == 5 else "fontawesomepro"

        try:
            fontawesome = importlib.import_module(package)
        except ImportError:
            return config

        symlink.unlink_p()
        symlink.parent.makedirs_p()

        fa_path = Path(inspect.getfile(fontawesome)).parent
        (fa_path / "static" / package.replace("-", "_") / "svgs").symlink(symlink)

        key = "mdx_configs|pymdownx.emoji|options|custom_icons"

        custom_icons = (deep_get(config, key, sep="|") or []) + [str(symlink.parent)]
        deep_set(config, key, custom_icons, sep="|")

        config.theme.dirs.insert(1, str(symlink.parent.parent))

        return config

    def on_post_build(self, *, config: MkDocsConfig) -> None:
        symlink.parent.parent.rmtree_p()
