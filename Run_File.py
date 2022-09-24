import db_init
import create_csv
import menu

# This will first create the csv file then it initiates the database
# when it's comeplete the _classes.clazz() will be gone and replaces with the menu
# because we're only running the _classes file when we call for it inside of the menu

if __name__ == '__main__':
    create_csv.create_csv()
    db_init.main()
    menu.menu_main()