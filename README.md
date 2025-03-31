# Netflix Open Content Helper

A command-line utility to assist with downloading test files from [Netflix Open Content](https://opencontent.netflix.com).

## Quickstart

Download the first frame of [Sparks](https://opencontent.netflix.com/#h.d0oh6u8prqhe) to the current directory.

```bash
noc download --name sparks --frame-start 1 --frame-end 1
Downloading: sparks 1-1
download: s3://download.opencontent.netflix.com/sparks/aces_image_sequence_59_94_fps/SPARKS_ACES_00001.exr to ./SPARKS_ACES_00001.exr
```

List the available Open Content Assets with frame content.

```bash
noc list
Available content with frames:
- chimera: Live action footage, 4K. Download configured for the 23.98fps frame rate version. TIFF files.
- cosmos_laundromat: Animated short film done in Blender, 2K 24p. EXR files.
- meridian: Live action noir UHD short, 59.94fps. Mastered in Dolby Vision HDR. TIFF files.
- sparks: Live action 4K HDR test short, 59.94fps, finished at 4000 nits. ACES EXR files.
```

Open a new web browser window to the [Netflix Open Content URL](https://opencontent.netflix.com).

```bash
noc browse
```

### Initial Setup

```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies
uv pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

## Contributing

Contributions to improve this utility are welcome! Please submit issues and pull requests on GitHub.

## License

This code is MIT licensed. See the [LICENSE](LICENSE) file for details.

## Credits

Created and maintained by [Jason MacLeod](https://github.com/jdmacleod).

## Reference

See the [REFERENCE.md](./REFERENCE.md) for details on how this project is set up, including developer details.

Made using [Marc Goodner's Python Template](https://github.com/robotdad/python-template)
