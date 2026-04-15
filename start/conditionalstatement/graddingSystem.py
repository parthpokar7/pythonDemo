html=int(input("enter html marks: "))
css=int(input("enter css marks: "))
js=int(input("enter js marks: "))
python=int(input("enter python marks: "))
java=int(input("enter java marks: "))
ruby=int(input("enter ruby marks: "))

if (html>100 or css>100 or js>100 or python>100 or java>100 or ruby>100):
    print("marks must be in range of 0 to 100")


marks = {
    "html": html,
    "css":css,
    "js":js,
    "python":python,
    "java":java,
    "ruby":ruby
}

gracedSubs = {}
failedCounter = 0

counter = 0
if marks["html"]<25:
    failedCounter += 1
if marks["css"]<25:
    failedCounter += 1
if marks["js"]<25:
    failedCounter += 1
if marks["python"]<25:
    failedCounter += 1
if marks["java"]<25:
    failedCounter += 1
if marks["ruby"]<25:
    failedCounter += 1

if marks["html"]>=25 and marks["html"]<35:
    counter += 1
    gracedSubs["html"] = (35 - marks["html"]) + marks["html"]
if marks["css"]>=25 and marks["css"]<35:
    counter += 1
    gracedSubs["css"] = (35 - marks["css"]) + marks["css"]
if marks["js"]>=25 and marks["js"]<35:
    counter += 1
    gracedSubs["js"] = (35 - marks["js"]) + marks["js"]
if marks["python"]>=25 and marks["python"]<35:
    counter += 1
    gracedSubs["python"] = (35 - marks["python"]) + marks["python"]
if marks["java"]>=25 and marks["java"]<35:
    counter += 1
    gracedSubs["java"] = (35 - marks["java"]) + marks["java"]
if marks["ruby"]>=25 and marks["ruby"]<35:
    counter += 1
    gracedSubs["ruby"] = (35 - marks["ruby"]) + marks["ruby"]

totalMarks = 0
percentage = 0

if failedCounter == 0: #marks less than 25
    if counter <=2: #grace marks
        totalMarks = marks["html"] + marks["css"] + marks["js"] + marks["python"] + marks["java"] + marks["ruby"]
        percentage = (totalMarks / 600) * 100
        print(totalMarks)
        print(percentage)

        # if counter!=0:
        subs = tuple(gracedSubs.keys())
        #     print("you have been provided grace marks in " + str(counter) + " subjects :", subs)

        if counter==1:
            print("you have been provided grace marks in " + str(counter) + " subjects : " + str(subs[0]))
            print("actual marks of '" + str(subs[0]) + "' is: " + str(marks[subs[0]]) + " >>>> Updated marks: " + str(gracedSubs[subs[0]]))
        else:
            print("you have been provided grace marks in " + str(counter) + " subjects : "+ str(subs[0]) +" & " + str(subs[1]))
            print("actual marks of '" + str(subs[0]) + "' is: " + str(marks[subs[0]]) + " >>>> Updated marks: " + str(gracedSubs[subs[0]]))
            print("actual marks of '" + str(subs[1]) + "' is: " + str(marks[subs[1]]) + " >>>> Updated marks: " + str(gracedSubs[subs[1]]))

    elif counter == 0:
        totalMarks = html + css + js + python + java + ruby
        percentage = (totalMarks / 600) * 100
        print("total Marks :", totalMarks)
        print("total Percentage: ", percentage)
    else:
        print("failed")
else:
    print("failed")

if percentage > 85 and percentage <= 100:
    print("grade A")
elif percentage > 70 and percentage <= 85:
    print("grade B")
elif percentage > 55 and percentage <= 70:
    print("grade C")
elif percentage > 35 and percentage <= 55:
    print("grade D")
