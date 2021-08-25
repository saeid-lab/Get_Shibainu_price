from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess
import time


def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

url = "https://coinmarketcap.com/currencies/shiba-inu/"

while 1>0:
    soup  = BeautifulSoup(urlopen(url), 'html.parser')
    value = soup.find('div', {'class':'priceValue smallerPrice'}).contents
    sendmessage(value[0])
    time.sleep(900)
