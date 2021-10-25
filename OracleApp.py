from flask import Flask
import os
import cx_Oracle
import json

ORACLE_HOME = "/app/oracle/product/12.1.0"
ORACLE_LANG = "AMERICAN_AMERICA.AL32UTF8"

app = Flask(__name__)

@app.route('/test/', methods=['GET', 'POST'])
def test():
    cursor = getConnection().cursor()

    sql_file = open("../var/SqlScripts/test.sql")
    sql_as_string = sql_file.read()

    cursor.execute(sql_as_string)
    rv = cursor.fetchall()
    return(f"json: {json.dumps(rv, indent=4, sort_keys=True, default=str)}")


def getConnection():
    os.environ["ORACLE_HOME"] = ORACLE_HOME
    os.environ["PATH"] = ORACLE_HOME + os.pathsep + os.environ["PATH"]
    os.environ["NLS_LANG"]= ORACLE_LANG

    dsn = cx_Oracle.makedsn(host='xxx.xxx.xxx.xxx', port=xxxx, sid='xxxx')
    connection = cx_Oracle.connect(user='xxxx', password='xxxx', dsn=dsn)

    return connection

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=105)
