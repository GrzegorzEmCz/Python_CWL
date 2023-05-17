import os
from os import remove, rename
from pickle import load, dump

from past.builtins import raw_input

import models

book = models.Book()
student = models.Reader()


def write_book():
    ch = "Y"
    fp = open("book.dat", "ab")
    while ch == "Y":
        book.add()
        dump(book, fp)
        ch = raw_input("\n \t \t Do You Want to Continue<y/n>:\n")
        print("#" * 70)
        ch = ch.upper()


def write_reader():
    ch = "Y"
    fp = open("reader.dat", "ab")
    while ch == "Y":
        student.create()
        dump(student, fp)
        ch = raw_input("\n \t \t Do You Want to Continue <y/n>:\n")
        print("#" * 70)
        ch = ch.upper()


def display_all_readers():
    fin = open("reader.dat", "rb")
    if not (fin):
        print("\t \t File is Not Found..\n")
    else:
        try:
            while True:
                st = load(fin)
                st.show()
        except EOFError:
            pass
        fin.close()


def display_all_books():
    fin = open("book.dat", "rb")
    if not fin:
        print("\n Book File is Not Found..")
    else:
        try:
            while True:
                bk = load(fin)
                bk.show()
        except EOFError:
            pass
        fin.close()


def display_reader_book_id(no):
    flag = 0
    fin = open("book.dat", "rb")
    try:
        while True:
            bk = load(fin)
            if bk.get_book_id() == no:
                bk.show()
                flag = 1

    except EOFError:
        pass
    fin.close()
    if flag == 0:
        print("\n \t \t \t \t BOOK NOT PRESENT..!!")


def display_sps(n):
    flag = 0
    fin = open("reader.dat", "rb")
    try:
        while True:
            st = load(fin)
            if st.get_id() == n:
                st.show()
                flag = 1
    except EOFError:
        pass
    fin.close()
    if flag == 0:
        print("\n \t \t \t STUDENT NOT PRESENT..!!")


def modify_book():
    found = 0
    print("\n \t \t \t Modify Book \n")
    n = raw_input("\t \t Enter Book Number to be Modified:")
    fin = open("book.dat", "rb")
    fout = open("temp.dat", "wb")
    try:
        while True:
            bk = load(fin)
            if bk.get_book_id() == n:
                print("\n \t \t \t Book Details")
                bk.show()
                print("\n \t \t  Enter New Details")
                bk.modify()
                dump(bk, fout)
                found = 1
            else:
                dump(bk, fout)
    except EOFError:
        pass
    if found == 0:
        print("\t \t \t \t Book Not Present")
    fin.close()
    fout.close()
    remove("book.dat")
    rename("temp.dat", "book.dat")


def modify_reader():
    found = 0
    print("\n \t \t \t Modify Reader \n")
    n = raw_input("\t \t Enter Reader's ID to be Modified:")
    fin = open("reader.dat", "rb")
    fout = open("temp.dat", "wb")
    try:
        while True:
            st = load(fin)
            if st.get_id() == n:
                print("\n \t \t \t READER DETAILS")
                st.show()
                print("\n \t \t \t Enter New Reader Details:")
                st.modify()
                dump(st, fout)
                found = 1
            else:
                dump(st, fout)
    except EOFError:
        pass
    if found == 0:
        print("\n \t \t \t \t READER NOT PRESENT")
    fin.close()
    fout.close()
    remove("reader.dat")
    rename("temp.dat", "reader.dat")


def del_reader():
    flag = 0
    n = raw_input("\n \t \t Enter Reader ID to be Deleted:")
    fin = open("reader.dat", "rb")
    fout = open("temp.dat", "wb")
    try:
        while True:
            st = load(fin)
            if st.get_id() != n:
                dump(st, fout)
            else:
                flag = 1
    except EOFError:
        pass
    fin.close()
    fout.close()
    remove("reader.dat")
    rename("temp.dat", "reader.dat")
    if flag == 1:
        print("\n \t \t \t \t RECORD DELETED..!!")
    else:
        print("\n \t \t \t \t SORRY..!! RECORD DOES NOT EXIST..!!..")


def del_book():
    flag = 0
    n = raw_input("\n \t \t Enter Book ID to be Deleted:")
    fin = open("book.dat", "rb")
    fout = open("temp.dat", "wb")
    try:
        while True:
            bk = load(fin)
            if bk.get_book_id() != n:
                dump(bk, fout)
            else:
                flag = 1
    except EOFError:
        pass
    fin.close()
    fout.close()
    remove("book.dat")
    rename("temp.dat", "book.dat")
    if flag == 1:
        print("\n \t \t \t \t RECORD DELETED..!!")
    else:
        print("\n \t \t \t \t SORRY..!! RECORD DOES NOT EXIST..!!..")


def book_issue():
    found = 0
    flag = 0
    print("\n \t \t \t BOOK ISSUE.. \t \t \t \n")
    sn = raw_input("\t \t Enter the Reader's ID: \n")
    fin1 = open("book.dat", "rb")
    fin2 = open("reader.dat", "rb")
    fout = open("temp.dat", "wb")
    try:
        while True:
            st = load(fin2)
            if st.get_id() == sn:
                st.show()
                found = 1
                if st.get_token() == 0:
                    bn = raw_input("\t \t Enter Book Id:")
                    try:
                        while True:
                            bk = load(fin1)
                            if bk.get_book_id() == bn:
                                bk.show()
                                flag = 1
                                st.set_token()
                                st.set_book_id(bk.get_book_id())
                                dump(st, fout)
                                os.system("clean")
                                print("\n \t \t \t Book Issued Successfully \t \t \t")
                                print("\t PLEASE NOTE : Write the current date in backside of your book ")
                                print("\t \t and submit within 15 days \n")
                                print("\t \t Fine Rs.20 for each day after 15 days period..!! \n")
                    except EOFError:
                        pass
                else:
                    print("\t You have not returned the last book..")

    except EOFError:
        pass
    if flag == 0:
        print("\t \t \t No Such Book Present !!!")
    if found == 0:
        print("\t \t \t No Such Reader Exists !!!")
    fin1.close()
    fin2.close()
    fout.close()
    remove("reader.dat")
    rename("temp.dat", "reader.dat")


def book_deposit():
    print("\n \n \t \t \t BOOK DEPOSITING.")
    sn = " "
    found = 0
    flag = 0
    day = 0
    fine = 0
    sn = raw_input("\n \t \t Enter Readers ID:")
    print()
    fin1 = open("reader.dat", "rb")
    fin2 = open("book.dat", "rb")
    fout = open("temp.dat", "wb")
    try:
        while True:
            st = load(fin1)
            if st.get_id() == sn:
                found = 1
                print()
                print("\t Reader Token Number", st.get_token())
                if st.get_token() == 1:
                    try:
                        while True:
                            bk = load(fin2)
                            if bk.get_book_id() == st.get_book_id():
                                bk.show()
                                flag = 1
                                print()
                                days = int(raw_input("\t Book Deposited In no. of days:"))
                                if days >= 15:
                                    fine = (days - 15) * 20
                                    print("\n \t Fine : Rs.", fine)
                                st.reset_token()
                                st.set_book_id(0)
                                st.show()
                                dump(st, fout)
                                print("\n \t \t BOOK DEPOSITED !!!")
                    except EOFError:
                        pass
                else:
                    print("\n \t \t You have not issued the  book..")
    except EOFError:
        pass
    if found == 0:
        print("\n \t No Such Student Exists")
    fin1.close()
    fin2.close()
    fout.close()
    remove("reader.dat")
    rename("temp.dat", "reader.dat")
