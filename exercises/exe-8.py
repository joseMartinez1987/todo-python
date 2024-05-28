import csv

with open('weather.csv', 'r') as file:
  data = list(csv.reader(file))
  print(data)

city = input('Enter the city: ')

for row in data:
  if row[0] == city:
    print(row[1])
    break