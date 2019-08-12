 # -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import log


def connection_querry():
  try:
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'trk_db'
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("Select users.name, sensors.type, sensors.idrasp, status.status1, status.status2, status.status3, status.time  "
                   "from users left join sensors on sensors.id_user = users.id "
                   "left join status on status.id_sensors = sensors.id")
    data = cursor.fetchall()
    return data
    #print(cursor.fetchall())
  except Exception as error:
    log.eventadd(str(error))
    return "API has a problem, contact your system administrator", 500



app = Flask(__name__)
CORS(app)

@app.route('/')
def json():
  return jsonify(connection_querry())

if __name__=='__main__':
  app.run(debug=True)