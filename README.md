# toy01_table_stripper

This is a minimal Python package that demonstrates how to use the `uv` tool for
managing dependencies and running the application.

## Development

Create a virtual environment and install dependencies using `uv`:

```bash
uv venv
uv pip install -e .
```

Run the command-line interface by piping an HTML file:

```bash
cat sample.html | toy01-table-stripper
```

