from kodemon import kodemon
import time

# Extract filename
thisFilename = __file__
thisFilename = thisFilename[thisFilename.rfind("/") + 1:]

@kodemon(func_name="waitFunction", filename=thisFilename)
def waitFunction():
    print "I am so happy."
    time.sleep(1)
    print "Me to!"

@kodemon(func_name="loopFunction", filename=thisFilename)
def loopFunction():
    print "Look ma, I can count"
    for x in range(1, 5):
        print x
        time.sleep(1)

    print "Im all grown up now!"

if __name__ == "__main__":
    waitFunction()
    loopFunction()