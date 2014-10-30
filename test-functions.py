from kodemon import kodemon
import time


@kodemon
def waitFunction():
    print "I am so happy."
    time.sleep(1)
    print "Me to!"

@kodemon
def loopFunction():
    print "Look ma, I can count"
    for x in range(1, 5):
        print x
        time.sleep(1)

    print "Im all grown up now!"

if __name__ == "__main__":
    waitFunction()
    loopFunction()