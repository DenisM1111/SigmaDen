import psycopg2
con=psycopg2.connect(dbname='test', user='postgres', password='Q1w2e3r4', host='localhost')
cursor=con.cursor()
#qwery='SELECT login, password, id FROM public."logins"'
qwery="UPDATE public.logins SET password='138871263' WHERE id=2;"
cursor.execute(qwery)
con.commit()
data=cursor.fetchall()
print(data)