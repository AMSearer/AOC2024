import os

globalDict = {}

fileName = os.path.basename(__file__);

inputPath = os.path.dirname(__file__) + "/Inputs/" + fileName[0: len(fileName)-3] + "_in.txt";

array2D = []

count = 0

with open(inputPath, 'r') as file:
    for line in file.readlines():
        array2D.append(line.split())
# print(array2D)

def valid(a,b):
    if(0 <= a and a < len(array2D) ):
        if(0 <= b and b < len(array2D[a][0])):
            return True
    return False

gDict = {"N":[(-3, 0), (-2, 0), (-1, 0)], "NE":[(-3, 3), (-2, 2), (-1, 1)], "E":[(0, 3), (0, 2), (0, 1)], "SE":[(3, 3), (2, 2), (1, 1)], "S":[(3, 0), (2, 0), (1, 0)], "SW":[(3, -3), (2, -2), (1, -1)], "W":[(0, -3), (0, -2), (0, -1)], "NW":[(-3, -3), (-2, -2), (-1, -1)]}
# print(gDict["N"])

# for a in array2D:
#     for b in array2D[a]:
#         for dir in gDict:

# for dir in gDict:
#     print(dir)
#     for set in gDict[dir]:
#         print(set[0], set[1])

search = ['S', 'A', 'M']

# for aInd, a in enumerate(array2D, 0):
#     for bInd, b in enumerate(a[0],0):
#         for dir in gDict:
#             # print(gDict[dir])
#             if not (valid(aInd + gDict[dir][0][0], bInd + gDict[dir][0][1])):
#                     continue # continue to next dir if furthest offset index is not valid
#             elif( b == 'X'):
#                 for n in range(0,3):
#                     x = aInd + gDict[dir][n][0]
#                     y = bInd + gDict[dir][n][1]
#                     if( array2D[x][0][y] == search[n]):
#                         if(n == 2): count += 1;
#                         continue
#                     else:
#                         break

searchX = [['S', 'M'], ['M', 'S']]
searchDir = [[[-1, -1], [1, 1]],
              [[-1, 1], [1, -1]]]

firstFound = False

for aInd, a in enumerate(array2D, 0):
    for bInd, b in enumerate(a[0],0):
        for dir in searchDir:
            # print(gDict[dir])
            if not (valid(aInd + dir[0][0], bInd + dir[0][1])):
                    continue # continue to next dir if furthest offset index is not valid
            elif not(valid(aInd + dir[1][0], bInd + dir[1][1])):
                    continue
            elif( b == 'A'):
                x = aInd + dir[0][0]
                y = bInd + dir[0][1]
                w = aInd + dir[1][0]
                z = bInd + dir[1][1]

                for ele in searchX:
                        if(array2D[x][0][y] == ele[0] and array2D[w][0][z] == ele[1]):
                            if(firstFound): count+=1;
                            firstFound = True
                if not(firstFound):
                     break


        firstFound = False

print(count)