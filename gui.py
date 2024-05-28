from modules.functions import get_todos, write_todos
import FreeSimpleGUI as sg


label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button('Add', tooltip="Add todo")

list_box = sg.Listbox(values=get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit', tooltip='Edit todo')

complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')


window = sg.Window('My To-Do App',
                   layout=[
                     [label], [input_box, add_button],
                     [list_box, edit_button, complete_button ],
                     [exit_button]
                     ])



while True:
  event, value = window.read()
  print('event: ',event)
  print('value: ',value)

  match event:
    case 'Add':
      todos  = get_todos()
      new_todo = value['todo'] + '\n'
      todos.append(new_todo)
      write_todos(todos)
      window['todos'].update(values=todos)
    case 'Edit':
      todo_to_edit = value['todos'][0]
      new_todo = value['todo'] + '\n'
      todos = get_todos()
      index = todos.index(todo_to_edit)
      todos[index] = new_todo
      write_todos(todos)
      window['todos'].update(values=todos)
      
    case 'todos':
      window['todo'].update(value['todos'][0])
    case 'Complete':
      todo_to_complete = value['todos'][0]
      todos = get_todos()
      print('todo_to_complete: ',todo_to_complete + '\n')
      print('todos: ',todos)
      todos.remove(todo_to_complete)
      write_todos(todos)
      window['todos'].update(values=todos)
      window['todo'].update(value='')
      
    case 'Exit':
      break
      
    case sg.WIN_CLOSED:
      break

window.close()


