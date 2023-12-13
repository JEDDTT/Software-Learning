from random import randint as rnd
import os 
#memReg = "/members.txt" #if there is an error use the full path by replacing \ by /
#exReg = "/inactive.txt"
memReg = 'C:/Users/HP/Desktop/Software-Learning/Courses and certificate/Python/learning-python-2896241-main/learning-python-2896241-main/Practices/Reading and copying/members.txt'
exReg = 'C:/Users/HP/Desktop/Software-Learning/Courses and certificate/Python/learning-python-2896241-main/learning-python-2896241-main/Practices/Reading and copying/inactive.txt'
fee = ("yes", "no")

def genFiles(current, old):
    with open(current, 'w+') as writefile:
        writefile.write('Membership No  Date Joined Active  \n')
        data = "{:^13}  {:<11} {:<6}\n" #curly brackets are used to specify the format check python string formatting on w3schools

        for rowno in range(20):
            date = str(rnd(2015,2020))+ "-" + str(rnd(1,12))+'-'+str(rnd(1,28))
            writefile.write(data.format(rnd(10000,99999), date, fee[rnd(0,1)]))
    with open(old, 'w+') as writefile:
        writefile.write('Membership No  Date Joined Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+ '-'+str(rnd(1,28))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))
    print("files have been generated successfully")

genFiles(memReg, exReg)