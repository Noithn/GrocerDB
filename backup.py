import sqlite3, io
from GDB import dbname, conn

with io.open('backup_dump.sql', 'w') as p:
    for line in conn.iterdump():
        p.write('%s\n' % line)
print('Backup created')
conn.close()