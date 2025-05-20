# Oracle Schema Exporter

This repository contains a simple script for exporting table definitions from
an Oracle database to an Excel workbook. The script relies on the `cx_Oracle`
package to connect to the database and `openpyxl` to create the Excel file.

## Usage

1. Install the required dependencies:
   ```bash
   pip install cx_Oracle openpyxl
   ```
2. Set environment variables to match your Oracle credentials and desired
   output file:
   - `ORACLE_DSN` – DSN string for the Oracle instance (e.g. `localhost/orclpdb`)
   - `ORACLE_USER` – database username
   - `ORACLE_PASSWORD` – database password
   - `OUTPUT_EXCEL` – path for the resulting Excel file

3. Run the exporter:
   ```bash
   python export_table_schema.py
   ```

Each table will be written to a separate sheet with columns for name, type, and
whether the column allows `NULL` values.
