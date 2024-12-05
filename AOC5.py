import os

globalDict = {}

fileName = os.path.basename(__file__);

inputPath = os.path.dirname(__file__) + "/Inputs/" + fileName[0: len(fileName)-3] + "_in.txt";

input = []

count = 0

with open(inputPath, 'r') as file:
    lines = file.read()

    input = lines.split("\n\n")

rules = input[0].split("\n")
updates = input[1].split("\n")

