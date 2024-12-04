import os

fileName = os.path.basename(__file__);

inputPath = os.path.dirname(__file__) + "/Inputs/" + fileName[0: len(fileName)-3] + "_in.txt";

with open(inputPath, 'r') as file:
    data = file.read()

mul1 = None;
mul2 = None;


dataBad = "mul(4*, mul(6,9!, ?(12,34),mul ( 2 , 4 )";
dataGood = "mul(11,8)mul(8,5)";

data = dataGood;

it = 0;
global offset;
offset = 0;
max = len(data); # len 1 more than highest index
global total
total = 0;
global good;
good = 0;
global testStep
testStep = 1;

def isNum(test):
    return ord(test) >= 48 and ord(test) <= 57;

def validate(step, pos):
    global numStr;
    #numStr = "";
    print(data[pos]);
    if step == 1:
        if data[pos] == 'm':
            return True;
        else:
            return False;
        
    elif step == 2:
        if data[pos] == 'u':
            return True;
        else:
            return False;
    elif step == 3:
        if data[pos] == 'l':
            return True;
        else:
            return False;
    elif step == 4:
        if data[pos] == '(':
            return True;
        else:
            return False;
    elif step == 5:
        if isNum(data[pos]):
            numStr = data[pos];
            return True;
        else:
            return False;
    elif step == 6:
        if isNum(data[pos]):
            numStr += data[pos];
            return True;
        elif data[pos] == ',':
            mul1 = int(numStr);
            return True;
        else:
            return False;
    elif step == 7:
        if isNum(data[pos]):
            numStr += data[pos];
            return True;
        elif data[pos] == ',':
            testStep = 8;
            mul1 = int(numStr);
            return True;
        else:
            return False;
    elif step == 8:
        if data[pos] == ',':
            return True;
        else:
            return False;
    elif step == 9:
        if isNum(data[pos]):
            numStr = data[pos];
            return True;
        else:
            return False;
    elif step == 10:
        if isNum(data[pos]):
            numStr += data[pos]
            return True;
        elif data[pos] == ',':
            mul2 = int(numStr);
            return True;
        else:
            return False;
    elif step == 11:
        if isNum(data[pos]):
            numStr += data[pos];
            return True;
        elif data[pos] == ',':
            mul2 = int(numStr);
            return True;
        else:
            return False;
    elif step == 12:
        if data[pos] == ')':
            total += (mul1 * mul2);
            pos += offset;
            testStep = 0;
            return True;
        else:
            return False;



    return True;



while(it < max-1):
    valid = validate(testStep, it + offset);
    if(valid):
        #it += 1; # shouldn't be needed since using offset to advance
        offset += 1; # TODO check edges to keep from skipping chars
        testStep += 1;
    else:
        it += offset;


print(total);
