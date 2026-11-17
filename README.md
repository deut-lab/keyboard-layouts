# RuUa and EnDe keyboard layouts for Windows

**English** · [Deutsch](README.de.md) · [Українська](README.uk.md) · [Русский](README.ru.md)

Two layouts to type Russian, Ukrainian, German and English without extra switching.

- **RuUa**: the Russian ЙЦУКЕН layout that also has the Ukrainian letters ґ, і, ї, є.
- **EnDe**: the English QWERTY layout that also has the German letters ä, ö, ü, ß.

Letters stay where you are used to them; extra characters are typed with the **right Alt key** (AltGr).

**Keyboard pictures and why everything is placed this way:** https://deut-lab.github.io/keyboard-layouts/

## Install

1. Download an archive from the [release page](https://github.com/deut-lab/keyboard-layouts/releases/latest): `RuUa2611.zip` or `EnDe2611.zip`.
2. Unpack it and run `setup.exe`. Allow it when Windows asks for administrator rights.
3. Sign out of Windows and sign in again.
4. Open Settings, then "Time & language" and "Language & region". Next to your language press "…", then "Language options" and "Add a keyboard", and choose **Russia-Ua 20261117** (for Russian) or **LAT-DEU 20261117** (for English).

If Windows says "Windows protected your PC", click "More info" and "Run anyway". It appears because the installer has no paid digital signature.

The layouts do not work on computers with ARM processors (Snapdragon, Surface Pro X).

To remove a layout, open Settings, then "Apps" and "Installed apps", find its name and click "Uninstall".

## What is inside

| Folder | Contents |
| --- | --- |
| `src` | layout sources `.klc`, they open in Microsoft Keyboard Layout Creator 1.4 |
| `docs` | the website with keyboard pictures |
| `scripts` | `klc_to_svg.py` draws a keyboard picture from a `.klc` file, `build_site.py` builds the website |

Ready installers are on the release page, not in the folders.

## License

[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/): free to download, use and share unchanged with credit to Deut-lab; no commercial use, no modified versions. See [LICENSE.md](LICENSE.md).
