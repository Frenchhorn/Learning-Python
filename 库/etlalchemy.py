# https://github.com/seanharr11/etlalchemy
# select schema
# https://github.com/seanharr11/etlalchemy/issues/7

# virtualenv -p C:\Python27\python.exe python2 --system-site-packages
# pip install etlalchemy

# install cx_oracle
# https://pypi.python.org/pypi/cx_Oracle/5.3
# install oracle
# http://www.oracle.com/technetwork/topics/winx64soft-089540.html
# unzip and copy .dll in \instantclient_12_2 to \Python27\Lib\site-packages

# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

from etlalchemy import ETLAlchemySource, ETLAlchemyTarget
oracle_db_source = ETLAlchemySource("oracle://username:password@host:port/SID")
# ETLAlchemySource("oracle://username:password@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=xxx)(PORT=xxx))(CONNECT_DATA=(SERVICE_NAME=xxx)))")
sqlite_db_target = ETLAlchemyTarget("sqlite:///C:/.../target.db")
sqlite_db_target.addSource(oracle_db_source)
sqlite_db_target.migrate()
