# coding: utf-8
"""Utility to connect to an Oracle database and export table schema
information as an Excel document.

This script requires the following external dependencies:
- cx_Oracle
- openpyxl

Install them via pip before running this script:
    pip install cx_Oracle openpyxl
"""
from __future__ import annotations

import os
from typing import List, Tuple

try:
    import cx_Oracle
except ImportError:  # pragma: no cover - library might not be available
    cx_Oracle = None

try:
    from openpyxl import Workbook
except ImportError:  # pragma: no cover - library might not be available
    Workbook = None


class OracleSchemaExporter:
    """Class responsible for extracting schema information from Oracle."""

    def __init__(self, dsn: str, user: str, password: str):
        if cx_Oracle is None:
            raise RuntimeError("cx_Oracle is required for this script")
        self.connection = cx_Oracle.connect(user, password, dsn)

    def fetch_tables(self) -> List[str]:
        """Return a list of table names available to the user."""
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT table_name FROM user_tables")
            return [row[0] for row in cursor.fetchall()]

    def fetch_columns(self, table: str) -> List[Tuple[str, str, str]]:
        """Return column definitions for a given table.

        Returns a list of tuples containing column name, type, and nullable
        (YES/NO).
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                """SELECT column_name, data_type, nullable
                   FROM user_tab_columns
                   WHERE table_name = :tbl
                   ORDER BY column_id""",
                tbl=table,
            )
            return [(row[0], row[1], row[2]) for row in cursor.fetchall()]


class ExcelWriter:
    """Helper class to write schema information into an Excel file."""

    def __init__(self, path: str):
        if Workbook is None:
            raise RuntimeError("openpyxl is required for this script")
        self.workbook = Workbook()
        self.path = path

    def write_table(self, table: str, columns: List[Tuple[str, str, str]]):
        sheet = self.workbook.create_sheet(title=table)
        sheet.append(["Column", "Type", "Nullable"])
        for col, dtype, nullable in columns:
            sheet.append([col, dtype, nullable])

    def save(self):
        # Remove the default sheet created by openpyxl
        default_sheet = self.workbook["Sheet"]
        self.workbook.remove(default_sheet)
        self.workbook.save(self.path)


def export_schema_to_excel(dsn: str, user: str, password: str, output_path: str):
    """Export Oracle schema to an Excel workbook."""
    exporter = OracleSchemaExporter(dsn, user, password)
    writer = ExcelWriter(output_path)

    for table in exporter.fetch_tables():
        columns = exporter.fetch_columns(table)
        writer.write_table(table, columns)

    writer.save()


if __name__ == "__main__":  # pragma: no cover - manual usage
    dsn = os.environ.get("ORACLE_DSN", "localhost/orclpdb")
    user = os.environ.get("ORACLE_USER", "scott")
    password = os.environ.get("ORACLE_PASSWORD", "tiger")
    output_path = os.environ.get("OUTPUT_EXCEL", "schema.xlsx")
    export_schema_to_excel(dsn, user, password, output_path)
