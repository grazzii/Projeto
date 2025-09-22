from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# URL do backend - no Docker Compose usaremos o nome do serviço
BACKEND_URL = os.getenv('BACKEND_URL', 'http://backend:25000')

@app.route('/')
def index():
    try:
        # Tenta buscar dados do backend
        response = requests.get(f"{BACKEND_URL}/api/data", timeout=5)
        data = response.json() if response.status_code == 200 else {
            'message': 'Backend não disponível',
            'status': 'error'
        }
    except requests.exceptions.RequestException as e:
        data = {
            'message': f'Erro ao conectar com o backend: {str(e)}',
            'status': 'error'
        }
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)