import os
import sqlite3

dir_path = os.path.dirname(os.path.realpath(__file__))

db_file = dir_path + "/system.db"

connection = sqlite3.connect(db_file)
connection.row_factory = sqlite3.Row

db = connection.cursor()


def check_db():
    return os.path.exists(db_file)


def insert_or_change_ip(ip_address):
    check = select_ip()
    if check is not None:
        db.execute("UPDATE remote_tv set ip_address='" + ip_address + "'")
    else:
        db.execute("INSERT INTO remote_tv (ip_address) VALUES ('" + ip_address + "')")
    connection.commit()


def select_ip():
    db.execute("SELECT ip_address FROM remote_tv limit 1")
    result = db.fetchone()
    if result is not None:
        result.keys()
        return result["ip_address"]
    else:
        return None
