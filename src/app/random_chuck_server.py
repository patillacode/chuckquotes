import argparse
import logging
import json
import sys
import traceback

from flask import Flask
from chucklib.quotes import quote_chuck_norris

logging.basicConfig(filename='log/chuck.log',
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    handlers=[logging.StreamHandler()])

# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(message)s'))

# add the handler to the root logger
logging.getLogger('').addHandler(console)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def main():
    try:
        logger.info("Another request for an awesome quote has been made!")
        return json.dumps({"quote": unicode(quote_chuck_norris())}), 200
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
                            default=8080,
                            type=int,
                            help="port to listen to [default: 8080")
        args = parser.parse_args()

        app.run(host=args.host, port=args.port)

    except SystemExit:
        logger.info("Farewell!")
    except:
        logger.error(traceback.format_exc())
