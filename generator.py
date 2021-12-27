#imports
import random

#read the data file
with open("data.txt","r") as dataFILE:
    data = dataFILE.read()

#fix data
data += " %%%end"
data = data.lower()
    
#split data
data = data.split(" ")

#analyze data
patterns = {}
seen1 = []
seen2 = {}
index = {}
lword = ".."
for word in data:
    if lword in seen1:
        if word in seen2[lword]:
            #print(patterns[lword])
            #print(word)
            #print(index[lword][word])
            #print(lword)
            #if "by" in patterns: print(patterns["by"])
            patterns[lword][index[lword][word]]["times"] += 1
        else:
            patterns[lword].append({"word":word,"times":1})
            index[lword][word] = len(patterns[lword])-1
            seen2[lword] = [word]
    else:
        patterns[lword] = []
        if word == "%%%end": break
        seen1.append(lword)
        patterns[lword].append({"word":word,"times":1})
        index[lword] = {}
        index[lword][word] = len(patterns[lword])-1
        seen2[lword] = [word]
    lword = word
#print(patterns)

#generate new sentance
def ran(arr):
    if len(arr) <= 0: return "%%%term"
    p_arr = []  #proportioned array
    for d in arr:   #loops through array
        #print(arr)
        for x in range(d["times"]):
            p_arr.append(d["word"])
    return random.choice(p_arr)

sen = input("create your story:\n")
sentot = ""
lword = sen.strip().split(" ")[-1]
length = 20
while True:
    for x in range(int(length)):
        pattern = patterns[lword]
        word = ran(pattern)
        if word == "%%%term": break
        if word == "%%%end": break
        sen += " " + word
        lword = word

    print(sen)
    nxt = input("")
    sentot += sen
    if nxt == "log":
        with open("output.txt","w") as FILE:
            FILE.write(sentot)
    sen = ""
    
