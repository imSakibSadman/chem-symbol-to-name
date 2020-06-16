import csv
import os
import sys

database = {} # Reading database
with open(os.path.abspath(os.path.dirname(sys.argv[0])) + '/database.csv', 'r') as database_file:
    readerx = csv.reader(database_file)
    for row in readerx:
        database[row[0]] = row[1]

database_file.close()

exeptions = [] # Reading exeptions
with open(os.path.abspath(os.path.dirname(sys.argv[0])) + '/exeptions.csv', 'r') as exeptions_file:
    readery = csv.reader(exeptions_file)
    l = list(readery)
    for sublist in l:
        for item in sublist:
            exeptions.append(item)

exeptions_file.close()

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
inv_SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")

def converter():
    prompt = input("Enter a symbol or a name OR ENTER q TO QUIT: ").translate(inv_SUB)
    alt_prompt = prompt.lower()

    for expetion in exeptions: # Checks if it is a name or symbol. If it is a name, makes it capital.
        if alt_prompt in exeptions:
            prompt = alt_prompt.capitalize()

    for symbol in database: # Checks if the input is in the database or not. If it is not, prints it.
        if prompt in database or prompt == "q":
            break
        else:
            print("Not found in our database!")
            return True

    if prompt == "q": # Checks if the input is 'q'. If it is, quits the program.
        print("Thank You!")
        return False
 
    result = database[prompt].translate(SUB)
    print(result)


while converter() is not False:
        converter()