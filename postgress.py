import psycopg2
con=psycopg2.connect(dbname='test', user='postgres', password='Q1w2e3r4', host='localhost')
cursor=con.cursor()
table="logins"
def select(columns,wcolumns,value):
    global cursor
    global table
    if len(wcolumns)>0:
        qwery = f'SELECT {columns} FROM public.{table} WHERE {wcolumns}={value}'
    else:
        qwery = f'SELECT {columns} FROM public.{table}'
    cursor.execute(qwery)
    data = cursor.fetchall()
    return data
def update(columns,wcolumns,value,wvalue):
    global cursor
    global table
    if len(wcolumns)>0:
        qwery = f'UPDATE public.{table} SET {columns} WHERE {wcolumns}={wvalue};'
    else:
        qwery = f"UPDATE public.{table} SET {columns}={value};'
    cursor.execute(qwery)
    con.commit()
    return 0
def insert(columns,values):
    global cursor
    global table


qwery="UPDATE public.logins SET password='138871263' WHERE id=2;"
cursor.execute(qwery)
con.commit()
data=cursor.fetchone()
print(data)