# Changelog[^1]

Notable changes to Iconoclast will be documented here. Breaking changes are marked with a 🚩.

Iconoclast adheres to [semantic versioning](https://semver.org/spec/v2.0.0.html).

## <a name="2-0-0">[2.0.0] - 2023-05-05</a>

🚩 fa-material is now **Iconoclast**. To upgrade, uninstall fa-material and install Iconoclast:

```bash
pip uninstall fa-material && pip install iconoclast
```

### Added

- Iconoclast now has CSS support, enabling you use Font Awesome icons in block and partial overrides. ([Docs](https://iconoclast.celsiusnarhwal.dev#css-support))
- Iconoclast now supports Font Awesome Kits, allowing you to seamlessly bring your own custom icons to Material for
  MkDocs. ([Docs](https://iconoclast.celsiusnarhwal.dev#using-kits))

### Changed

- 🚩 Iconoclast's plugin is now named `iconoclast`.
- 🚩 Support for Font Awesome 5 has been removed. Iconclast supports Font Awesome 6 only.
  - 🚩 The `version` configuration option has also been removed.

## <a name="1-1-0">[1.1.0] - 2023-04-27</a>

## Added

- fa-material now supports Font Awesome 5 (it previously only supported Font Awesome 6). To use Font Awesome 5, set
  the `version` option of the `fontawesome-pro` plugin to `5` (the default is `6`).

      ```yaml
      plugins:
        - fontawesome-pro:
            version: 5
      ```

## <a name="1-0-1">[1.0.1] - 2023-04-27</a>

### Changed

- fa-material's Python version constraint has been relaxed to 3.7+.

## <a name="1-0-0">[1.0.0] - 2023-04-27</a>

This is the initial release of fa-material.

[^1]: Based on [Keep a Changelog](https://keepachangelog.com)
