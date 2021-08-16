from flask import Flask
from flask_restful import Resource, Api
from clientes.cadastro import Cadastro
from clientes.alterar import Altera
from clientes.consutar import Consulta
from flask_jwt_extended import JWTManager


app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = '15asd3as5d1awe8f1as5'

#Endpoint
api.add_resource(Cadastro, '/user')
api.add_resource(Altera, '/alterar_usuario')
api.add_resource(Consulta, '/consutar_usuario')

#Configurações de inicialização, EM PRODUÇÃO O DEBUG DEVE SER IGUAL A FALSE
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=9091, debug=True)