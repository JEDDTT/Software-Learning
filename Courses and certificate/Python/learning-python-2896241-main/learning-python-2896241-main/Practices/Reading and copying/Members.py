from random import randint as rnd
import os 
#memReg = "/members.txt" #if there is an error use the full path by replacing \ by /
#exReg = "/inactive.txt"
memReg = 'C:/Users/HP/Desktop/Software-Learning/Courses and certificate/Python/learning-python-2896241-main/learning-python-2896241-main/Practices/Reading and copying/members.txt'
exReg = 'C:/Users/HP/Desktop/Software-Learning/Courses and certificate/Python/learning-python-2896241-main/learning-python-2896241-main/Practices/Reading and copying/inactive.txt'
fee = ("yes", "no")

def genFiles(current, old):
    with open(current, 'w+') as writefile:
        writefile.seek(0)
        writefile.write('Membership No  Date Joined Active  \n')
        data = "{:^13}  {:<11} {:<6}\n" #curly brackets are used to specify the format check python string formatting on w3schools

        for rowno in range(20):
            date = str(rnd(2015,2020))+ "-" + str(rnd(1,12))+'-'+str(rnd(1,28))
            writefile.write(data.format(rnd(10000,99999), date, fee[rnd(0,1)]))
    with open(old, 'w+') as writefile:
        writefile.seek(0)
        writefile.write('Membership No  Date Joined Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+ '-'+str(rnd(1,28))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))
    print("Files have been generated successfully")

#genFiles(memReg, exReg)

def cleanfiles(currentMember, inactiveMember):
    with open(currentMember, 'r+') as membersFile:
        with open(inactiveMember, 'a+') as inactiveFile:
            membersFile.seek(0)
            membersList = membersFile.readlines() #Saves everything within the list to avoid messing up the file
            header = membersList[0] #Saves the header from the list to interact with rows only 
            membersList.pop(0) #removes header from the list
            inactiveList = [member for member in membersList if ('no' in member)]
           #code below does the same thing aswell 
           #for member in membersList:
               #if 'no' in member:
                   #inactiveList.append(member) #If a member is not active in the member list then that member is added to inactive list
            #Placing the cursor at the begenning of the membersFile(CurrentMember)       
            membersFile.seek(0)
            membersFile.write(header) #We start to write from the beginning which will overwrite the data in the file (might overwrite everything in the file, I need to test this hipothesie).
        
        #for inactMember in inactiveList:
            #inactiveFile.write(inactMember)
            
            for member in membersList: #The list contain all the members taken from currentMembers file. 
                if member in inactiveList:
                    inactiveFile.write(member) #We add inactive members that exist within the inactiveList to the inactive file.
                else:
                    membersFile.write(member) #Or else if the member does not exist in the inactive then it should be written to the current member file.
                #so bacilly by placing the cursor in the beginning of file, any data that is being written from the beginning of file, will overwrite all data in that file.
            membersFile.truncate() # Reduces the file to present data and delete everything that follows.
            
           

cleanfiles(memReg, exReg)
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())