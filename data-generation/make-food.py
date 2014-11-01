from kodemon import kodemon
from time import sleep
from random import uniform

# Extract filename
thisFilename = __file__
thisFilename = thisFilename[thisFilename.rfind("/") + 1:]


def getRandom():
    return uniform(0, 1.0)


@kodemon(func_name="walk", filename=thisFilename)
def walk():

    print "Step"
    sleep(0.1)


@kodemon(func_name="walkTo", filename=thisFilename)
def walkTo(steps, where):

    print "Walk to " + where
    for i in range(steps):
        walk()


@kodemon(func_name="open", filename=thisFilename)
def open(what):

    print "Open " + what
    sleep(0.3)


@kodemon(func_name="get", filename=thisFilename)
def get(what):

    print  "Get " + what
    sleep(0.02)


@kodemon(func_name="ret", filename=thisFilename)
def ret(what):
    print "Put back " + what
    sleep(0.3)


@kodemon(func_name="applayTo", filename=thisFilename)
def applayTo(do, to):

    print "Apply " + do + " to " + to
    sleep(getRandom())


@kodemon(func_name="fromAppliacne", filename=thisFilename)
def fromAppliacne(appliance):

    sleep(0.01)
    print "in " + appliance


@kodemon(func_name="eat", filename=thisFilename)
def eat(topping, food):

    print "Eat " + food + " with " + topping
    sleep(getRandom())
    print "Omnomnom"


@kodemon(func_name="makeFood", filename=thisFilename)
def makeFood(steps, where, appliance, topping, food):
    walkTo(steps, where)
    open(appliance)
    get(food)
    fromAppliacne(appliance)
    get(topping)
    fromAppliacne(appliance)
    applayTo(topping, food)
    ret(food)
    fromAppliacne(appliance)
    ret(topping)
    fromAppliacne(appliance)
    eat(topping, food)


if __name__ == "__main__":

    makeFood(10, "kitchen", "fridge", "butter", "bread")
