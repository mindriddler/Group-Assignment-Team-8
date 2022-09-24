import db_init
import create_csv
import menu

# This will first create the csv file and initiate the db
# then go to main menu and start looping
if __name__ == '__main__':
    create_csv.create_csv()
    db_init.main()
    menu.menu_main()