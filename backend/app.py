from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

@app.route('/api/', methods=['GET'])
def api_root():
    return jsonify({
        'message': 'Bem-vindo à raiz da API!',
        'status': 'success'
    })
    
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        'message': 'Dados do backend funcionando!',
        'timestamp': datetime.datetime.now().isoformat(),
        'status': 'success'
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

"if __name__ == '__main__':
    "app.run(host='0.0.0.0', port=25000, debug=True)"
