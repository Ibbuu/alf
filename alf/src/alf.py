from flask import Flask, render_template
from mysql.connector import Error
from mysql.connector import pooling
import os


connection_pool = pooling.MySQLConnectionPool(pool_name="local_pool",
                                                  pool_size=5,
                                                  pool_reset_session=True,
                                                  host=os.getenv('DB_HOST'),
                                                  database=os.getenv('DB_DATABASE'),
                                                  user=os.getenv('DB_USER'),
                                                  password=os.getenv('DB_PASSWORD'))

def get_details():
    connection_object = connection_pool.get_connection()
    if connection_object.is_connected():
        cursor = connection_object.cursor()
        cursor.execute("select * from alf.test_table;")
        record = cursor.fetchall()
        cursor.close()
        connection_object.close()
        return record


app = Flask(__name__)
@app.route('/')
def home():
    fetchdata=get_details()
    return render_template('home.html',data=fetchdata)

@app.route('/healthz')
def healthz():
    connection_object = connection_pool.get_connection()
    if connection_object.is_connected():
        cursor = connection_object.cursor(buffered=True)
        cursor.execute("select 1")
        cursor.close()
        connection_object.close()
    return ''

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)