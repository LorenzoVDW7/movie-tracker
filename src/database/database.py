import psycopg2
import config

conn = psycopg2.connect(database="movies.db",
                        user=f"{config.DATABASE_USERNAME}",
                        password=f"{config.DATABASE_PASSWORD}",
                        host="localhost",
                        port="5432")