import db_init
import _classes
import create_csv

if __name__ == '__main__':
    create_csv.create_csv()
    db_init.main()
    _classes.clazz()
    
