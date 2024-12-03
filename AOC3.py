import os

fileName = os.path.basename(__file__);

inputPath = os.path.dirname(__file__) + "/Inputs/" + fileName[0: len(fileName)-3] + "_in.txt";

with open(inputPath, 'r') as file:
    data = file.read()

print(data);