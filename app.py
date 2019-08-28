from flask import Flask
import sys
import numpy

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


@app.route('/start')
def start():
    # for item in productMap['iphoneXs']['Excellent']:
    #     print(item)
    list = numpy.stack(productMap['iphoneXs']['Excellent'], axis=0)
    return 'Hello World!'


productMap = {
    'iphoneXs': {
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
