import MySQLdb

conn = MySQLdb.connect(
    user = 'dev',
    password = 'secret',
    db = 'flask',
    host = 'localhost',
    port = 3306
)