#!/usr/bin/env python

import pypwned
import argparse
import time
import sys
import requests
import os
import json
import csv
import datetime
import re

# colors
W  = '\033[0m'  # white
R  = '\033[91m' # Light Red
B  = '\033[94m' # Light Blue
G  = '\033[92m' # Light Green
O  = '\033[33m' # orange
LG = '\033[37m' # Light Gray

def Banner():

	Banner = r"""
###########################################################        
______                         _ 
| ___ \                       | |
| |_/ /_      ___ __   ___  __| |
|  __/\ \ /\ / / '_ \ / _ \/ _` |
| |    \ V  V /| | | |  __/ (_| |
\_|     \_/\_/ |_| |_|\___|\__,_|

"""
	print O + Banner + W
        print '[' + G + '>' + W + '] Created by: Hashim Jawad (@ihack4falafel) of ACTIVELabs'
        print '[' + G + '>' + W + '] Version   : 1.0'
        print O + '###########################################################\n' + W 

def GetAllBreachesForAccount(Email):
    Counter = 1
    time.sleep(1.3)
    try:
        Request = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/{}'.format(Email), verify=True) 
        StatusCode = Request.status_code
        if StatusCode == 200:
            print '[' + R + '!' + W +'] Email account has been pwned'
            Json  = Request.content.decode('utf8', 'ignore')
            List = json.loads(Json)
            print '[' + G + '+' + W + '] Listing breaches..'
            for item in List:
                print 'Breach number: ' + str(Counter)
                Counter += 1
                print ('###########################################################\n'
                        + G + 'Breach Name' + W + ' | ' + R + unicode(item['Title']) + W + '\n'
                        + G + 'Domain     ' + W + ' | ' + R + unicode(item['Domain']) + W + '\n'
                        + G + 'Breach Date' + W + ' | ' + R + unicode(item['BreachDate']) + W + '\n'
                        + G + 'Fabricated ' + W + ' | ' + R + unicode(item['IsFabricated']) + W + '\n'
                        + G + 'Verified   ' + W + ' | ' + R + unicode(item['IsVerified']) +  W + '\n'
                        + G + 'Retired    ' + W + ' | ' + R + unicode(item['IsRetired']) + W + '\n'
                        + G + 'Spam       ' + W + ' | ' + R + unicode(item['IsSpamList']) + W + '\n'
                        + '###########################################################')
            now = datetime.datetime.now()
            File = str(Email) + '_' + str(now.strftime('%m-%d-%Y-%H-%M-%S')) + '.csv' 
            print '[' + G + '+' + W + '] Saving results to ' + str(File) + '..'
            time.sleep(1.3)
	    with open('%s' % File, 'w') as csvFile:
                fields = ['Name', 'Title', 'Domain', 'BreachDate', 'AddedDate', 'ModifiedDate', 'PwnCount', 'Description', 'LogoPath', 'DataClasses', 'IsVerified', 'IsFabricated', 'IsSensitive', 'IsRetired', 'IsSpamList']
                writer = csv.DictWriter(csvFile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(List)
            csvFile.close()
        elif StatusCode == 404:
            print '[' + G + '+' + W +'] Email account has not been pwned'
        elif StatusCode == 429:
            print '[' + R + '!' + W + '] Rate limit has been exceeded try again in few seconds'
        elif StatusCode == 403:
            print '[' + R + '!' + W + '] Forbidden! no user agent has been spcified'
        elif StatusCode == 400:
            print '[' + R + '!' + W + '] Bad request! Check account string'
    except Exception as error:
        print '[' + R + '+' + W + '] A New Exception occured: ', error


def GetAllPastesForAccount(Paste):
    Counter = 1
    time.sleep(1.3)
    try:
        Request = requests.get('https://haveibeenpwned.com/api/v2/pasteaccount/{}'.format(Paste), verify=True) 
        StatusCode = Request.status_code
        if StatusCode == 200:
            print '[' + R + '!' + W +'] Email account found on Pastebin'
            Json  = Request.content.decode('utf8', 'ignore')
            List = json.loads(Json)
            print '[' + G + '+' + W + '] Listing Pastebins..'
            for item in List:
                print 'Pastebin number: ' + str(Counter)
                Counter += 1
                print ('###########################################################\n'
                        + G + 'Title       ' + W + ' | ' + R + unicode(item['Title']) + W + '\n'
                        + G + 'Source      ' + W + ' | ' + R + unicode(item['Source']) + W + '\n'
                        + G + 'Email Count ' + W + ' | ' + R + unicode(item['EmailCount']) + W + '\n'
                        + G + 'ID          ' + W + ' | ' + R + unicode(item['Id']) + W + '\n'
                        + G + 'Date        ' + W + ' | ' + R + unicode(item['Date']) +  W + '\n'
                        + '###########################################################')
            now = datetime.datetime.now()
            File = 'Pastebin_' + str(Paste) + '_' + str(now.strftime('%m-%d-%Y-%H-%M-%S')) + '.csv' 
            print '[' + G + '+' + W + '] Saving results to ' + str(File) + '..'
            time.sleep(1.3)
            with open('%s' % File, 'w') as csvFile:
                fields = ['Date', 'Source', 'EmailCount', 'Id', 'Title']
                writer = csv.DictWriter(csvFile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(List)
            csvFile.close()
        elif StatusCode == 404:
            print '[' + G + '+' + W +'] Email account has not been found on Pastebin'
        elif StatusCode == 429:
            print '[' + R + '!' + W + '] Rate limit has been exceeded try again in few seconds'
        elif StatusCode == 403:
            print '[' + R + '!' + W + '] Forbidden! no user agent has been spcified'
        elif StatusCode == 400:
            print '[' + R + '!' + W + '] Bad request! Check account string'
    except Exception as error:
        print '[' + R + '+' + W + '] A New Exception occured: ', error

def GetAllBreachesForDomain(Domain):

    Counter = 1
    print '[' + G + '+' + W + '] Checking domain for possible breaches..'
    time.sleep(1.3)
    try:
        if pypwned.getAllBreaches(domain=Domain):
            print '[' + R + '!' + W + '] Domain has been pwned'
            List =  pypwned.getAllBreaches(domain=Domain)
	    print '[' + G + '+' + W + '] Listing breaches..'
            for item in List:
                print 'Breach number: ' + str(Counter)
                Counter += 1
                print ('###########################################################\n'
                        + G + 'Breach Name' + W + ' | ' + R + unicode(item['Title']) + W + '\n'
                        + G + 'Domain     ' + W + ' | ' + R + unicode(item['Domain']) + W + '\n'
                        + G + 'Breach Date' + W + ' | ' + R + unicode(item['BreachDate']) + W + '\n'
                        + G + 'Fabricated ' + W + ' | ' + R + unicode(item['IsFabricated']) + W + '\n'
                        + G + 'Verified   ' + W + ' | ' + R + unicode(item['IsVerified']) +  W + '\n'
                        + G + 'Retired    ' + W + ' | ' + R + unicode(item['IsRetired']) + W + '\n'
                        + G + 'Spam       ' + W + ' | ' + R + unicode(item['IsSpamList']) + W + '\n'
                        + '###########################################################')
            now = datetime.datetime.now()
            File = str(Domain) + '_' + str(now.strftime('%m-%d-%Y-%H-%M-%S')) + '.csv' 
            print '[' + G + '+' + W + '] Saving results to ' + str(File) + '..'
            time.sleep(1.3)
            with open('%s' % File, 'w') as csvFile:
                fields = ['Name', 'Title', 'Domain', 'BreachDate', 'AddedDate', 'ModifiedDate', 'PwnCount', 'Description', 'LogoPath', 'DataClasses', 'IsVerified', 'IsFabricated', 'IsSensitive', 'IsRetired', 'IsSpamList']
                writer = csv.DictWriter(csvFile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(List)
            csvFile.close()
        else:
            print '[' + G + '+' + W + '] Domain has not been pwned'

    except Exception as error:
        print '[' + R + '+' + W +'] A New Exception occured: ', error


def main():

    global Email, Domain, Paste, EmailsList

    Banner() 

    parser = argparse.ArgumentParser('A python client for HaveIBeenPwned REST API. The script will output table of findings to stdout and dump the results if any to .csv file')
    parser.add_argument('-cd', metavar='<domain name>', dest='Domain', help='check existing breaches for specified domain')
    parser.add_argument('-cp', metavar='<email account>', dest='Paste', help='check current pastes for given email. This option accept file with list of emails as an input, the file format should be one email per line')
    parser.add_argument('-ce', metavar='<email account>', dest='Email', default=None, help='check possible breaches for given email. This option accept file with list of emails as an input, the file format should be one email per line')
    args = parser.parse_args()
    
    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit(1)
    elif args.Domain:
        Domain = args.Domain
        GetAllBreachesForDomain(Domain)
    elif args.Paste:
        if re.search('@', str(args.Paste)):
	    Paste = args.Paste
	    print '[' + G + '+' + W +'] Checking ' + str(Paste) + ' for possible pastes..'
            GetAllPastesForAccount(Paste)
	else:
	    EmailsFile = args.Paste
	    try:
	        f = open(EmailsFile)
	        EmailsList = f.read().splitlines()
		print '[' + G + '+' + W +'] Parsing email list for possible pastes..'
		for item in EmailsList:
			Paste = item
			print '[' + G + '+' + W +'] Checking ' + str(Paste) + ' for possible pastes..'
			GetAllPastesForAccount(Paste)
	    except Exception as error:
                print '[' + R + '+' + W +'] A New Exception occured: ', error
    elif args.Email:
        if re.search('@', str(args.Email)):
	    Email = args.Email
	    print '[' + G + '+' + W +'] Checking ' + str(Email) + ' for possible breaches..'
            GetAllBreachesForAccount(Email)
	else:
	    EmailsFile = args.Email
	    try:
	        f = open(EmailsFile)
	        EmailsList = f.read().splitlines()
		print '[' + G + '+' + W +'] Parsing email list for possible breaches..'
		for item in EmailsList:
			Email = item
			print '[' + G + '+' + W +'] Checking ' + str(Email) + ' for possible breaches..'
			GetAllBreachesForAccount(Email)
	    except Exception as error:
                print '[' + R + '+' + W +'] A New Exception occured: ', error
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
