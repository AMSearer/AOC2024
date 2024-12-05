import os

globalDict = {}

fileName = os.path.basename(__file__);

inputPath = os.path.dirname(__file__) + "/Inputs/" + fileName[0: len(fileName)-3] + "_in.txt";

with open(inputPath, 'r') as file:
    lines = file.read()

    input = lines.split("\n\n")

rules = input[0].split("\n")
updatesStr = (input[1].split("\n"))
updates = []

updates.append([[int(y) for y in x.split(',')] for x in updatesStr])

# updates.append(x for x in updatesStr)

for updateStr in updatesStr:
    # updates.append(int(x) for x in updateStr.split(','))
    # print(updateStr.split(','))
    intList = [int(num) for num in updateStr.split(',')]
    # print(intList)


print(updates)