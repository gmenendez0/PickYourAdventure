from flask import Flask
from controllers.GameController import game_bp

app = Flask(__name__)

app.register_blueprint(game_bp, url_prefix = '/game')

if __name__ == "__main__":
    app.run(debug=True)

#PENDING:
#3. Documentar
#4. Implementar tests unitarios
#5. Implementar tests de integracion
#6. Formatear codigo con black
#7. Dockerizar