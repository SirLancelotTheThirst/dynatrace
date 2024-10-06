import psutil
import sys
import time
from datetime import datetime
import pyodbc
import os

def monitor_ram(connection):
    # Get the total, available, and used memory
    memory_info = psutil.virtual_memory()

    total_memory = memory_info.total  # Total RAM
    available_memory = memory_info.available  # Available RAM
    used_memory = memory_info.used  # Used RAM
    memory_percentage = memory_info.percent  # Percentage of RAM used

    print(f"Total Memory: {total_memory / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {used_memory / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {available_memory / (1024 ** 3):.2f} GB")
    print(f"Memory Usage Percentage: {memory_percentage:.2f}%")

    data = (datetime.now(), total_memory/ (1024 ** 3), available_memory/ (1024 ** 3), used_memory/ (1024 ** 3), memory_percentage)
    save_to_database(connection, data)

def connect():
    # Create the connection string
    connection_string = os.getenv('dynatrace_dsn')

    # Establish the connection
    return pyodbc.connect(connection_string)

def save_to_database(connection, data):
    cursor = connection.cursor()

    # SQL Query to insert data
    sql_insert_query = """
    INSERT INTO ram_monitoring (created_at, total_memory, available_memory, used_memory, memory_percentage)
    VALUES (?, ?, ?, ?, ?)
    """

    # Execute the query
    cursor.execute(sql_insert_query, data)

    # Commit the transaction to save the data
    connection.commit()

    # Close the connection
    cursor.close()

conn = connect()

try:
    while True:
    
        monitor_ram(conn)
        sys.stdout.write("\033[4A")
        sys.stdout.flush()
        time.sleep(5)
except KeyboardInterrupt:
        monitor_ram(conn)
        print("Stopped ")






