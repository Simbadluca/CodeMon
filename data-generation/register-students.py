from kodemon import kodemon
from random import randrange
from time import sleep

# Extract filename
thisFilename = __file__
thisFilename = thisFilename[thisFilename.rfind("/") + 1:]

@kodemon(func_name="getApplications", filename=thisFilename)
def getApplications():

    sleep(1)
    return 20


@kodemon(func_name="getApplicant", filename=thisFilename)
def getApplicant(applicant):

    sleep(0.01)
    info = getPersonInformation(applicant)

    return info


@kodemon(func_name="getPersonInformation", filename=thisFilename)
def getPersonInformation(id):

    sum = 0
    for i in range(1000):
        sum += i + randrange(1000)

    sleep(0.02)
    print "adding some pressure: " + str(sum)
    print "Getting information for applicant with id: " + str(id)

    return sum + id

@kodemon(func_name="addApplicantInformationToDB", filename=thisFilename)
def addApplicantInformationToDB(info):

    sleep(0.2)
    print "Adding applicant with id " + str(info) + " to database"

    return info


@kodemon(func_name="registerApplicantAsStudent", filename=thisFilename)
def registerApplicantAsStudent(info):

    print "Registering student with id :" + str(info) + "."
    sleep(0.08)


@kodemon(func_name="cleanUpAndExit", filename=thisFilename)
def cleanUpAndExit():

    sleep(0.2)
    print "\nCleaning and exiting."
    sleep(1.3)
    print "Done."



if __name__ == "__main__":

    for applicant in range(getApplications() + 1):
        info = getApplicant(applicant)
        info = addApplicantInformationToDB(info)
        registerApplicantAsStudent(info)

    cleanUpAndExit()

