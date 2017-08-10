import psycopg2


def get_connection(**kwargs):
    dbname = kwargs.get('dbname', 'michaelsoileau')
    user = kwargs.get('name', 'michaelsoileau')
    password = kwargs.get('password', 'start')
    # conn = psycopg2.connect(
    #     "dbname=" + dbname + " user=" + user + " password=" + password)
    conn = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
    cur = conn.cursor()
    return cur
