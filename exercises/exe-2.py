name = input('enter a name')

file = open('files/members.txt', 'r')
read_file = file.readlines()
file.close()

read_file.append(name + '\n')

store_file = open('files/members.txt', 'w')
store_file.writelines(read_file)
store_file.close()
