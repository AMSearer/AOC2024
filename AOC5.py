import os

globalDict = {}

fileName = os.path.basename(__file__);

inputPath = os.path.dirname(__file__) + "/Inputs/" + fileName[0: len(fileName)-3] + "_in.txt";

with open(inputPath, 'r') as file:
    lines = file.read()

    input = lines.split("\n\n")

rulesStr = input[0].split("\n")
updatesStr = (input[1].split("\n"))
updates = []
rules = []

for updateStr in updatesStr:
    updates.append([int(y) for y in updateStr.split(',')])

for ruleStr in rulesStr:
    rules.append([int(y) for y in ruleStr.split('|')])

# updates.append([[int(y) for y in x.split(',')] for x in updatesStr])

# print(updates)

updateValid = False;
validUpdates = []

for update in updates:
    updateValid = True;
    for idx, page in enumerate(update[-2::-1]):
        for rule in rules:
            if rule[1] == page:
                if rule[0] in update[-1-idx:]:
                    # print("Rule ", rule[0], "|", rule[1], "violated by page ", page)
                    updateValid = False;
    if updateValid:
        validUpdates.append([update[len(update) // 2], update]) 

# print(validUpdates)   

total = 0

for update in validUpdates:
    total += update[0]

print(total)