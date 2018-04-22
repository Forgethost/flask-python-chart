import pyodbc
from datetime import datetime, timedelta
import pytz



def conn_db():
    server = '<uourazureSQL DB>.database.windows.net'
    database = '<yourdbname>'
    username = '<yourdbusername>'
    password = '<yourdbpassword>'
    driver = '{ODBC Driver 17 for SQL Server}'
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    return conn, cursor

def close_db(cursor):
    cursor.close()


def get_current_date():
    utc = pytz.timezone("UTC")
    curr_date = utc.localize(datetime.today())
    return curr_date
