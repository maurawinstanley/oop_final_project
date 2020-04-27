import time
from flask import Flask, request, jsonify
import logging 
import sys

sys.path.insert(1, '/Users/abbir/Desktop/School/Classes/sp20/ooad/projects/')

from oop_final_project import client
logger = logging.getLogger()
app = Flask(__name__)


@app.route('/result', methods = ['GET'])
def result():
    
    if request.method == 'GET':
        
        url = request.args.get('url', None)
        
       
        client_obj = client.Client(url)
        response = client_obj.to_worker()
        
        return jsonify(str(response))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')









