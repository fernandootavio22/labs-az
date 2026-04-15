from flask import Flask
import datetime
import socket

app = Flask(__name__)

@app.route('/')
def home():
    agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    hostname = socket.gethostname()
    return f"""
    <html>
        <body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
            <h1> Lab Dockerfile - AZCORP</h1>
            <p><strong>Status:</strong> Ativo </p>
            <p><strong>Horário do Servidor:</strong> {agora}</p>
            <p><strong>ID do Container:</strong> {hostname}</p>
            <hr>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)