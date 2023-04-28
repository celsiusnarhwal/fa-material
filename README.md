# fa-material

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fa-material?logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/fa-material)
[![PyPI](https://img.shields.io/pypi/v/fa-material?logo=pypi&color=green&logoColor=white&style=for-the-badge)](https://pypi.org/project/fa-material)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/celsiusnarhwal/fa-material?logo=github&color=orange&logoColor=white&style=for-the-badge)](https://github.com/celsiusnarhwal/fa-material/releases)
[![PyPI - License](https://img.shields.io/pypi/l/fa-material?color=03cb98&style=for-the-badge)](https://github.com/celsiusnarhwal/fa-material/blob/main/LICENSE.md)
[![Code style: Black](https://aegis.celsiusnarhwal.dev/badge/black?style=for-the-badge)](https://github.com/psf/black)

fa-material is the easiest way to use [Font Awesome](https://fontawesome.com/) [Pro](https://fontawesome.com/plans) icons in
your [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) project.

An active Font Awesome Pro license is required to use fa-material.

## Installation

1. [Install Font Awesome Pro's Python package](https://fontawesome.com/docs/web/use-with/python-django#using-font-awesome-pro-with-django).
2. Install fa-material.

   ```bash
   pip install fa-material
   ```

## Usage

Add the `fontawesome-pro` plugin to `mkdocs.yml`:

```yaml
plugins:
  - fontawesome-pro
```

That's it. You can now use Font Awesome Pro icons in the same way you already do Font Awesome Free icons (e.g.
`:fontawesome-thin-user-secret:`). They'll work in Markdown files, `mkdocs.yml`, and anywhere else Material for MkDocs'
icon system is used.

### Font Awesome 5

You can use Font Awesome 5 with fa-material by setting `fontawesome-pro`'s `version` option to `5`.

```yaml
plugins:
  - fontawesome-pro:
      version: 5
```

This option must be either `5` or `6`, defaulting to the latter.

## License

fa-material is licensed under the [MIT License](LICENSE.md).
