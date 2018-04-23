import re
from unittest import TestCase
from redshift_sqlalchemy.dialect import CopyCommand


class TestCopyCommand(TestCase):

    def test_basic_copy_case(self):
        expected_result = re.sub(r'\s+', ' ',
                                  "COPY schema1.t1 FROM 's3://mybucket/data/listing/' "
                                  "CREDENTIALS 'aws_access_key_id=cookies;aws_secret_access_key=cookies' CSV "
                                  "TRUNCATECOLUMNS EMPTYASNULL BLANKSASNULL DELIMITER ',' IGNOREHEADER 0 ;").strip()
        copy = CopyCommand('schema1', 't1', 's3://mybucket/data/listing/', 'cookies', 'cookies')
        copy_str = re.sub(r'\s+', ' ', str(copy)).strip()
        self.assertEqual(expected_result, copy_str)
