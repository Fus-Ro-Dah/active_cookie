# most\_active\_cookie
## Challenge Description

Given a cookie log file in the following format:
cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00

Write a command line program in your preferred language to process the log file and return the most active cookie for specified day. The example below shows how we'll execute your program.

## Running Instruction
1. Make sure all neccessary python packages have been installed
2. **Running the searching program**
    The program has two arguments: 
    1. The CSV path
    2. The date query (YYYY-MM-DD), preceded by '-d'
    Example:
    `$ ./most\_active\_cookie cookie_log.csv -d 2018-12-08`
 3. **Running the testing program**
     The testing program has two arguments:
     1. The number of test cases
     2. The desired length of tesing file
     Example:
     `python3 tester.py 2 5`

