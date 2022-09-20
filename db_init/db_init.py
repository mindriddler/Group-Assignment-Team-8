import sqlite3
import json

EXAMPLE_DATASET = (
    (1, "Alice", "Smith"),
    (2, "Bob", "Smith"),
    (3, "Carol", "Brown"),
    (4, "Carlos", "Rojas"),
    (5, "Charlie", "Miller")
)

CREATE_TABLE = '''
                CREATE TABLE IF NOT EXISTS person(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    firstname TEXT,
                    lastname TEXT,
                    birthdate TEXT,
                    address TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                )
                '''

INSERT_DATA = '''
            INSERT INTO person(
                id,
                firstname,
                lastname,
                birthdate,
                address
            )
            VALUES (firstname, lastname, birthdate, address, ?)
            '''


def open_connection(filename):
    return sqlite3.connect(r"C:\Users\fredr\Desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignmentDevOps22\db\test.db", isolation_level=None)


def create_table(connection):
    try:
        connection.execute(CREATE_TABLE)
    except Exception:
        print('Failed to create table')
        raise


def insert_data(connection):
    try:
        with connection:
            connection.executemany(INSERT_DATA, EXAMPLE_DATASET)
    except sqlite3.IntegrityError:
        print("couldn't add Joe twice")
    except Exception:
        print("Failed to insert")
        raise

# def insert_data(conn):    
    # with open(r"c:\users\fredr\desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignmentDevOps22\data\persons.json") as conn:
        # data_to_database_executemany = []
        # persons = json.load(conn)
        # for person in persons['persons']:
            # data_to_database_executemany.append(tuple(person.values()))
