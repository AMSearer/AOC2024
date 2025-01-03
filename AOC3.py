import os

globalDict = {}

fileName = os.path.basename(__file__);

inputPath = os.path.dirname(__file__) + "/Inputs/" + fileName[0: len(fileName)-3] + "_in.txt";

with open(inputPath, 'r') as file:
    data = file.read()

global mul1;
global mul2;
globalDict["mul1"] = None;
globalDict["mul2"] = None;
globalDict["total"] = 0;
globalDict["do"] = True;


dataBad = "mul(4*, mul(6,9!, ?(12,34),mul ( 2 , 4 )";
dataGood = "mul(11,8)mul(8,5)";
dataGood = "mul(620,236)mul(589,126)mul(260,42)mul(335,250)mul(422,738)mul(694,717)mul(417,219)mul(366,638)mul(773,126)";
dataGood = "}mul(620,236)where()*@}!&[mul(589,126)]&^]mul(260,42)when() when()$ ?{/^*mul(335,250)>,@!<{when()+-$don't()*'^?+>>/%:mul(422,738),mul(694,717);~;%<[why()>@-mul(417,219)?&who(474,989){select()-{#mul(366,638)mul(773,126)/*";

# data = dataGood;

# data = "mul(620,236)"

it = 0;
global offset;
offset = 0;
max = len(data); # len 1 more than highest index
# global total
# total = 0;
global good;
good = 0;
global testStep
testStep = 1;

def isNum(test):
    return ord(test) >= 48 and ord(test) <= 57;

def validate(step, pos):
    global numStr;
    global total;
    # global mul1;
    # global mul2;
    
    try:
        if(total == None):
            total = 0;
    except NameError:
        total = 0;
    
    try:
        if(mul1 == None):
            mul1 = 0;
    except NameError:
        mul1 = 0;
    
    try:
        if(mul2 == None):
            mul2 = 0;
    except NameError:
        mul2 = 0;

    #numStr = "";
    # print(data[pos]);
    if step == 1:
        if data[pos] == 'm':
            return True;
        elif data[pos] == 'd':
            if data[pos:pos+4] == "do()":
                globalDict["do"] = True;
            elif data[pos:pos+7] == "don't()":
                globalDict["do"] = False;
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
            testStep = 8;
            globalDict["mul1"] = int(numStr);
            return True;
        else:
            return False;
    elif step == 7:
        if isNum(data[pos]):
            numStr += data[pos];
            return True;
        elif data[pos] == ',':
            testStep = 8;
            globalDict["mul1"] = int(numStr);
            return True;
        else:
            return False;
    elif step == 8:
        if data[pos] == ',':
            globalDict["mul1"] = int(numStr);
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
        elif data[pos] == ')':
            globalDict["mul2"] = int(numStr);
            if(globalDict["do"]):
                globalDict["total"] += globalDict["mul1"] * globalDict["mul2"]
            # total += (mul1 * mul2);
            pos += offset;
            testStep = 0;
            return False;
        else:
            return False;
    elif step == 11:
        if isNum(data[pos]):
            numStr += data[pos];
            return True;
        elif data[pos] == ')':
            globalDict["mul2"] = int(numStr);
            if(globalDict["do"]):
                globalDict["total"] += globalDict["mul1"] * globalDict["mul2"]
            # total += (mul1 * mul2);
            pos += offset;
            testStep = 0;
            return False;
        else:
            return False;
    elif step == 12:
        if data[pos] == ')':
            # total += (mul1 * mul2);
            globalDict["mul2"] = int(numStr);
            if(globalDict["do"]):
                globalDict["total"] += globalDict["mul1"] * globalDict["mul2"]
            pos += offset;
            testStep = 0;
            return False;
        else:
            return False;



    return True;



while(it < max-1):
    valid = validate(testStep, it + offset);
    if(valid):
        #it += 1; # shouldn't be needed since using offset to advance
        
        if( data[it+offset] == ','):
            testStep = 9;
        else:
            testStep += 1;
        offset += 1; # TODO check edges to keep from skipping chars
    else:
        it += offset + 1;
        offset = 0;
        testStep = 1;


print(globalDict["total"]);
