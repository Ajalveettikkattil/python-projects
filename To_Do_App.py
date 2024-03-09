#To Do List

todo_list = []

def addList():
    item = input("Enter a new Task: ")
    todo_list.append(item)
    print(f"{item} added to the list")
    
def displayList():
    print("------------")
    print("To Do List")
    print("------------")
    for index, item in enumerate(todo_list,start=1):
        print(f"{index}-{item}")
        
def removeList():
    displayList()
    index = int(input("Enter your item number to remove:"))-1
    if 0<= index < len(todo_list):
        removed_item = todo_list.pop(index)
        print(f"{removed_item} removed from the list")
    else:
        print("Invaild Input")

while True:
    print("################")
    print("To Do List App")
    print("################")
    print("1 - Add To List")
    print("2 - Display List")
    print("3 - Remove From List")
    print("4 - Exit")

    option = input("Select your Option.")

    if option == '1':
        addList()
    elif option == '2':
        displayList()
    elif option == '3':
        removeList()
    elif option == '4':
        print("Exit")
        break
    else:
        print("Invalid Option")