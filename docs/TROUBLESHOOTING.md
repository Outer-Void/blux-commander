# Troubleshooting

## Common Issues

### TUI Does Not Start
- Ensure Textual >= 0.62 is installed.
- Check that the terminal supports rich color output.

### Plugins Missing
- Verify plugin directories in `config.yaml` and environment variables.
- Run `bluxq cmd plugins list --verbose` to display discovery paths.

### Telemetry Failures
- Confirm the telemetry directory is writable.
- Disable telemetry temporarily with `BLUX_CMD_TELEMETRY=off` and check logs.

## Collecting Diagnostics

Run `bluxq cmd status --verbose` to output detailed subsystem state, then attach the generated
JSONL telemetry snippet found in `~/.config/blux-commander/logs/` when filing support tickets.
