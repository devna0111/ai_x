import cx_Oracle
import pandas as pd

conn = cx_Oracle.connect("scott",
                        "tiger",
                        "210.121.189.12:1521/xe") # localhost(127.0.0.1)

def get_emp_list():
    cursor = conn.cursor()
    sql = "SELECT * FROM EMP ORDER BY EMPNO"
    cursor.execute(sql)
    result = cursor.fetchall()
    keys = [desc[0] for desc in cursor.description]
    emp_list = [dict(zip(keys, row)) for row in result]
    return emp_list