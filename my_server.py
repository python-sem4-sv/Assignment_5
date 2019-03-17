from flask import Flask, request, make_response
import simplejson as json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    client_password = json.loads(request.get_json())['password']
    if client_password == 'az':
        print(client_password)
        response = make_response('', 200)
        return response
    response = make_response('', 403)
    return response
