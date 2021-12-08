from os import write
import most_active_cookie
import random
import string
import csv
import sys
import os

class processorTester:
    def __init__(self):
        self.cookieSize = 16
    
    """
    This function generates a random cookie of cookieSize
    """
    def generateARandomCookie(self):
        cookieCharacters = string.ascii_letters + string.digits
        randomCookie = ""
        for i in range(self.cookieSize):
            randomCookie += random.choice(cookieCharacters)
        return randomCookie

    """
    This function generates a random date that has the same format as timestamp
    """
    def generateARandomDate(self):
        randomDate = ""
        for i in range(4):
            randomDate += random.choice(string.digits)
        randomDate += '-'
        for i in range(2):
            randomDate += random.choice(string.digits)
        randomDate += '-'
        for i in range(2):
            randomDate += random.choice(string.digits)
        randomDate += 'T'
        for i in range(2):
            randomDate += random.choice(string.digits)
        randomDate += ':'
        for i in range(2):
            randomDate += random.choice(string.digits)
        randomDate += ':'
        for i in range(2):
            randomDate += random.choice(string.digits)
        randomDate += '+00:00'
        return randomDate

    """
    This function generates a given number of random cookie
    """
    def generateFixedNumberOfRandomCookie(self, testNum):
        randomCookieList = []
        for i in range(testNum):
            randomCookieList.append(self.generateARandomCookie())
        return randomCookieList
    
    """
    This function generates a given number of random dates
    """
    def generateFixedNumberOfRandomDate(self, testNum):
        randomDateList = []
        for i in range(testNum):
            randomDateList.append(self.generateARandomDate())
        return randomDateList
    
    """
    This function writes the cookie and date lists into a csv file
    """
    def exportIntoCsv(self, randomCookies, randomDates):
        with open('tempTestFile.csv', 'w') as t:
            writer = csv.writer(t)
            writer.writerow(['cookie', 'timestamp'])
            for i in range(len(randomCookies)):
                writer.writerow([randomCookies[i], randomDates[i]])


if __name__ == '__main__':
    arguments = sys.argv
    #The number of test cases
    testCaseNum = int(arguments[1])
    #The length of the testing csv
    testCsvSize = int(arguments[2])
    for i in range(testCaseNum):
        tester = processorTester()
        cookieList = tester.generateFixedNumberOfRandomCookie(testCsvSize)
        dateList = tester.generateFixedNumberOfRandomDate(testCsvSize)
        tester.exportIntoCsv(cookieList, dateList)
        print("Test case ", i + 1)
        print("Cookie:")
        print(cookieList)
        print("Timestamps:")
        print(dateList)
        processor = most_active_cookie.Processor()
        processor.readLog('tempTestFile.csv')
        #parse the time into YYYY-MM-DD
        processor.parseTimeByUTC()
        #categorize the cookie according to date
        processor.categorizeCookie()
        print("The dictionary entry for this test case's first date is:")
        tmpDict = processor.dict
        print(tmpDict)
        print(dateList[0], tmpDict[dateList[0][0:10]])
        #get the list for most active cookies
        res = processor.findMaxOccurence(dateList[0][0:10])
        print("The most active cookie for the first date is:")
        for i in res:
            print(i)
        os.remove('tempTestFile.csv')
        print("\n")
