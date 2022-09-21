import db_insert
import _classes
import create_csv

if __name__ == '__main__':
    create_csv.create_csv()
    db_insert.main()
    _classes.clazz()