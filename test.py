import json
# def write(cmd, ans):
#     with open('words.json') as jsonfile:
#         decoded = json.load(jsonfile)
#     decoded[str(cmd)] = str(ans)
#     with open('words.json', 'w') as jsonfile:
#         json.dump(decoded, jsonfile)
# write('hello','hii')

# with open('words.json') as jsonfile:
#     data = json.load(jsonfile)
# data['hello'] = 'hii'
# with open('words.json', 'w') as jsonfile:
#     json.dump(data, jsonfile)
#     jsonfile.close()

# def write():
#     term=input('Enter a term')
#     defineterm=input('Definition')

#     with open('da.json') as data:
#         bag = json.load(data)
#         print('done')
        

    

# write()

with open('words.json') as data:
    list=json.load(data)
if 'america' in list:
    print('Success')
    print(list['america'])