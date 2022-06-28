from contextlib import nullcontext
from flask import Flask, render_template
from flask import request
from requests import NullHandler
import main

app = Flask(__name__)

#rota principal
@app.route('/')
def index():
	return render_template('index.html')

#rota de requisição
@app.route('/autenticar', methods=['GET'])
def antenticar():
	
	#agora só precisamos chamar a API e consumir seus dados a partir 
	#da variável city
	city = request.args.get('city')
	

	teste = main.func_meteorologia(city)
	return teste[0]
app.run(debug=True)
