---
description: Font Awesome Pro integration for Material for MkDocs
---

# Iconoclast

Iconoclast integrates [Font Awesome](https://fontawesome.com/) [Pro](https://fontawesome.com/plans) with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material). It makes
using Font Awesome Pro icons in your site as easy as using Font Awesome Free icons already is.[^1]
And with support for Font Awesome Kits[^2], using your own custom icons is just as simple.

[^1]: https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/
[^2]: https://fontawesome.com/docs/web/setup/use-kit

??? question "Material for MkDocs already has a mechanism for [adding custom icons](https://squidfunk.github.io/mkdocs-material/setup/changing-the-logo-and-icons/?h=bootstrap#additional-icons). Why do I need Iconoclast?"

    You *could* download Font Awesome Pro, unzip it, and copy the SVG files into your project, but then you wouldn't
    be able to publish your project to GitHub without violating the [Font Awesome Pro license](https://fontawesome.com/support#what-cant-i-do-with-a-font-awesome-pro-license).
    Iconoclast allows you to use Font Awesome Pro icons in your project without exposing them in your codebase.

## Prerequisites

<div class="annotate" markdown>

- [:fontawesome-brands-font-awesome: Font Awesome Pro](https://fontawesome.com/plans) (1)
- [:logo: Material for MkDocs](https://squidfunk.github.io/mkdocs-material)

</div>

1. Only Font Awesome 6 is supported by Iconoclast.

## Installation

You'll need to install Font Awesome Pro's Python package alongside Iconoclast.

Grab your Font Awesome package manager token from your [Font Awesome account page](https://fontawesome.com/account)
and bind it to the `FONTAWESOME_PKG_TOKEN` environment variable.

```bash
export FONTAWESOME_PKG_TOKEN={FONTAWESOME_TOKEN} # (1)!
```

1. Replace `{FONTAWESOME_TOKEN}` with your Font Awesome token.

Then, follow the instructions for your package manager.

=== ":fontawesome-brands-python: pip"

    Add the following to your `requirements.txt`:

    [comment]: <> (This code block is marked as TOML for annotation support only.)

    === ":octicons-file-code-16: `requirements.txt`"

        ```toml
        iconoclast >= 2.0.0, < 3.0.0
        ---extra-index-url https://dl.fontawesome.com/${FONTAWESOME_PKG_TOKEN}/fontawesome-pro/python/simple
        fontawesomepro >= 6.0.0, < 7.0.0
        ```
    Then run:

    ```bash
    pip install -r requirements.txt
    ```

=== ":simple-poetry: Poetry"

    Install [poetry-source-env](https://github.com/celsiusnarhwal/poetry-source-env):

    ```bash
    poetry self add poetry-source-env
    ```

    Add the following to your `pyproject.toml`:

    === ":octicons-file-code-16: `pyproject.toml`"

        ```toml
        [[tool.poetry.source]]
        name = "fontawesome"
        url = "https://dl.fontawesome.com/${FONTAWESOME_PKG_TOKEN}/fontawesome-pro/python/simple"
        secondary = true
        ```

    Then run:

    ```bash
    poetry add iconoclast && poetry add fontawesomepro --source fontawesome
    ```

=== ":pdm: PDM"

    Add the following to your `pyproject.toml`:

    === ":octicons-file-code-16: `pyproject.toml`"

        ```toml
        [tool.pdm.resolution]
        respect-source-order = true

        [[tool.pdm.source]]
        name = "fontawesome"
        url = "https://dl.fontawesome.com/${FONTAWESOME_PKG_TOKEN}/fontawesome-pro/python/simple"
        verify_ssl = true

        [[tool.pdm.source]]
        name = "pypi" # (1)!
        url = "https://pypi.org/simple"
        verify_ssl = true
        ```

        1. Explicitly including PyPI while enabling `tool.pdm.resolution.respect-source-order` forces PDM to prefer
        Font Awesome's package index over PyPI, preventing potential dependency injection attacks if say, a bad actor
        were to publish a malicious package named `fontawesomepro` to PyPI.

    Then run:

    ```bash
    pdm add iconoclast fontawesomepro
    ```

## Configuration

!!! warning "Iconoclast requires emoji"

    Before using Iconoclast, make sure your Material for MkDocs site has been [configured to use emoji](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#configuration):

    === ":octicons-file-code-16: `mkdocs.yml`"

        ```yaml
        markdown_extensions:
            - attr_list
            - pymdownx.emoji:
                emoji_index: !!python/name:materialx.emoji.twemoji
                emoji_generator: !!python/name:materialx.emoji.to_svg
        ```

The simplest possible configuration is just adding the `iconoclast` plugin to `mkdocs.yml`:

=== ":octicons-file-code-16: `mkdocs.yml`"

    ```yaml
    plugins:
        - iconoclast
    ```

You can now use Font Awesome Pro icons in Markdown files just as you would Font Awesome Free icons. For example,
`:fontawesome-duotone-icons:` will now render as :fontawesome-duotone-icons:.

### Social Cards

!!! warning "Deprecation warning"

    If you're using [Material for MkDocs Insiders](https://squidfunk.github.io/mkdocs-material/insiders/) 4.33.0 or
    later, the built-in social plugin has undergone a rewrite that renders `iconocards` obsolete. You can safely ignore
    the content of this section and use the built-in social plugin as normal.

    As of Iconoclast 2.0.2, `iconocards` will emit a deprecation warning on versions of Material for MkDocs where it is
    no longer needed.

Iconoclast's `iconocards` plugin is **required** to use Iconoclast icons in social cards generated by Material for
MkDocs' built-in social plugin.[^3]

[^3]: https://squidfunk.github.io/mkdocs-material/setup/setting-up-social-cards/

To use `iconocards`, you must **remove** the built-in social plugin from `mkdocs.yml`. Don't worry — `iconocards` is
fully backwards-compatible with the built-in social plugin; you won't lose any functionality.

=== ":octicons-file-code-16: `mkdocs.yml`"

    ```yaml
    plugins:
        - iconoclast
        - iconocards # (1)!
    ```

    1. `iconocards` **must** be declared *after* `iconoclast`.

`iconocards` supports all [configuration options](https://squidfunk.github.io/mkdocs-material/setup/setting-up-social-cards/?h=social#built-in-social-plugin) of the built-in social plugin.

### CSS Support

If you want to use Font Awesome icons when [overriding blocks or partials](https://squidfunk.github.io/mkdocs-material/customization/#overriding-partials),
Iconoclast can automatically add the necessary CSS to your site so that you can reference Font Awesome
as you would in any other website (e.g, `#!html <i class="fa-solid fa-rocket"></i>` would render as
:fontawesome-solid-rocket:).

You can do this via the following configuration option:

`css`

: :octicons-milestone-24: Default: `false` — Whether to add Font Awesome's CSS to your site.

    === ":octicons-file-code-16: `mkdocs.yml`"

        ```yaml
        plugins:
          - iconoclast:
              css: true
        ```

### Using Kits

Have a Font Awesome Kit[^2] with custom icons that you'd like
to use in your project? Iconoclast has you covered.

To use a Kit, you'll have to set up the following configuration options:

<div class="annotate" markdown>

`kit.name`

: :octicons-milestone-24: The name of the Kit to use.

    === ":octicons-file-code-16: `mkdocs.yml`"

        ```yaml
        plugins:
          - iconoclast:
              kit:
                name: Jajankit
        ```

`kit.token`

: :octicons-milestone-24: Default: `#!yaml !ENV FONTAWESOME_API_TOKEN` — Your Font Awesome API token. (1)

    === "Via `FONTAWESOME_API_TOKEN`"

        If your token is bound to the `FONTAWESOME_API_TOKEN` environment variable, Iconoclast will detect it
        automatically and you can omit this option from `mkdocs.yml`.

        === ":octicons-file-code-16: `mkdocs.yml`"

            ```yaml
            plugins:
              - iconoclast:
                  kit:
                    name: Jajankit
            ```

    === "Via another environment variable"

        If your token is bound to an environment variable other than `FONTAWESOME_API_TOKEN`, you can specify it with
        the `#!yaml !ENV` tag.

        === ":octicons-file-code-16: `mkdocs.yml`"

            ```yaml
            plugins:
                - iconoclast:
                    kit:
                      name: Jajankit
                      token: !ENV SOME_ENVIRONMENT_VARIABLE
            ```

    === "Via explicit hardcoding"

        You can explicitly hardcode your token in `mkdocs.yml` if you want, though this is obviously not recommended.

        === ":octicons-file-code-16: `mkdocs.yml`"

            ```yaml
            plugins:
                - iconoclast:
                    kit:
                      name: Jajankit
                      token: OATO-GA-MATA-YORUSHIKUTE (2)
            ```

</div>

1. This is distinct from your Font Awesome package manager token. You can find your API token on your
   [Font Awesome account page](https://fontawesome.com/account) (you may need to generate one first).

2. Replace with your actual API token.

Once you've configured your Kit, you need to install it:

```bash
iconoclast install # (1)!
```

1. If you're a fan of shortcuts, `icl install` also works.

You can then reference your custom icons in Markdown files with the syntax `:fontawesome-kit-[icon-name]:`
(e.g. `:fontawesome-kit-solid-rakugo-sensu:`).

If you've enabled [CSS Support](#css-support), you can also reference your custom icons in HTML files with the syntax
`#!html <i class="fa-kit fa-[icon-name]"></i>` (e.g. `#!html <i class="fa-kit fa-solid-rakugo-sensu"></i>`).

!!! tip

    You need to rerun `iconoclast install` every time you make a change to your Kit's name or custom icons.

!!! warning "Using CSS with Kits counts against your pageviews"

    Font Awesome allots you a certain number of Kit pageviews per month.[^4] If you use Iconoclast's CSS support with a
    Kit, Iconoclast will serve your CSS via Font Awesome's CDN rather than bundling it with your site, which means that
    every time someone visits your site, it will count against your pageviews.

[^4]: https://fontawesome.com/docs/web/setup/use-kit#kits-and-pageviews
