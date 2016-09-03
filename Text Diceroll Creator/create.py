number = 0
tempnumber = 1
o = open("output.txt", "w")
f = open("lines.txt", "r")

person = ['scout', 'soldier', 'pyro', 'demoman', 'heavy', 'engineer', 'medic', 'sniper', 'spy', 'other']

def finish(numbers):
    global number
    global tempnumber
    time = 1
    for x in range(1, numbers):
        time2 = time+1
        if time2 == numbers:
            time2 = 1
        o.write("alias "+person[number]+"_diceroll_"+str(time)+" \"alias "+person[number]+"_result "+person[number]+"text"+str(time)+"; alias "+person[number]+"_diceroll "+person[number]+"_diceroll_"+str(time2)+"\"\n")
        time+=1
    o.write("alias "+person[number]+"_diceroll "+person[number]+"_diceroll_1\n")
    number +=1
    tempnumber = 1
    o.write("\n")

def process(text):
    global tempnumber
    if text is '':
        o.write("\n")
        finish(tempnumber)
        return
    o.write("alias " + person[number] + "text" + str(tempnumber) + " \"say "+text+"; trashcan_cycle; unbindnum\"\n")
    tempnumber +=1

for line in f:
    if number < 10:
        process(line.rstrip())
else:
    o.write("alias trashcan_cycle \"")
    for x in range(0, 9):
        o.write(person[x]+"_diceroll; ")
		
    o.write("other_diceroll\"\n\nalias trashmessage \"alias message echo Chat binds switched to: Trashtalk.\"\n\n")
    o.write("alias switchtrash \"unbindnum; ")

    for y in range(0, 9):
        o.write("alias KP_"+str(y+1)+" "+person[y]+"_result;")

    o.write("alias KP_plussign other_result; trashcan_cycle; trashmessage; showonscreen\"")

f.close()
o.close()