"""Typer-based command line interface for BLUX Commander."""

from __future__ import annotations

import typer

from blux_commander.core import api, commander, plugins, telemetry, tui

app = typer.Typer(help="BLUX Commander — Unified Cockpit")
cmd_app = typer.Typer(help="Commander control surface")
app.add_typer(cmd_app, name="cmd")

plugins_app = typer.Typer(help="Plugin commands")
telemetry_app = typer.Typer(help="Telemetry commands")
ai_app = typer.Typer(help="AI console commands")

cmd_app.add_typer(plugins_app, name="plugins")
cmd_app.add_typer(telemetry_app, name="telemetry")
cmd_app.add_typer(ai_app, name="ai")

commander.bootstrap()


@cmd_app.command()
def dashboard() -> None:
    """Launch the Textual dashboard."""

    tui.launch_dashboard()


@cmd_app.command()
def status(verbose: bool = typer.Option(False, "--verbose", help="Show extended diagnostics")) -> None:
    """Print commander status."""

    commander.print_status(verbose=verbose)


@plugins_app.command("list")
def plugins_list(verbose: bool = typer.Option(False, "--verbose", help="Show discovery paths")) -> None:
    """List registered plugins."""

    plugins.list_registered(verbose=verbose)


@telemetry_app.command("tail")
def telemetry_tail(limit: int = typer.Option(10, help="Number of telemetry entries to show")) -> None:
    """Tail telemetry entries."""

    telemetry.tail(limit=limit)


@ai_app.command()
def ai(reflect: bool = typer.Option(False, "--reflect", help="Enable reflection mode")) -> None:
    """Interact with the AI developer console."""

    if reflect:
        print("Reflection mode activated. Awaiting conscious-agent guidance.")
    else:
        print("AI console ready. Use --reflect for guidance mode.")


@app.command()
def api_server(host: str = "127.0.0.1", port: int = 8000, reload: bool = False) -> None:
    """Run the FastAPI server."""

    api.run(host=host, port=port, reload=reload)


def get_app() -> typer.Typer:
    """Return the Typer app for entry-point exposure."""

    return app


if __name__ == "__main__":  # pragma: no cover
    app()
