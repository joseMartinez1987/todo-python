from modules.functions import get_todos,write_todos
import time 

print(time.strftime('%Y-%m-%d %H:%M:%S'))
while True:
    user_action = input('Type add, edit, show, complete or exit: ')
    user_action = user_action.strip()
    if user_action.startswith('add'): 
        todo = user_action[4:] + '\n'
        todos = get_todos()
        if todos == False:
            continue
        todos.append(todo)
        write_todos(todos)
    elif user_action.startswith('show'):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # form 1 to modify the todos string (for loop)
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        #Form 2 to modify to todos string (list comprehension) shorter way!!
        new_todos = [item.strip('\n') for item in todos]
        
        for index,item in enumerate(new_todos) :
            print(f'{index} - {item}')

    elif user_action.startswith('edit'):
        try:
            todos = get_todos()
            for index, todo in enumerate(todos):
                print(f"{index} - {todo.strip('\n')} ")
            edit_index = input('Enter the number of the todo to edit: ')
            todo_modified = input(f'enter a todo to modify {todos[int(edit_index)]}: ')
            todos[int(edit_index)] = todo_modified + '\n'
            write_todos(todos)
            # todos[int(edit_index)] = todo_modified
        except ValueError:
            print('please enter a valid number')
            continue

    elif user_action.startswith('complete'):
        todos = get_todos()
        for index, todo in enumerate(todos):
            print(f'{index} - {todo.strip('\n')}')
        todo_complete_index = int(input('Enter the todo number to be completed'))
        todos.pop(todo_complete_index)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith('exit'):
        break
        
    else:
        print('it is not a valid command')

print('bye')
