from flask_restful import Resource, reqparse
import mysql.connector

class Cadastro(Resource):
    
    def post(self):

        argumentos = reqparse.RequestParser()
        argumentos.add_argument("username", type=str, required=True, help="O campo 'username' deve ser informado!")
        argumentos.add_argument("firstName", type = str, required = True, help= "O campo 'firstName' deve ser informado!")
        argumentos.add_argument("lastName", type = str, required = True, help= "O campo 'lastName' deve ser informado!")
        argumentos.add_argument("email", type = str, required = True, help= "O campo 'email' deve ser informado!")
        argumentos.add_argument("password", type = str, required = True, help= "O campo 'password' deve ser informado!")
        argumentos.add_argument("phone", type = str, required = True, help= "O campo 'phone' deve ser informado!")
        argumentos.add_argument("userStatus", type = str, required = True, help= "O campo 'userStatus' deve ser informado!")        
        args = argumentos.parse_args()

        conexao = mysql.connector.connect(
            host = "",
            user = "",
            password = "",
            database = ""
        )