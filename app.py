from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/start', methods=['POST'])
def start_adventure():
    return jsonify()

@app.route('/choose', methods=['POST'])
def choose_path():
    data = request.json
    choice = data.get('choice')
    return jsonify()

if __name__ == "__main__":
    app.run(debug=True)

#PENDING:
#1. Implementar GameService._get_first_adventure()
    #1.1 Implementar adventureService
    #1.2 Implementar adventureRepository
    #1.3 Integrar BDD SQLLite
#2. Implementar capa controller (con manejo de errores personalizado para poder cambiar de tipo de error)
#3. Documentar
#4. Implementar tests unitarios
#5. Implementar tests de integracion
#6. Formatear codigo con black
#7. Dockerizar