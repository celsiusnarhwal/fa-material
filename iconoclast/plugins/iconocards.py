from material.plugins.social.plugin import SocialPlugin
from mkdocs.config.defaults import MkDocsConfig
from path import Path


class IconocardsPlugin(SocialPlugin):
    def _load_logo(self, config: MkDocsConfig):
        theme = config.theme
        icon = theme["icon"]["logo"]

        if icon and "logo" not in theme:
            for path in theme.dirs:
                icon_path = Path(path) / ".icons" / f"{icon}.svg"
                if icon_path.exists():
                    return self._load_logo_svg(icon_path, self.color["text"])

        return super()._load_logo(config)
