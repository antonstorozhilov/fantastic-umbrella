from spotify_connection import SpotifyConnection
import os
import psycopg2
import time


spotify = SpotifyConnection()

def connect_to_db():
    DATABASE_URL = os.getenv('DATABASE_URL')
    while True:
        try:
            conn = psycopg2.connect(DATABASE_URL)
            print("Connected to the database!")
            return conn
        except psycopg2.OperationalError:
            print("Database not ready, retrying in 5 seconds...")
            time.sleep(5)

if __name__ == '__main__':
    conn = connect_to_db()
    cursor = conn.cursor()

    while True:
        print(spotify.get_artist_data('4Z8W4fKeB5YxbusRsdQVPb'))
        time.sleep(5)

        cursor.execute("SELECT 1")
        print(cursor.fetchone())

    conn.close()