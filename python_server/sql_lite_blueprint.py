from flask import Blueprint, render_template, request
import sqlite3
import random
import os

sql_lite_blueprint = Blueprint('sql_lite', __name__)

@sql_lite_blueprint.route('/sql_lite')
def sql_lite():
    conn = sqlite3.connect('Base_Sql_lite/principal.db')
    cursor = conn.cursor()
    table_name = 'disk_failures'  # Replace with the name of the table you want to check
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    result = cursor.fetchone()
    conn.close()
    data = None  # Initialize the data variable
    if result:
        # consulto datos
        data = retornar_datos()
    else:
        # creo la tabla y coloco datos aleatorios
        crear_aleatorio()
        data = retornar_datos()
    return render_template("sql_lite.html", data=data)

def crear_aleatorio():
    conn = sqlite3.connect('Base_Sql_lite/principal.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS disk_failures
                    (id INTEGER PRIMARY KEY, serial_number TEXT, failure_type TEXT, date TEXT)''')
    conn.commit()
    # Generate sample data
    serial_numbers = ['ABC123', 'DEF456', 'GHI789', 'JKL012', 'MNO345']
    failure_types = ['Read Error', 'Write Error', 'Bad Sectors', 'Disk Crash', 'Power Failure']

    # Insert formatted data into the table
    for i in range(1, 11):
        serial_number = random.choice(serial_numbers)
        failure_type = random.choice(failure_types)
        date = f'2022-01-{str(i).zfill(2)}'  # Generate sample dates for January 2022

        cursor.execute("INSERT INTO disk_failures (serial_number, failure_type, date) VALUES (?, ?, ?)",
                    (serial_number, failure_type, date))
    conn.commit()
    conn.close()

def retornar_datos():
    conn = sqlite3.connect('Base_Sql_lite/principal.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM disk_failures")
    result = cursor.fetchall()
    conn.close()
    return result