from tortoise import Tortoise
import psycopg2


async def init_db():
    await Tortoise.init(
        db_url='postgres://user:password@localhost:5432/database',
        modules={'models': ['models']}
    )


def connect_db():
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="123",
        host="127.0.0.1"
    )
    return conn


def db_do(sql_comm):
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="123",
        host="127.0.0.1"
    )
    cursor = conn.cursor()
    cursor.execute(sql_comm)
    res = cursor.fetchall()
    conn.commit()
    conn.close()
    return res


def close_db(conn):
    conn.cursor.close()
    conn.close()


def create_db():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        create_table_query = '''
            CREATE TABLE Data (
                id SERIAL PRIMARY KEY,
                date VARCHAR(15),
                cargo_type VARCHAR(255),
                rate real
            )
            '''
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
    except psycopg2.errors.DuplicateTable:
        print("You have an active bd Data")
    conn.close()