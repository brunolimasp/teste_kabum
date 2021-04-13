
from app import *





@app.route('/api', methods=['POST'])
@cross_origin()
def api():

        data = request.get_json()
        print (data)

        email = data['email']

        print(email)

        return jsonify({'alert': 'alerta em json'})