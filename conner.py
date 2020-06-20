
import pymysql

def get_conn():
    """
    :return: 连接，游标l
    """
    # 创建连接
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="12345678",
                           db="Dajango",
                           charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()