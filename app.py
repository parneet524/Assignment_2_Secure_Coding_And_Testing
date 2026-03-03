import os
import logging
import pymysql
from urllib.request import urlopen
from urllib.error import URLError

logging.basicConfig(level=logging.INFO)

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "admin"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "testdb"),
}


def get_user_input():
    name = input("Enter your name: ").strip()
    if not name:
        logging.warning("Empty input received.")
    return name


def fetch_remote_data():
    url = "https://example.com"
    try:
        with urlopen(url, timeout=5) as response:
            data = response.read().decode()
            logging.info("Data fetched successfully.")
            return data
    except URLError as error:
        logging.error("Failed to fetch data: %s", error)
        return ""


def save_to_database(data):
    query = "INSERT INTO mytable (column1) VALUES (%s)"
    try:
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute(query, (data,))
        connection.commit()
        logging.info("Data saved to database.")
    except pymysql.MySQLError as error:
        logging.error("Database error: %s", error)
    finally:
        cursor.close()
        connection.close()


def process_application():
    user_input = get_user_input()
    remote_data = fetch_remote_data()
    save_to_database(remote_data)
    logging.info("Application completed for user: %s", user_input)


if __name__ == "__main__":
    process_application()
