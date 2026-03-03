import os
import logging
import pymysql
from urllib.request import urlopen

logging.basicConfig(level=logging.INFO)

db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "admin"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "testdb"),
}


def get_user_input():
    name = input("Enter your name: ").strip()
    return name


def get_data():
    url = "https://example.com"
    try:
        with urlopen(url, timeout=5) as response:
            return response.read().decode()
    except Exception as error:
        logging.warning("Error fetching data: %s", error)
        return ""


def save_to_db(data):
    query = "INSERT INTO mytable (column1) VALUES (%s)"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query, (data,))
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    logging.info("User input processed safely.")
