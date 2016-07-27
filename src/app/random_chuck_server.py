import argparse
import json
import logging
import random
import sys
import traceback

from chucklib.quotes import quote_chuck_norris
from flask import Flask
from flask import render_template
from os import listdir


logging.basicConfig(stream=sys.stdout,
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    handlers=[logging.StreamHandler()])

# logging.basicConfig(filename='log/chuck.log',
#                     level=logging.INFO,
#                     format='%(asctime)s %(levelname)s %(message)s',
#                     handlers=[logging.StreamHandler()])

# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(message)s'))

# add the handler to the root logger
logging.getLogger('').addHandler(console)
logger = logging.getLogger(__name__)

app = Flask(__name__)


def get_random_background():
    return "background-{0}".format(
        random.randrange(len(listdir("static/chuckpics"))) + 1)


@app.route("/api")
def api():
    try:
        logger.info("Another API request for an awesome quote has been made!")
        return json.dumps({"quote": unicode(quote_chuck_norris())}), 200
    except:
        logger.error(traceback.format_exc())
        return json.dumps(
            {"error": "Sorry, something bad happened with your request."}), 500


@app.route("/")
def main():
    try:
        logger.info("Another WEB request for an awesome quote has been made!")
        return render_template('index.html',
                               quote=unicode(quote_chuck_norris()),
                               background=get_random_background())
    except:
        logger.error(traceback.format_exc())
        return json.dumps(
            {"error": "Sorry, something bad happened with your request."}), 500


class ChuckParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: {0}\n'.format(message))
        self.print_help()
        sys.exit(2)


if __name__ == '__main__':
    try:
        parser = ChuckParser()
        parser.add_argument("--host",
                            default="127.0.0.1",
                            help="IP to run on [default: 127.0.0.1]")
        parser.add_argument("--port",
                            default=9090,
                            type=int,
                            help="port to listen to [default: 9090")
        args = parser.parse_args()

        app.run(host=args.host, port=args.port)

    except SystemExit:
        logger.info("Farewell!")
    except:
        logger.error(traceback.format_exc())
