from flask import Flask
from controllers.GameController import game_bp, GameController

app = Flask(__name__)

#Si esto empezara a crecer, deberia llevarse a otro archivo
game_controller = GameController()
game_bp.add_url_rule('/start', view_func=game_controller.start_adventure, methods=['POST'])
game_bp.add_url_rule('/choose', view_func=game_controller.choose_path, methods=['POST'])

app.register_blueprint(game_bp, url_prefix='/game')

if __name__ == "__main__":
    app.run(debug=True)


#PENDING:
#3. Documentar
#4. Implementar tests unitarios
#5. Implementar tests de integracion
#6. Formatear codigo con black
#7. Dockerizar
#8. Readme
#9. Demo