import os
import pickle
import sys
item=[]
def write_in_file():
    f=open("Wildlife_sanctuary.dat","ab")
    Area_no=int(input("Enter Area no.: "))
    animal_name=input("Enter Animal name: ")
    cost=input("Enter the cost: ")
    item.append([Area_no,animal_name, cost])
    pickle.dump(item,f)
    f.close()
    item.clear()
def display():
    f=open("Wildlife_sanctuary.dat","rb")
    try:
        while True:
            item1=pickle.load(f)
            print(item1)
    except EOFError:
        pass
    f.close()
def search():
    f=open("Wildlife_sanctuary.dat","rb")
    i=input("Enter Area no. to search: ")
    found=0
    try:
        while True:
            item1=pickle.load(f)
            print(item1)
            if item1[0][1]==i:
                found=1
                print(item1)
                break
            if found==0:
                print("Item not found")
    except EOFError:
        pass
    f.close()
def update():
    F1=open("Wildlife_sanctuary.dat","rb")
    F2=open("temp.dat","ab")
    r=int(input("Enter the Area no. to update: "))
    try:
        while True:
            data=pickle.load(F1)
            if data[0][0]==r:
                print("Enter new item details")
                data[0][0]=int(input("Enter Area no.: "))
                data[0][1]=input("Enter animal name: ")
                data[0][2]=input("Cost: ")
                pickle.dump(data,F2)
            else:
                pickle.dump(data,F2)
    except EOFError:
        pass
    F1.close()
    F2.close()
    os.remove("Wildlife_sanctuary.dat")
    os.rename("temp.dat","Wildlife_sanctuary.dat")
    file=open("Wildlife_sanctuary.dat","rb")
    try:
        while True:
                stud=pickle.load(file)
                print(stud)
    except EOFError:
             pass
    file.close()
def delete():
    f1=open("Wildlife_sanctuary.dat","rb")
    f2=open("temp.dat","ab")
    r=int(input("Enter the area no. to delete: "))
    try:
        while True:
            data=pickle.load(f1)
            if data[0][0]==r:
                pass
            else:
                pickle.dump(data,f2)
    except EOFError:
        pass
    f1.close()
    f2.close()
    os.remove("Wildlife_sanctuary.dat")
    os.rename("temp.dat","Wildlife_sanctuary.dat")
    file=open("Wildlife_sanctuary.dat","rb")
    print("RECORD AFTER,DELETION")
    try:
        while True:
            stud=pickle.load(file)
            print(stud)
    except EOFError:
        pass
        file.close()

while True:
    print("MENU\n 1:Write in file \n 2:Display \n 3:Search \n 5:Delete \n 6:Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
            write_in_file()
    if ch==2:
            display()
    if ch==3:
            search()
    if ch==4:
            update()
    if ch==5:
            delete()
    if ch==6:
            print("Thank You!")
            sys.exit()