from csv import reader
import sys

#This is the class for the processor that deals with the cookie log
class Processor:
    def __init__(self):
        #list for answer
        self.ans = []
        #dictionary for dates as keys and lists of cookies as value
        self.dict = {}
        #list for the original strings of time read from logs
        self.listOfOriginalTime = []
        #list for the original cookie read from logs
        self.listOfCookie = []
        #list for the processed times in the format of YYYY-MM-DD
        self.allParsedTime = []

    
    #This function parses the given string ad return the UTC time it's representing
    #pre: a string representing the timestamp is given
    #post: a list containing the year, month and date is returned
    def parseTimeByUTC(self):
        
        #Go through each of the time string
        for originalTime in self.listOfOriginalTime:
            #collect the parts of a time record
            year = originalTime[0:4]
            month = originalTime[5:7]
            date = originalTime[8:10]
            #put the time record's year, month and date into the list
            self.allParsedTime.append([year, month, date])

    #This function returns the list containing the most active cookies
    #pre: a list containing all cookies in a day is given
    #post: a list containing the most active cookies is returned
    def findMaxOccurence(self, inputDate):
        #retrieve the list of cookie of a given date
        listForQuery = self.dict[inputDate]
        #find the maximum frequency
        maxFreq = 0
        for l in listForQuery:
            if maxFreq < listForQuery.count(l):
                maxFreq = listForQuery.count(l)
        #find the corresponding cookie with max frequency
        for l in listForQuery:
            if listForQuery.count(l) == maxFreq and l not in self.ans:
                self.ans.append(l)
        return self.ans
    
    #This function reads the cookie and time in the log into two lists
    #pre: a filename of a log is given
    #post: the two columns of the log is read into two lists
    def readLog(self, fileName):
        #open the given file
        with open(fileName, 'r') as f:
            csv_reader = reader(f)
            listOfLog = list(csv_reader)
            #loop through the log and store values into two lists
            for l in listOfLog:
                #read cookie
                if l[0] != 'cookie':
                    self.listOfCookie.append(l[0])
                #read timestamp
                if l[1] != 'timestamp':
                    self.listOfOriginalTime.append(l[1])
    
    #This function categorizes the cookie according to time and stores them in a dictionary
    #pre: we have two lists of cookies and parsed time(YYYY-MM-DD)
    #post: we fill the dictionary using time as key and a list containing all cookie as value
    def categorizeCookie(self):
        for i in range(len(self.listOfCookie)):
            currentYear = self.allParsedTime[i][0]
            currentMonth = self.allParsedTime[i][1]
            currentDate = self.allParsedTime[i][2]
            currentTime = currentYear + "-" + currentMonth + "-" + currentDate
            #insert the timestamp into the dict
            if currentTime not in self.dict:
                self.dict[currentTime] = [self.listOfCookie[i]]
            else:
                self.dict[currentTime].append(self.listOfCookie[i])
            

#The main function
if __name__ == '__main__':
    arguments = sys.argv
    fileName = arguments[1]
    inputDate = arguments[3]
    processor = Processor()
    #read the log into lists
    processor.readLog(fileName)
    #parse the time into YYYY-MM-DD
    processor.parseTimeByUTC()
    #categorize the cookie according to date
    processor.categorizeCookie()  
    #get the list for most active cookies
    res = processor.findMaxOccurence(inputDate)
    for i in res:
        print(i)
