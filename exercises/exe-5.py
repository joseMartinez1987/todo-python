# date = input("Enter a today's day: ")
# mood = input(f"How do you rate your mood taday from 1 to 10? ") + 2 * "\n"
# thought = input("Let yout thought flow: \n")
#
# with open(f'journal/{date}.txt', 'w') as file:
#     file.write(mood)
#     file.write(thought)

with open("journal/15-05-24.txt", 'r') as file:
    text = file.read()
    print(text)
    print(len(text.strip('\n')))


