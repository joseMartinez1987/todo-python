from modules.functions import get_todos, write_todos
import FreeSimpleGUI as sg
import time

sg.theme('Black')


clock = sg.Text('', key='clock')
label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button('Add', tooltip="Add todo")

list_box = sg.Listbox(values=get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit', tooltip='Edit todo')

complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')



window = sg.Window('My To-Do App',
                   layout=[
                     [clock],
                     [label],
                     [input_box, add_button],
                     [list_box, edit_button, complete_button ],
                     [exit_button]
                     ])



while True:
  event, value = window.read(timeout=10)
  window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
  match event:
    case 'Add':
      todos  = get_todos()
      new_todo = value['todo'] + '\n'
      todos.append(new_todo)
      write_todos(todos)
      window['todos'].update(values=todos)
    case 'Edit':
      try:
        todo_to_edit = value['todos'][0]
        new_todo = value['todo'] + '\n'
        todos = get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        write_todos(todos)
        window['todos'].update(values=todos)
      except IndexError:
        sg.popup('Please select a todo to edit', font=('helvitica', 14))
      
    case 'todos':
      window['todo'].update(value['todos'][0])
    case 'Complete':
      try:
        todo_to_complete = value['todos'][0]
        todos = get_todos()
        print('todo_to_complete: ',todo_to_complete + '\n')
        print('todos: ',todos)
        todos.remove(todo_to_complete)
        write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value='')
      except IndexError:
        sg.popup('Please select a todo to complete', font=('helvitica', 14))
      
    case 'Exit':
      break
      
    case sg.WIN_CLOSED:
      break

window.close()


