import re
from unittest import TestCase
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import CreateSchema


class TestCreateSchemaCommand(TestCase):

    def test_basic_create_schema(self):

        expected_result = re.sub(r'\s+', '', "CREATE SCHEMA abc").strip()
        engine = create_engine('redshift+psycopg2://')
        ddl_statement = re.sub(r'\s+', '', str(CreateSchema("abc").compile(engine)).strip())
        self.assertEqual(expected_result, ddl_statement)
