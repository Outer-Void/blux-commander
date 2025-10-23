"""Tests for CLI wiring."""

from typer.testing import CliRunner

from blux_commander import cli

runner = CliRunner()


def test_status_command_runs() -> None:
    result = runner.invoke(cli.app, ["cmd", "status"])
    assert result.exit_code == 0
    assert "BLUX Commander Status" in result.stdout
