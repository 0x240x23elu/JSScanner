#import faster_than_requests as requests
import concurrent.futures
import requests
from concurrent import futures
#import requests as r 
import re 
import urllib3 
import os
import colored
from colored import stylize
urllib3.disable_warnings()
print(colored.fg("red"), 
     "╔════════════════════════════════════════════════════════════════╗\n"
      "║                    Devlope By 0x240x23elu                      ║\n"
      "║                                                                ║\n"
      "╚════════════════════════════════════════════════════════════════╝")
print("╔════════════════════════════════════════════════════════════════╗\n"
      "║                                                                ║\n"
      "║                           WARNING                              ║\n"
      "║                                                                ║\n"
      "║      I highly recommend using this tool by using Kali Linux OS ║\n"
      "║                                                                ║\n"
      "║      By using this tool it means you agree with terms,         ║\n"
      "║      conditions, and risks                                     ║\n"
      "║                                                                ║\n"
      "║      By using this tool you agree that                         ║\n"
      "║      1. use for legitimate security testing                    ║\n"
      "║      2. not for crime                                          ║\n"
      "║      3. the use of this tool solely for                        ║\n"
      "║         educational reasons only                               ║\n"
      "║                                                                ║\n"
      "║      By using this tool you agree that                         ║\n"
      "║      1. You are willing to be charged with criminal or state   ║\n"
      "║         law applicable by law enforcement officers             ║\n"
      "║         and government when abused                             ║\n"
      "║      2. the risk is borne by yourself                          ║\n"
      "║                                                                ║\n"
      "║         Thank you and happy pentest                            ║\n"
      "║                                                                ║\n"
      "╚════════════════════════════════════════════════════════════════╝")

path = input("Please Enter Any File: ") 
reg = input("Path Of Regex/Patten File: ")
list=[] 
file1 = open(path, 'r')
Lines = file1.readlines() 
count = 0
# Strips the newline character
for line in Lines: 
    ip = line.strip()
    print(colored.fg("white"), ip)
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [
                executor.submit(
                    lambda: requests.get(ip))
            for _ in range(1)
        ]
            

        results = [
            f.result().text
            for f in futures
        ]

        
        
        file2 = open(reg, 'r')
        Lines2 = file2.readlines()
        for line2 in Lines2: 
            regex = line2.strip()
        #print(regex)
            matches = re.finditer(regex, str(results), re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
    
                print (colored.fg("green") ,"Regex: ",regex)
                print(colored.fg("red") , "Match {matchNum} was found at: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()), '\n')
                f = open('out.txt.txt', 'a')
                L = [ip, '\n', "Regex: ", regex, '\n', "Match {matchNum} was found at : {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()),'\n']
                f.writelines(L)
                f.close()
           
    except requests.exceptions.RequestException as e:
        # A serious problem happened, like an SSLError or InvalidURL
        print("Error: {}".format(e))    

