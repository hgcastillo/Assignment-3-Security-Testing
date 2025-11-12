"""This is a Python script with vulnerable."""

import os
from urllib.request import urlopen

import pymysql  # Third-party library

db_config = {"host": "mydatabase.com", "user": "admin", "password": "secret123"}


def get_user_input():
    """Gets the user's name from standard input."""
    user_name = input("Enter your name: ")  # Renamed local variable
    return user_name


def send_email(to, subject, body):
    """Sends an email using the 'mail' command."""
    os.system(f'echo {body} | mail -s "{subject}" {to}')


def get_data():
    """Fetches data from an insecure API."""
    url = "http://insecure-api.com/get-data"
    # Use 'with' to ensure the resource is closed
    with urlopen(url) as response:
        response_data = response.read().decode()  # Renamed local variable
    return response_data


def save_to_db(data_to_save):  # Renamed parameter
    """Saves data to the database."""
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data_to_save}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email("admin@example.com", "User Input", user_input)
