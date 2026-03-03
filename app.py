import os
import pymysql


def get_user_input():
    return input("Enter your name: ").strip()


def save_to_database(name):
    query = "INSERT INTO users (name) VALUES (%s)"

    connection = pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "testdb"),
    )

    cursor = connection.cursor()
    cursor.execute(query, (name,))
    connection.commit()
    cursor.close()
    connection.close()


def main():
    name = get_user_input()
    if name:
        save_to_database(name)
        print("User saved successfully.")
    else:
        print("No name entered.")


if __name__ == "__main__":
    main()
