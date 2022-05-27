
import re

regex = '^[a-zA-Z]+$'

def checkString (string) :
    if re.search(regex, string) :
        print("It is Character")
    else :
        print("It is not Character")


isCharecter = input("Enter  Character : ")
checkString(isCharecter)

# ================================
import re

regex = '[0-9]+'

def checkDigit (string) :
    if re.search(regex, string) :
        print("It is Digit")
    else :
        print("It is not Digit")


isCharecter = input("Enter  Character : ")
checkDigit(isCharecter)

# ====================================
import keyword

def check (string) :
    if keyword.iskeyword(string) :
        print("It is Keyword")
    else :
        print("It is not Keyword")

check("for")



