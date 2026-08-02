import sqlite3
import json
from pathlib import Path


class DBSchema:

    def __init__(self):
        # Project Root
        self.project_root = Path(__file__).resolve().parents[2]
        self.db_path = self.project_root / "db.sqlite3"

    def get_table_schema(self, table_name):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(f"PRAGMA table_info('{table_name}')")

        columns = dict()

        for column in cursor.fetchall():

            columns[column[1]] = "null"
        conn.close()

        return columns

    def get_database_schema(self):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            AND name NOT LIKE 'sqlite_%'
        """)

        tables = [row[0] for row in cursor.fetchall()]

        conn.close()

        database = {}

        for table in tables:
            database[table] = self.get_table_schema(table)

        return database

    def get_schema_json(self, table_name=None):

        if table_name:
            return json.dumps(
                self.get_table_schema(table_name),
                indent=4
            )

        return json.dumps(
            self.get_database_schema(),
            indent=4
        )

    def print_schema(table_name):  
            db = DBSchema()  
            return db.get_schema_json("candidates_candidates")

if __name__ == "__main__":

    db = DBSchema()

    print(
        db.get_schema_json("candidates_candidates")
    )