#import faster_than_requests as requests
import concurrent.futures
import requests
from concurrent import futures
#import requests as r 
import re 
import urllib3 
import sys 
import os
import colored
from colored import stylize
import argparse
urllib3.disable_warnings()
print(colored.fg("red"), "JSScan developed by @0x240x23elu adjusted by @sukenn")

parser = argparse.ArgumentParser(usage="python3 JSScanner.py --urls jsfiles.txt --regex regex.txt --output output.txt")
optional = parser._action_groups.pop()
optional.add_argument("-u","--urls",help="file including .js urls")
optional.add_argument("-r","--regex",help="file including regex")
optional.add_argument("-o","--output",help="output file")

parser._action_groups.append(optional)
args = parser.parse_args()

path = args.urls
reg = args.regex
output = args.output

if path is None:
    path = input("Please Enter Any File: ") 
if reg is None:
    reg = input("Path Of Regex/Patten File: ")
if output is None:
    output = input("Path To Save Output File: ")

list=[] 
file1 = open(path, 'r')
Lines = file1.readlines() 
count = 0
# Strips the newline character
for line in Lines: 
    ip = line.strip()
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
                print(colored.fg("green"), ip)
                print(colored.fg("red") , "Match {matchNum} was found at: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()), '\n')
                f = open(output, 'a')
                L = [ip, '\n', "Regex: ", regex, '\n', "Match {matchNum} was found at : {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()),'\n']
                f.writelines(L)
                f.close()
           
    except requests.exceptions.RequestException as e:
        # A serious problem happened, like an SSLError or InvalidURL
        print("Error: {}".format(e))    

