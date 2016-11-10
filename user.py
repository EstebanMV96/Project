from flask import Flask, abort
app = Flask(__name__)

api_url = '/v1.0'
from flask import Flask, abort, request
import json

from usercommands import get_list,create_archive,delete_archs,recently_archs

app = Flask(__name__)
api_url = '/v1.0'

@app.route(api_url+'/files',methods=['GET'])
def get_arch():
	list = {}
  	list["Files"] = get_list()
  	return json.dumps(list), 200

@app.route(api_url+'/files',methods=['POST'])
def create_arch():
  conten = request.get_json(silent=True)
  filename = conten['filename']
  content = conten['content']
  if(create_archive(filename,content)):
    print filename
    print content
    return "CREATED" , 201
  else:
    return "error while creating file", 400

@app.route(api_url+'/files',methods=['DELETE'])
def delete_arch():
  error = False
  for filename in get_list():
    if not delete_archs(filename):
        error = True

  if error:
    return 'NO_PUDO', 400
  else:
    return 'PUDO', 200

@app.route(api_url+'/files',methods=['PUT'])
def update_files():
  return "not found", 404

@app.route(api_url+'/files/recently_created',methods=['GET'])
def recently_crea():
  list = {}
  list["Files"] = recently_archs()
  return json.dumps(list),200
  #return recently_archs()

		 
if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8088,debug='True')
