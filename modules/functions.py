def get_todos():
    try:
        with open('todos.txt', 'r') as read_file:
            todos = read_file.readlines()
            return todos
    except Exception as e:
        print('An error occurred')
        print(e)
        return False
    
    
def write_todos(todos):
    with open('todos.txt', 'w') as write_file:
        write_file.writelines(todos)
    print('todos saved')
print(__name__)
if __name__ == '__main__':
    print('Hello')
    print('This is called from functions.py')