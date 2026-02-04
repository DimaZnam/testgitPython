# user_prompt = "Type add or Show: "
""" """
todos = ["first" , "second", "third"]

while True:

    user_action = input("Type add,show, edit, def, exit: ")
    user_action = user_action.strip()

    match user_action:

        case "add":
            todo  = input("Enter a todo: ")
            todos.append(todo.capitalize())

        case  'show' | 'display':
            #print (todos)
            for index, item in enumerate(todos):
                item = item.capitalize()
                print(index,".", item)

        case 'edit':
            #print ("Got it!")
            number = int (input("Enter a number of the todo to edit: "))
            number = number-1
            buffer = todos [number]
            new_todo = input ("Enter New todo: ")
            todos [number] = new_todo

            print ("Old value: ",buffer, " New value: ", todos [number])
        case "def":
            todos = ["first", "second", "third"]
        case 'exit':
            break

        case _:
            print("Hey, you entered an unknow command")
print ("----!!!!!____Done----!!!!!____")












