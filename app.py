from flask import Flask
import sys
import numpy
from itertools import product
import webbrowser

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

globalData = {}


@app.route('/start')
def start():
    product = 'iphoneXS'
    conditon = 'Excellent'
    result = getParams(product, conditon)
    for params in result:
        # MacOS
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        globalData[params.__str__()] = {}
        # Windows
        # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        # Linux
        # chrome_path = '/usr/bin/google-chrome %s'

        webbrowser.get(chrome_path).open(productMap[product]['url'] + '&params=' + params.__str__())

    return globalData.__str__()


def getParams(product, conditon):
    result = []
    for item0 in productMap[product][conditon][0]:
        for item1 in productMap[product][conditon][1]:
            for item2 in productMap[product][conditon][2]:
                for item3 in productMap[product][conditon][3]:
                    for item4 in productMap[product][conditon][4]:
                        for item5 in productMap[product][conditon][5]:
                            for item6 in productMap[product][conditon][6]:
                                for item7 in productMap[product][conditon][7]:
                                    for item8 in productMap[product][conditon][8]:
                                        for item9 in productMap[product][conditon][9]:
                                            for item10 in productMap[product][conditon][10]:
                                                result.append(
                                                    [item0, item1, item2, item3, item4, item5, item6, item7, item8,
                                                     item9, item10])
    return result


productMap = {
    'iphoneXS': {
        'url': 'https://huishou.paipai.com/detail?pid=174921',
        'Excellent': [[7399], [7396, 3987, 2023], [2014], [2452, 2902, 2903], [2072], [2026], [2100], [2125], [2118],
                      [2114], [2067]],
        'Good': [[7399], [7396, 3987, 2023], [2014], [2452, 2902, 2903], [2072], [2026], [2100], [2125, 2126],
                 [2118, 2120], [2114, 2115], [2067]],
        'Poor': [[7399], [7396, 3987, 2023], [2014], [2452, 2902, 2903], [2072], [2026], [2100], [2126, 2128],
                 [2120, 3098], [2115, 8565, 2475], [2067]],
        'Broken': [[7399], [7396, 3987, 2023], [2014], [2452, 2902, 2903], [2072], [2026], [2100], [6873], [2122],
                   [3304], [2067]],
    }
}
