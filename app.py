from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        dados = {
            'mensagem': 'Olá do Python Flask!',
            'hora': datetime.now().strftime('%H:%M:%S')
        }
        return render_template('index.html', **dados)
    except Exception as e:
        return f"Erro ao renderizar template: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)