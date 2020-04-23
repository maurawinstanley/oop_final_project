import time
from flask import Flask, request, jsonify
import logging 
import sys


# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/mauraw/Documents/oop')

from final_project import client
logger = logging.getLogger()
app = Flask(__name__)
'''app = Flask(__name__)
print(sys.path)
@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/input_url', methods=['POST'])
def classify_object():

	
	client_obj = client.Client('https://sc01.alicdn.com/kf/HTB1FM3eLXXXXXadXXXXq6xXFXXXC/teddy-bear-stuff-toys.jpg_350x350.jpg')
	
	return client_obj.to_worker()'''




@app.route('/result', methods = ['GET'])
def result():
    if request.method == 'GET':
        player_id = request.args.get('player_id', None)
        logger.debug(player_id)

        client_obj = client.Client(player_id)
        string = client_obj.to_worker()
        return jsonify(str(string))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')









