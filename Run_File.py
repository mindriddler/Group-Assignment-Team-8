import db_init
import create_csv
import menu

# This will first create the csv file and initiate the db
# then go to main menu and start looping
if __name__ == '__main__':
    create_csv.create_csv()
    # M: It's a good principle to create a DB init here. What would be even better is if it
    # returned a reference to the db connection, and then you could pass it into menu.
    # In this way, you would always re-use the connection when the code is running in main
    # instead of having to create new connections sometimes.
    db_init.main()
    menu.menu_main()