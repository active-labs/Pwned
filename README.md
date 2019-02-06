# Pwned
A python client for HaveIBeenPwned REST API. The script will output table of findings to stdout and dump the results if any to .csv file

## Installation
You need to install prerequisites and you should be good to go
```
pip install -r requirements.txt
```

## Usage
```
10:35:35 root@kali Pwned python Pwned.py -h

###########################################################        
______                         _ 
| ___ \                       | |
| |_/ /_      ___ __   ___  __| |
|  __/\ \ /\ / / '_ \ / _ \/ _` |
| |    \ V  V /| | | |  __/ (_| |
\_|     \_/\_/ |_| |_|\___|\__,_|


[>] Created by: Hashim Jawad (@ihack4falafel) of ACTIVELabs
[>] Version   : 1.0
###########################################################

usage: A python client for HaveIBeenPwned REST API. The script will output table of findings to stdout and dump the results if any to .csv file
       [-h] [-cd <domain name>] [-cp <email account>] [-ce <email account>]

optional arguments:
  -h, --help           show this help message and exit
  -cd <domain name>    check existing breaches for specified domain
  -cp <email account>  check current pastes for given email. This option
                       accept file with list of emails as an input, the file
                       format should be one email per line
  -ce <email account>  check possible breaches for given email. This option
                       accept file with list of emails as an input, the file
                       format should be one email per line
10:35:37 root@kali Pwned 
```

## Examples
Checking email for possible breach
```
10:52:34 root@kali Pwned python Pwned.py -ce test@test.local

###########################################################        
______                         _ 
| ___ \                       | |
| |_/ /_      ___ __   ___  __| |
|  __/\ \ /\ / / '_ \ / _ \/ _` |
| |    \ V  V /| | | |  __/ (_| |
\_|     \_/\_/ |_| |_|\___|\__,_|


[>] Created by: Hashim Jawad (@ihack4falafel) of ACTIVELabs
[>] Version   : 1.0
###########################################################

[+] Checking test@test.local for possible breaches..
[!] Email account has been pwned
[+] Listing breaches..
Breach number: 1
###########################################################
Breach Name | Dropbox
Domain      | dropbox.com
Breach Date | 2012-07-01
Fabricated  | False
Verified    | True
Retired     | False
Spam        | False
###########################################################
Breach number: 2
###########################################################
Breach Name | GeekedIn
Domain      | geekedin.net
Breach Date | 2016-08-15
Fabricated  | False
Verified    | True
Retired     | False
Spam        | False
###########################################################
Breach number: 3
###########################################################
Breach Name | iMesh
Domain      | imesh.com
Breach Date | 2013-09-22
Fabricated  | False
Verified    | True
Retired     | False
Spam        | False
###########################################################
Breach number: 4
###########################################################
Breach Name | Trillian
Domain      | trillian.im
Breach Date | 2015-12-27
Fabricated  | False
Verified    | True
Retired     | False
Spam        | False
###########################################################
[+] Saving results to test@test.local_02-06-2019-10-52-49.csv..
10:52:50 root@kali Pwned 
```

Checkling list of emails for public pastes
```
10:54:17 root@kali Pwned python Pwned.py -cp list.txt       

###########################################################        
______                         _ 
| ___ \                       | |
| |_/ /_      ___ __   ___  __| |
|  __/\ \ /\ / / '_ \ / _ \/ _` |
| |    \ V  V /| | | |  __/ (_| |
\_|     \_/\_/ |_| |_|\___|\__,_|


[>] Created by: Hashim Jawad (@ihack4falafel) of ACTIVELabs
[>] Version   : 1.0
###########################################################

[+] Parsing email list for possible pastes..
[+] Checking test@test.local for possible pastes..
[+] Email account has not been found on Pastebin
[+] Checking test1@test.local for possible pastes..
[!] Email account found on Pastebin
[+] Listing Pastebins..
Pastebin number: 1
###########################################################
Title        | pxahb.xyz
Source       | AdHocUrl
Email Count  | 1695
ID           | http://pxahb.xyz/emailpass/www.naamyoga.com.txt
Date         | None
###########################################################
[+] Saving results to Pastebin_test1@test.local_02-06-2019-10-54-34.csv..
[+] Checking test2@test.local for possible pastes..
[!] Email account found on Pastebin
[+] Listing Pastebins..
Pastebin number: 1
###########################################################
Title        | pxahb.xyz
Source       | AdHocUrl
Email Count  | 1695
ID           | http://pxahb.xyz/emailpass/www.naamyoga.com.txt
Date         | None
###########################################################
[+] Saving results to Pastebin_test2@test.local_02-06-2019-10-54-37.csv..
10:54:38 root@kali Pwned 
```

## Contributing
Pull request are always welcome.

## License
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
