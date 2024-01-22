#Scarlett Arroyo and Tony Garcia
#1/11/24
#To-Do List

#Initialize        
myList = []
#Functions
def toDolist():
    while True:
        global myList
        print("1. Add task to list \n2. View list \n3. Complete a task \n4. Remove a task \n5. Remove all tasks \n6. Sort list alphabetically \n7. Check how many items on list\n8. Exit")
        option=int(input("Option:"))
        if option == 1:
            newtask = input("What would you like to add:")
            myList.insert(0, newtask)
            print (myList)
        if option == 2:
            print(myList)
        if option == 3:        
            print(myList)
            completed = input("What task is completed?")
            i = myList.index(completed)
            myList.insert(i,"X")
            myList.remove(completed)
            print(myList)
        if option == 4:
            remove = input("What task would you like to remove?")
            print(myList)
            i = myList.index(remove)
            myList.remove(remove)
            print(myList)
        if option == 5:
            myList.clear()
            print(myList)
        if option == 6:
            myList.sort()
            print(myList)
        if option == 7:
            print(len(myList))
        if option == 8:
            print("goodbye")
            break

#Main
toDolist()
