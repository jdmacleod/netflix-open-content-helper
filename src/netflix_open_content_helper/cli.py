import subprocess
import webbrowser

import typer

from netflix_open_content_helper import CONFIG, __version__


def download_from_s3(s3_uri: str, s3_path: str, dest_path: str = ".") -> None:
    """
    Download a file from S3.

    Args:
        s3_uri (str): The base S3 URI.
        s3_path (str): The specific path to the file in S3.
        dest_path (str): The destination path for the downloaded file.
    """
    commands = [
        "aws",
        "s3",
        "cp",
        "--no-sign-request",
        f"{s3_uri}/{s3_path}",
        dest_path,
    ]
    subprocess.run(commands, check=True)


def version_callback(value: bool) -> None:
    """Display the version of the package."""
    if value:
        typer.echo(f"Netflix Open Content Helper, version {__version__}")
        raise typer.Exit()


app = typer.Typer()


@app.callback()
def common(
    version: bool = typer.Option(
        False,
        "--version",
        is_eager=True,
        help="Show the version of the package.",
        callback=version_callback,
    ),
) -> None:
    """A helper suite for Netflix Open Content media."""
    pass


@app.command()
def browse() -> None:
    """
    Open a web browser for Netflix Open Content.
    """
    typer.echo("Open a new web browser pointed to the Open Content.")
    NETFLIX_OPEN_CONTENT_URL = CONFIG["netflix_open_content_url"]
    if not NETFLIX_OPEN_CONTENT_URL:
        raise ValueError("Netflix Open Content URL is not configured.")
    # Check if the URL is valid
    if not NETFLIX_OPEN_CONTENT_URL.startswith(("http://", "https://")):
        raise ValueError("Invalid URL format.")
    # Open the URL in the default web browser
    # This will open the URL in a new tab if the browser is already open
    # or in a new window if the browser is not open
    # Note: This will not work in a headless environment
    # such as a server without a GUI
    # or in a terminal without a web browser
    webbrowser.open_new(NETFLIX_OPEN_CONTENT_URL)


@app.command()
def download(
    name: str = typer.Option(..., help="The asset name."),
    frame_start: int = typer.Option(1, help="The start frame for the download."),
    frame_end: int = typer.Option(2, help="The end frame for the download."),
) -> None:
    """
    Download frame content from Netflix Open Content.
    """
    typer.echo("Download content.")
    typer.echo(f"Name: {name} {frame_start}-{frame_end}")
    # Validate the frame range
    if frame_start < 1 or frame_end < 1:
        raise ValueError("Frame numbers must be positive integers.")
    if frame_start > frame_end:
        raise ValueError("Start frame must be less than or equal to end frame.")
    # Validate the count
    count = frame_end - frame_start + 1
    if count < 1:
        raise ValueError("Count must be at least 1.")
    # Print the count
    typer.echo(f"Count: {count}")
    # Implement the download logic here
    # Check if the AWS CLI is installed
    test_commands = ["aws", "--version"]
    try:
        subprocess.run(test_commands, check=True, capture_output=True)
    except subprocess.CalledProcessError:
        raise OSError("AWS CLI is not installed.")
    # Obtain the asset configuration
    asset = [d for d in CONFIG["assets"] if d["name"] == name][0]
    if not asset:
        raise ValueError(f"Asset {name} not found.")
    # Check if the S3 URI is configured for the asset
    s3_uri = asset["s3_uri"]

    if not s3_uri:
        raise ValueError(f"S3 URI is not configured for {name}.")
    # Check if the S3 URI is valid
    if not s3_uri.startswith("s3://"):
        raise ValueError(f"Invalid S3 URI format {s3_uri}. Must start with 's3://'.")
    s3_basename = asset["s3_basename"]
    if not s3_basename:
        raise ValueError(f"S3 basename is not configured for {name}.")
    # Check if the S3 basename is valid
    if "%" not in s3_basename:
        raise ValueError(
            f"Invalid S3 basename format {s3_basename}. Must contain a frame wildcard like %04d."
        )
    # Generate the S3 path for each frame
    for frame in range(frame_start, frame_end + 1):
        # Generate the S3 path
        s3_path = s3_basename % frame
        # Download the content from S3
        download_from_s3(s3_uri, s3_path)


@app.command()
def list() -> None:
    """
    List available Netflix Open Content.
    """
    typer.echo("Available content:")
    for asset in sorted(CONFIG["assets"], key=lambda x: x["name"]):
        typer.echo(f"- {asset['name']}: {asset['description']}")


if __name__ == "__main__":
    app()
