import re
from unittest import TestCase
from sqlalchemy.engine import create_engine
from sqlalchemy.sql.ddl import CreateTable
from sqlalchemy.sql.schema import MetaData, Column, Table
from sqlalchemy.sql.sqltypes import Integer


class TestCreateTableCommand(TestCase):

    def test_basic_create_table(self):
        expected_result = re.sub(r'\s+', '', "CREATE TABLE testtable (col1 INTEGER)").strip()

        engine = create_engine('redshift+psycopg2://')
        table_model = Table("testtable", MetaData(), Column("col1", Integer))
        ddl_statement = re.sub(r'\s+', '', str(CreateTable(table_model).compile(engine)).strip())

        self.assertEqual(expected_result, ddl_statement)
