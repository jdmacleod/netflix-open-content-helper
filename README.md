# Netflix Open Content Helper

A command-line utility for downloading test frames from [Netflix Open Content](https://opencontent.netflix.com).

![GitHub branch check runs](https://img.shields.io/github/check-runs/jdmacleod/netflix-open-content-helper/main)
![GitHub License](https://img.shields.io/github/license/jdmacleod/netflix-open-content-helper)

[![Tests Status](./tests/reports/junit/tests-badge.svg?dummy=8484744)](./tests/reports/junit/report.html)
[![Coverage Status](./tests/reports/coverage/coverage-badge.svg?dummy=8484744)](./tests/reports/coverage/index.html)
[![codecov](https://codecov.io/gh/jdmacleod/netflix-open-content-helper/branch/main/graph/badge.svg)](https://codecov.io/gh/jdmacleod/netflix-open-content-helper)

## Prerequisites

You will need the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) installed and available in `$PATH` to download frame content. No AWS account is needed however, as we use `-no-sign-request` when downloading files.

## Quickstart

Install using [pip](https://pypi.org/project/pip/) or [pipx](https://pipx.pypa.io/stable/).

```bash
$ pip install netflix-open-content-helper
```

or

```bash
$ pipx install netflix-open-content-helper
```

This will provide the command-line utility `noc`.

### Using `noc` with Netflix Open Content

Download the first frame of [Sparks](https://opencontent.netflix.com/#h.d0oh6u8prqhe) to the current directory.

```bash
$ noc download sparks
Downloading: sparks frames 1-1
Downloading... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:11
```

List the available Netflix Open Content Assets with frame content.

```bash
$ noc list
Available content with frames:
- chimera             : Live action footage, 4K. Download configured for the 23.98fps frame rate version. TIFF files.
- cosmoslaundromat    : Animated short film done in Blender, 2K 24p. EXR files.
- meridian            : Live action noir UHD short, 59.94fps. Mastered in Dolby Vision HDR. TIFF files.
- sparks              : Live action 4K HDR test short, 59.94fps, finished at 4000 nits. ACES EXR files.
```

Open a new web browser window to the [Netflix Open Content URL](https://opencontent.netflix.com).

```bash
$ noc browse
... (web browser opens)
```

## Developer Setup

Clone this repository (or fork on GitHub).

In the local repository directory, set up for Python development. The steps below show [Astral's uv](https://docs.astral.sh/uv/) in use - but using Python [venv](https://docs.python.org/3/library/venv.html) is also fine.

```bash
# Create and activate Python virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies with the project set as editable
uv pip install -e ".[dev]"

# Install Git pre-commit hooks
pre-commit install
```

Create a feature branch and make changes. See [TESTS.md](./TESTS.md) for details on running this product's tests.

## Contributing

Contributions to improve this utility are welcome! Please submit [issues](https://github.com/jdmacleod/netflix-open-content-helper/issues) and [pull requests](https://github.com/jdmacleod/netflix-open-content-helper/pulls) on GitHub.

## License

This code is MIT licensed. See the [LICENSE](LICENSE) file for details.

## Credits

Created and maintained by [Jason MacLeod](https://github.com/jdmacleod).

## Reference

See the [REFERENCE.md](./REFERENCE.md) for details on how this project is set up, including developer details.

Made using [Marc Goodner's Python Template](https://github.com/robotdad/python-template)
