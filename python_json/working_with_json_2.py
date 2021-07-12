''' JavaScript Object Notation '''
import json

# with open('states.json' , 'r') as f:
#     data = json.load(f) # json.load method loads a file into a python object

# for state in data['states']:
#     print(state['name'] , state['abbreviation'])

# for state in data['states']:
#     del state['area_codes']
#
# #Write the data to a file as a json
# with open('new_states.json' , 'w') as f:
#     json.dump(data , f , indent=2)


with open('questions1.json' , 'r') as f:
    data = json.load(f)

# print(json.dumps(data , indent=2))
# print(len(data['games'][0]['questions'])) 15
# for q in data['games'][0]['questions']:
#     print(q['question'] , q['content'][ q['correct'] ])

for q in data['games'][0]['questions']:
    print(q['question'])
    print(q['content'])
    answer = int(input('Enter index of the correct answer: '))
    if answer != q['correct']:
        print(f'wrong , correct answer\'s index was {q["correct"]}')
        break;
