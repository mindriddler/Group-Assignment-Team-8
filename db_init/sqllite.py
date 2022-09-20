from db_init import open_connection, create_table, insert_data


def select_firstname_equals(connection, name):
    return tuple(connection.execute(
        '''
        SELECT
            firstname,
            lastname,
            birtdate,
            address,
            timestamp
        FROM person
        WHERE
            firstname = ?
        ''', [name]
    ))


def select_firstname_like(connection, name):
    return tuple(connection.execute(
        '''
        SELECT
            firstname,
            lastname,
            birthdate,
            address,
            timestamp
        FROM person
        WHERE
            firstname LIKE ?
        ''', [name]
    ))

# def insert_db():
    # with open(r"c:\users\fredr\desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignmentDevOps22\data\persons.json") as f:
        # data_to_database_executemany = []
        # persons = json.load(f)
        # for person in persons['persons']:
            # data_to_database_executemany.append(tuple(person.values()))


def main():
    with open_connection(r"c:\users\fredr\desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignment\db\test.db") as conn:
        create_table(conn)
        insert_data(conn)
        print(select_firstname_like(conn, "C%"))
    conn.close()


if __name__ == "__main__":
    main()
