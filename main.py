# define function
def topFiveMovies():
    # print first movie
    print("2 fast 2 furious")
   
    #print second movie
    print("divergent")
   
    #print third movie
    print("us")
   
    #print fourth movie
    print("cars")
   
    #print fifth movie
    print("The glass castle")

print("these are my top five movies")
topFiveMovies()
#define second function
def topThreePlaces():
    #print first place
    print("Greece")
    #print second place
    print("California")
    #print third place
    print("Japan")

print("these are my top three places")
#run function
topThreePlaces()
#define third function
def topThreeColors():
    #print fist color
    print("black")
    #print second color
    print("red")
    #print third color
    print("blue")

#print description
print("these are my top three colors")
#run function
topThreeColors()
#define fourth function
def topThreeStores():
    #print first store
    print("target")
    #print second store
    print("platos closet")
    #print third store
    print("american eagle")

#print description
print("these are my top three stores")
#run function
topThreeStores()
#define fifth function
def topThreeAnimals():
    #print first animal
    print("dog")
    #print second animal
    print("horse")
    #print third animal
    print("cat")

print("these are my top three animals")
topThreeAnimals()



#define a function that out outs your name
#followed by is my name
def myNameIs(nameIs):
    #print name
    print(nameIs + " is my name")

#run function
myNameIs("Emily")

#define function
def timesTwo(answer):
    #print
    print(answer * 2)
#run function
timesTwo(12)

#define function
def plusFive(total):
    #print
    print(total + 5)
#run function
plusFive(15)

#define function
def divideTwo(number):
    #print
    print(number / 2)
#run function
divideTwo(64)

#define function
def addTwoNumbers(one, two):
    #print
    print(one + two)
#run function
addTwoNumbers(82, 18)

#deifne function
def madLib(holiday, noun, place, person, adjective, pluralBodyPart, verb, adjectiveTwo, nounTwo, food, pluralNoun):
    #print
    print("I can't believe it's already " + holiday + " I can't wait to put on my " + noun + " and visit every " + place +  
    " in my neighborhood, This year, i am going to dress up as (a) " + person + " with " + adjective + " " + pluralBodyPart + 
    ". Before I " + verb + ", I make sure to grab my " + adjectiveTwo + " " + nounTwo + " to hold all of my " + food + 
    ". Finally, all of my " + pluralNoun + " are ready to go!")

#run function
madLib("halloween", "costume", "house", "cowboy", "slimy", "hands", "drive", "colorful", "bag", "candy", "friends")

#define function
def woof():
    #print
    print("woof")
#run function
woof()

#define function
def woofTwo():
    #return woof
    return "Woof"
#print function
print(woofTwo())

#define function
def cat():
    #return
    return "cat"

#define function
def dog():
    #return
    return "dog"

#print functions
print(cat() + dog())

#define function
def numberOfPlanets():
    #return value of planets
    return "8"
#print function
print(numberOfPlanets())

#defien function
def practiceFunction(N):
   #if statments
    if (N >= 10):
        return "hi!"
    if (N < 10):
        return "bye!"

#print function
print(practiceFunction(11))

#define function
def elseStatments(E):
    if (E < 26):
        return "dog"
    else:
        return "cat"
#print function
print(elseStatments(44))

#define statments
def trueOrFalse(x):
    if x > 10:
        return "x is greater than 10"
    else:
        return "x is not greater than 10"
#run function
print(trueOrFalse(5))

#define function
def evenOrOdd(x):
#define statements
    if x % 2 == 0:
        return True
    else:
        return False
 #run function
print(evenOrOdd(10))

#define function
def twoBigNumbers(x, y):
#define statements
    if x > 10 and y > 10:
        return True
    else:
        return False
#run function
print(twoBigNumbers(10,6))

#define function
def toBeOrNot(x, y):
 #define statemnets
    if x > 10 or not y > 10:
        return True
    else:
        return False
#run function
print(toBeOrNot(10, 6))

#define function
def tooMuch(x, y, z):
#define statements
    if x > 10 or (not y > 10 and z == 5):
        return True
    else:
        return False
#run function
print(tooMuch(10, 6, 8))

#define function
def printTimesSeven():
    #print statements
    print("dog")
    print("dog")
    print("dog")
    print("dog")
    print("dog")
    print("dog")
    print("dog")
#run function
printTimesSeven()

# do this instead

#define function
def whileLoop():
    #variable defenition
    count = 1
    #make while statement
    while count < 10:
        #print
        print("yes")
        count = count + 1
#run function
whileLoop()

#define function
def countExample():
    count = 1
    print(count)
    count = 2
    print(count)

#define function
def dogTooManyTimes():
    count = 1
    while  count <=  9:
        print("dog")
        count = count + 1
    #run function
dogTooManyTimes()

#define function
def oneToOneHundered():
    count = 1
    while count <= 100:
        print(count)
        count = count + 1
#run function
oneToOneHundered()

#define function
def byFive():
    count = 5
    while count <= 100:
        print(count)
        count = count + 5
#run function
byFive()

#define function
def countToTen():
    count = 1
    number = 1
    while number <= 10:
        while count <= 10:
            print(count)
            count = count + 1
        number = number + 1
        count = 1
countToTen()

#define variable practice
mystring = "potato"
#postions   012345

#define function
def lastLetter(w):
    return w[len(w) - 1]
#run function
print(lastLetter("potato"))

#define function
def spellingBee(w):
    x = 0
    while x < len(w):
        print(w[x])
        x = x + 1
#run function
spellingBee("hippo")