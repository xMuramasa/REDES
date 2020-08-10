import json

# define list with values

basicList = [[int(0), "", ""], [int(0), "", ""], [int(0), "", ""],
         [int(0), "", ""], [int(0), "", ""]]


# open output file for writing
with open('listfile.txt', 'w') as filehandle:
    json.dump(basicList, filehandle)


with open('listfile.txt', 'r') as filehandle:
    basicList = json.load(filehandle)

print(basicList)