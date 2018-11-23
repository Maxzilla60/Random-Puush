# Random Puush
Opens a (or multiple) random public [Puush.me](http://puush.me) screenshots!
Just because...

## What?
This script generates random Puush URLs and checks if they are viewable/public images and then automatically opens them in the browser

## How?
* Get yourself [Python 3](https://www.python.org/downloads/)
* Run the script (see **"Usage"**)
* Check out the randomness!

## Usage
```
usage: rand_puush.py [-h] [-a AMOUNT] [-th THREADCOUNT] [-s] [-e] [-no]

optional arguments:
  -h, --help                                    show this help message and exit
  -a AMOUNT, --amount AMOUNT                    amount of Puush links to find, default is 1
  -th THREADCOUNT, --threadcount THREADCOUNT    amount of threads to use, default is 10
  -s, --output-urls-only                        print out only the found links, default is False
  -e, --endless                                 enable endless mode, opening links as it finds them,
                                                default is False
  -no, --no-auto-open                           disable automatically opening found links in browser,
                                                default is False
```