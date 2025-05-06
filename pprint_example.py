import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)

print ("\n\nAnother example:\n")

eggs = [
        {'name':'Sox', 'species': 'cat', 'age': '8'},
        {'name':'Chais', 'species': 'dog', 'age': '7'},
        {'name':'Woddy', 'species': 'bird', 'age': '6'}
        ]
pprint.pprint(eggs)
print("\n", eggs)

print ("\n\nAnother example:\n")
costumers = [
    {'name': 'Norik', 'age': '28', 'colors': ['black', 'blue', 'green']},
    {'name': 'Edel', 'age': '45', 'colors': ['black', 'blue', 'green']},
    {'name': 'Said', 'age': '14', 'colors': ['black', 'blue', 'green']},
    {'name': 'Demian', 'age': '10', 'colors': ['black', 'blue', 'green']}
    ]

pprint.pprint(costumers)

print("\n", costumers)
