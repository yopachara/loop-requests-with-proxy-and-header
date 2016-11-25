import requests
import random
import time
import logging

def LoadUserAgents(uafile):
    """
    uafile : string
        path to text file of user agents, one per line
    """
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1-1])
    random.shuffle(uas)
    return uas

    # load the user agents, in random order

def LoadProxy():
    return (random.choice(list(open("http_proxyhttp.txt"))))[:-1]

def main():
    i = 0
    while True:
        try:

            print "Loop count : "+str(i)
            url = 'https://app.viralsweep.com/rin/5894/186969'
            proxy = {"http": "http://"+LoadProxy()}
            print proxy
            # load user agents and set headers
            uas = LoadUserAgents(uafile="user_agents.txt")
            ua = random.choice(uas)  # select a random user agent
            headers = {
            "Connection" : "close",  # another way to cover tracks
            "User-Agent" : ua}
            print headers
            r = requests.get(url,proxies=proxy,headers=headers )
            print r
            time.sleep(1)
            i = i + 1
        except requests.exceptions.HTTPError as err:
            print err
            sys.exit(1)

logging.basicConfig(level=logging.DEBUG)
main()



