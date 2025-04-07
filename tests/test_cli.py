"""Tests for the Netflix Open Content Helper package."""

import pytest
from typer.testing import CliRunner

from netflix_open_content_helper.cli import app

runner = CliRunner(mix_stderr=False)


def test_app_reports_version() -> None:
    """Test that the version is reported."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "Netflix Open Content Helper, version" in result.stdout


def test_app_lists_frame_content_by_default() -> None:
    """Test that the default list action shows frame content."""
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "with frames" in result.stdout
    assert "chimera" in result.stdout
    assert "cosmoslaundromat" in result.stdout


def test_app_lists_nonframe_content_with_option() -> None:
    """Test that the list action can optionally show non-frame content."""
    result = runner.invoke(app, ["list", "--no-only-frames"])
    assert result.exit_code == 0
    assert "with frames" not in result.stdout
    assert "chimera" in result.stdout
    assert "cosmoslaundromat" in result.stdout
    assert "elfuente" in result.stdout
    assert "nocturne" in result.stdout


def test_app_download_validates_frame_options() -> None:
    """Test that the download frame numbers are validated."""
    with pytest.raises(ValueError) as excinfo:
        runner.invoke(
            app, ["download", "sparks", "-fs", -1, "-fe", 0], catch_exceptions=False
        )
    assert "must be positive integers." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        runner.invoke(
            app, ["download", "sparks", "-fs", 2, "-fe", 1], catch_exceptions=False
        )
    assert "must be less than or equal to end frame" in str(excinfo.value)


def test_app_download_has_dry_run_option() -> None:
    """Test that the download honors dry-run mode."""
    result = runner.invoke(app, ["download", "sparks", "-n"])
    assert "dry-run" in result.stdout


def test_app_download_validates_rename_option() -> None:
    """Test that the download rename string is validated."""
    with pytest.raises(ValueError) as excinfo:
        runner.invoke(
            app,
            ["download", "sparks", "-n", "--rename", "newname"],
            catch_exceptions=False,
        )
    assert "contain a frame substitution wildcard like %04d." in str(excinfo.value)


def test_app_download_renumber_option_requires_rename_option() -> None:
    """Test that the download rename string is validated."""
    with pytest.raises(ValueError) as excinfo:
        runner.invoke(
            app, ["download", "sparks", "-n", "--renumber", 5], catch_exceptions=False
        )
    assert "Option --renumber requires --rename." in str(excinfo.value)
