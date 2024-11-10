import contextlib
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

import requests
import typer
from dict_deep import deep_get
from log_symbols import LogSymbols
from merge_args import merge_args
from mkdocs.config.base import load_config
from sgqlc.endpoint.requests import RequestsEndpoint
from sgqlc.operation import Operation
from yarl import URL

from iconoclast.cli.context import set_context
from iconoclast.cli.exceptions import Iconoquit
from iconoclast.cli.graphql.schema import fontawesome_schema as schema
from iconoclast.plugins.main import IconoclastConfig, IconokitConfig

app = typer.Typer(rich_markup_mode="rich")

here = Path(__file__).parent

pip = [sys.executable, "-m", "pip", "--disable-pip-version-check"]


def common_options(func: Callable):
    # noinspection PyUnusedLocal
    @merge_args(func)
    def wrapper(
        ctx: typer.Context,
        config_file: Path = typer.Option(
            None,
            "--config-file",
            "-F",
            exists=True,
            dir_okay=False,
            help="The path to your MkDocs configuration file.",
            show_default=False,
        ),
        **kwargs,
    ):
        return func(ctx=ctx, **kwargs)

    return wrapper


@app.command(
    name="install",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
    epilog="This command supports all options of [cyan]pip install[/cyan] in addition to the ones above.",
)
@set_context
@common_options
def install(ctx: typer.Context):
    """
    Downlod Font Awesome Pro.
    """
    forbidden = {"--index-url", "-i"}.intersection(ctx.args)

    if forbidden:
        raise Iconoquit(
            f"The {forbidden.pop()} option is not supported by this command."
        )

    config_file = ctx.params.get("config_file")
    config = load_config(str(config_file) if config_file else None)
    plugin_config: IconoclastConfig = config.plugins["iconoclast"].config
    token = plugin_config.token

    if not token:
        raise Iconoquit(
            "You must specify a Font Awesome package manager token in Iconoclast's plugin configuration to use this "
            "command."
        )

    index_url = f"https://dl.fontawesome.com/{token}/fontawesome-pro/python/simple"

    subprocess.run(
        [*pip, "install", "fontawesomepro", "--index-url", index_url, *ctx.args],
    )


@app.command(
    name="kit",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
    epilog="This command supports all options of [cyan]pip install[/cyan] in addition to the ones above.",
)
@set_context
@common_options
def kit(
    ctx: typer.Context,
):
    """
    Install a kit.
    """
    config_file = ctx.params.get("config_file")
    config = load_config(str(config_file) if config_file else None)
    kit_config: IconokitConfig = config.plugins["iconoclast"].config.kit

    if not kit_config.enabled:
        raise Iconoquit(
            "You must specify a kit name and Font Awesome API token in "
            "Iconoclast's plugin configuration to use this command."
        )

    api_url = URL("https://api.fontawesome.com")

    resp = requests.post(
        api_url / "token",
        headers={"Authorization": f"Bearer {kit_config.token}"},
    )

    if resp.status_code == 403:
        raise Iconoquit("Your Font Awesome API token is invalid.")
    elif resp.status_code != 200:
        raise Iconoquit("Couldn't communicate with Font Awesome.")

    access_token = resp.json()["access_token"]

    endpoint = RequestsEndpoint(
        str(api_url), base_headers={"Authorization": f"Bearer {access_token}"}
    )

    op = Operation(schema.RootQueryType)
    op.me.kits.name()
    op.me.kits.token()
    op.me.kits.icon_uploads()

    data = endpoint(op)["data"]
    kits = deep_get(data, "me.kits")

    try:
        kit_ = next(k for k in kits if k["name"] == kit_config.name)
    except StopIteration:
        raise Iconoquit(f'Kit "{kit_config.name}" does not exist')

    icons = kit_["iconUploads"]

    with TemporaryDirectory() as tmpdir:
        with contextlib.chdir(tmpdir):
            iconokit_root = Path.cwd() / "iconokit"
            iconokit_pkg = iconokit_root / "iconokit"

            shutil.copytree(here / "iconokit", iconokit_root, dirs_exist_ok=True)
            (iconokit_pkg / ".token").write_text(kit_["token"])

            icons_dir = iconokit_pkg / ".overrides" / ".icons" / "fontawesome" / "kit"
            icons_dir.mkdir(parents=True, exist_ok=True)

            for icon in icons:
                svg = (
                    f"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 {icon['width']} "
                    f"{icon['height']}\"><path d=\"{icon['path']}\"/></svg>"
                )
                (icons_dir / icon["name"]).with_suffix(".svg").write_text(svg)

            subprocess.run(
                [*pip, "install", iconokit_root.absolute(), *ctx.args],
            )

            if not {"--quiet", "-q"}.intersection(ctx.args):
                print(f"{LogSymbols.SUCCESS.value} Installed {kit_config.name}.")


@app.callback(
    no_args_is_help=True,
    epilog=f"Iconoclast © {datetime.now().year} celsius narhwal. Thank you kindly for your attention.",
)
def main():
    """
    Iconoclast integrates Font Awesome Pro with Material for MkDocs.
    """


if __name__ == "__main__":
    # For debugging only.
    app()
