# Changelog[^1]

Notable changes to Iconoclast will be documented here. Breaking changes are marked with a 🚩.

Iconoclast adheres to [semantic versioning](https://semver.org/spec/v2.0.0.html).

## <a name="3.0.1">[3.0.1] - 2024-11-22</a>

### Fixed

- A minor spelling error.

## <a name="3.0.0">[3.0.0] - 2024-11-10</a>

### Changes

- 🚩 Iconoclast now requires Python 3.8 or later.
- 🚩 `iconoclast install`, which previous installed specified Font Awesome Kit, now installs Font Awesome Pro.
- 🚩 `iconoclast kit` is the new command for installing a Font Awesome Kit.
- 🚩 The `iconoclast setup` command has been removed and replaced by `iconoclast install`.

## <a name="2-1-0">[2.1.0] - 2023-06-04</a>

### Added

- Font Awesome Pro can now be installed via the new `iconoclast setup` command. This command supersedes the old,
  package manager-dependent, ways of installing Font Awesome Pro, which still work, but are no longer documented or
  supported. ([Docs](https://iconoclast.celsiusnarhwal.dev/#installation-and-setup))

## <a name="2-0-3">[2.0.3] - 2023-05-16</a>

### Fixed

- Fixed a bug where Iconoclast might fail when determining whether `iconocards` is deprecated for the installed version
  of Material for MkDocs.

## <a name="2-0-2">[2.0.2] - 2023-05-16</a>

### Changed

- The `iconocards` plugin now emits a deprecation warning on versions of Material for MkDocs where it is obsolete.
- Iconoclast's warning and error messages are now visually consistent with those emitted by MkDocs.

## <a name="2-0-1">[2.0.1] - 2023-05-11</a>

### Fixed

- Fixed a bug where Iconoclast's command-line interface would fail.

## <a name="2-0-0">[2.0.0] - 2023-05-05</a>

🚩 fa-material is now **Iconoclast**. To upgrade, uninstall fa-material and install Iconoclast:

```bash
pip uninstall fa-material && pip install iconoclast
```

### Added

- Iconoclast now has CSS support, enabling you use Font Awesome icons in block and partial
  overrides. ([Docs](https://iconoclast.celsiusnarhwal.dev#css-support))
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
