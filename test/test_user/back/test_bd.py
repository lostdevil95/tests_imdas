import psycopg2
from psycopg2.extras import DictCursor

conn = psycopg2.connect(
            user='****',
            password='*****',
            host='******',
            database='****',
            port='5434'
        )

cursor = conn.cursor(cursor_factory=DictCursor)
cursor.execute('''select * from systems_systemstatus''')
status = cursor.fetchall()
for stat in status:
    print(stat[1:5])
    if sum(stat[1:5]) == 4:
        print('OK')
    else:
        print('Services do not work')
cursor.close()
conn.close()

