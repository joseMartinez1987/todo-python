import glob

my_files = glob.glob('../*.txt')

for filepath in my_files:
  with open(filepath, 'r') as file:
    content = file.read()
    print(content)

