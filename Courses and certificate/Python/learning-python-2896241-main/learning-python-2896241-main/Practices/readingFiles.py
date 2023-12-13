def readingFile(a):
    """ the argument takes a path file as an input"""
    with open(a, "r") as text:
        content = text.read()
        print(content)

def writingFile(a):
    newLine = str(input("Please enter what you would like to write:- "))
    with open(a, "a") as text:
        text.write(str(f"{newLine} \n"))
        print("File updated")
    userInput = str(input("Would you like to read the file? Enter Y for Yes and N for No:- ")).upper()
    try:
        if userInput == "Y":
            reading = readingFile(a)
        elif userInput == "N":
            print("Goodbye")
    except ValueError:
            print("Please enter Y or N")
    except:
            print("Something went wrong")

def overwriting(a):
    with open(a, "w") as text:
        newLine = str(input("Please enter the new text to overwrite the text file:- "))
        text.write(str(f"{newLine} \n")) 
        print("File updated")
    userInput = str(input("Would you like to read the file? Enter Y for Yes and N for No:- ")).upper()
    try:
        if userInput == "Y":
            reading = readingFile(textFile)
        else:
            print("Goodbye")
    except ValueError:
            print("Please enter Y or N")
def copingFile(a):
    try:
        userInput = str(input("Please enter the name of the new file with an extension of txt at the end: "))
    except ValueError:
          print("Please enter a proper name")
    except:
          print("Something went wrong")

    with open(a, "r") as readFile:
        with open(userInput, "w") as writeFile:
            for line in readFile:
                writeFile.write(line)
    print("New file was created succesfully")
    userResponse = str(input("Would you like to read the new file ? Enter Y for Yes and N for No:- ")).upper()
    try:
        if userResponse == "Y":
            readingFile(userInput)
        elif userInput == "N":
            print("Thank you")
    except ValueError:
            print("Please enter Y or N")
    except:
            print("Something went wrong")                

        
textFile = "Example1.txt"
run = True
while run:
    print("Welcome to my reading and writing file algorithm")
    print("--------------------------------------------------")
    print("1. Read\n2. Write\n3. Copy\n4. Exit\n")
    print("Please select options above: ")
    userInput = str(input("Enter Read, Write, Copy or Exit: ")).lower()
    try:
        if(userInput == "read"):
            readingFile(textFile)
        elif (userInput == "write"):
             writingFile(textFile)
        elif(userInput == "copy"):
             copingFile(textFile)
        elif (userInput == "exit"):
            run = False
            break
    except ValueError:
         print("Please enter Read, Write and Exit")
    except:
         print("Something went wrong")
        
             



#overwriting(textFile)