import subprocess
from datetime import datetime
from pathlib import Path as StdPath
from tempfile import TemporaryDirectory

import requests
import typer
from dict_deep import deep_get
from halo import Halo
from mkdocs.config.base import load_config
from path import Path
from sgqlc.endpoint.requests import RequestsEndpoint
from sgqlc.operation import Operation
from yarl import URL

from iconoclast.cli.context import set_context
from iconoclast.cli.exceptions import Iconoquit
from iconoclast.cli.graphql.schema import fontawesome_schema as schema
from iconoclast.plugins.iconoclast import IconokitConfig

app = typer.Typer(rich_markup_mode="rich")

here = Path(__file__).parent


@app.command(
    name="install",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
@set_context
def install(
    ctx: typer.Context,
    config_file: StdPath = typer.Option(
        None,
        "--config-file",
        exists=True,
        dir_okay=False,
        help="The path to your MkDocs configuration file.",
    ),
):
    """
    Install a kit. This command supports all options of [cyan]pip install[/cyan] in addition to the ones listed
    below.
    """
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
        kit = next(k for k in kits if k["name"] == kit_config.name)
    except StopIteration:
        raise Iconoquit(f'Kit "{kit_config.name}" does not exist')

    icons = kit["iconUploads"]

    with TemporaryDirectory() as tmpdir:
        with Path(tmpdir) as tmp:
            iconokit_root = tmp / "iconokit"
            iconokit_pkg = iconokit_root / "iconokit"

            (here / "iconokit").copytree(iconokit_root)
            (iconokit_pkg / ".token").write_text(kit["token"])

            icons_dir = (
                iconokit_pkg / ".overrides" / ".icons" / "fontawesome" / "kit"
            ).makedirs_p()

            for icon in icons:
                svg = (
                    f"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 {icon['width']} "
                    f"{icon['height']}\"><path d=\"{icon['path']}\"/></svg>"
                )
                (icons_dir / icon["name"]).with_suffix(".svg").write_text(svg)

            with Halo(
                text=f"Installing {kit_config.name}...", spinner="dots"
            ) as spinner:
                subprocess.run(
                    f"pip install {iconokit_root.abspath()} {' '.join(ctx.args)}".split(),
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT,
                )
                spinner.succeed(f"Kit installed!")


@app.callback(
    no_args_is_help=True,
    epilog=f"Iconoclast © {datetime.now().year} celsius narhwal. Thank you kindly for your attention.",
)
def main():
    """
    Iconoclast integrates Font Awesome Pro with Material for MkDocs.
    """
