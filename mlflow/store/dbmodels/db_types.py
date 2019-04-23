"""
Set of SQLAlchemy database schemas supported in MLflow for tracking server backends.
"""
import os
POSTGRES = 'postgresql'
MYSQL = os.environ.get("MYSQLDB",'mysql+pymysql')   #os.environ['MYSQLDB']  #'mysql'
SQLITE = 'sqlite'
MSSQL = 'mssql'

DATABASE_ENGINES = [
    POSTGRES,
    MYSQL,
    SQLITE,
    MSSQL
]
