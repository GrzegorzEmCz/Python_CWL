import models
import view
from past.builtins import raw_input
import os


print("\n \t \t \t WELCOME TO MAGIC LIBRARY \t \t \t \n \n")
print("\t \t \t \t \t \t \t PROJECT DONE BY:")
print("\t \t \t \t \t \t \t Grzegorz Czernecki \n \n")
a = raw_input("PRESS ENTER TO CONTINUE:")
a = str(a)
if a.isalpha():
    pass

book = models.Book()
student = models.Reader()

os.system('clear')
view.main_menu()
