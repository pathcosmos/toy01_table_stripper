# toy01_table_stripper

This project provides a small helper to strip `<table>` tags from HTML.
It also demonstrates how to manage dependencies using the `uv` tool.

## Development

Create a virtual environment and install the package in editable mode:

```bash
uv venv
uv pip install -e .
```

## Usage

Pipe HTML content into the CLI to remove any `<table>` elements:

```bash
cat sample.html | toy01-table-stripper
```

The stripped output will be printed to the console.

## Project Structure

- `toy01_table_stripper/__init__.py` – library function `strip_table`
- `toy01_table_stripper/main.py` – command-line interface
- `pyproject.toml` – project metadata and uv configuration


