import os
import action
from past.builtins import raw_input


def admin_menu():
    ch = "Y"
    while ch == "Y":
        print("\n \t \t \t ADMINISTRATION MENU \t \t \t \n")
        print("\t 1. CREATE READER")
        print("\t 2. DISPLAY ALL READERS")
        print("\t 3. DISPLAY SPECIFIC READER")
        print("\t 4. MODIFY READER")
        print("\t 5. DELETE READER")
        print("\t 6. CREATE BOOK")
        print("\t 7. DISPLAY ALL BOOKS")
        print("\t 8. DISPLAY SPECIFIC BOOK")
        print("\t 9. MODIFY BOOK")
        print("\t 10.DELETE BOOK \n")
        ch1 = int(raw_input("\t \t Enter Your Choice:"))
        if ch1 == 1:
            action.write_reader()
        elif ch1 == 2:
            action.display_all_readers()
        elif ch1 == 3:
            os.system("clean")
            ad = raw_input("\n \t \t Enter Student's Admno to be Displayed:")
            action.display_sps(ad)
        elif ch1 == 4:
            action.modify_reader()
        elif ch1 == 5:
            action.del_reader()
        elif ch1 == 6:
            action.write_book()
        elif ch1 == 7:
            action.display_all_books()
        elif ch1 == 8:
            os.system("clean")
            bn = raw_input("\n \t \t ENTER BOOK NUMBER TO BE DISPLAYED:")
            action.display_reader_book_id(bn)
        elif ch1 == 9:
            action.modify_book()
        elif ch1 == 10:
            action.del_book()
        os.system("clean")
        ch = raw_input("\t \t Do you want Continue with ADMINMENU<y/n>:")
        ch = ch.upper()
        os.system("clean")
        if ch == "Y":
            continue
        else:
            main_menu()


def main_menu():
    ch = "Y"
    while ch == "Y":

        print("\n \n \t \t \t MAIN MENU \t \t \t")
        print("\t 1. BOOK ISSUE")
        print("\t 2. BOOK DEPOSIT")
        print("\t 3. ADMINISTRATION MENU")
        print("\t 4. EXIT\n \n")
        ch1 = int(raw_input("\t \t Enter Your Choice:"))
        os.system("clean")
        if ch1 == 1:
            action.book_issue()
        elif ch1 == 2:
            action.book_deposit()
        elif ch1 == 3:
            admin_menu()
        else:
            exit(0)

        ch = raw_input("\n \t \t \t Do You Want to Continue <y/n>:")
        ch = ch.upper()
        if ch == "N":
            break
        os.system("clean")
