"""
The order of these imports is important. Test cases are imported first from SQLAlchemy,
then are overridden by our local skip markers in _regression, _unsupported, and _future.
"""


# type: ignore
# fmt: off
from sqlalchemy.testing.suite import *
from databricks_sql.sqlalchemy.test._regression import *
from databricks_sql.sqlalchemy.test._unsupported import *
from databricks_sql.sqlalchemy.test._future import *
from databricks_sql.sqlalchemy.test._extra import TinyIntegerTest, DateTimeTZTestCustom
