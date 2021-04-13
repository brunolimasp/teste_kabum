from flask import *


# ------------------------------ FLASK ---------------------------------
app = Flask(__name__)



@app.route("/")
def index():

  return jsonify("Hello World!")




@app.route("/frete", methods=['POST'])

def frete():

  # COLEÇÂO DE DADOS
  data = request.get_json()

  peso = data['peso']
  dimensao = data['dimensao']
  altura = dimensao['altura']
  largura = dimensao['largura']


  teste = Calculo_frete(666, 222, 33333).frete_ninja()

  return teste




class Calculo_frete:
  def __init__(self,peso,altura,largura):

    self.peso = peso
    self.altura = altura
    self.largura = largura

  def frete_ninja(self):

    return jsonify(f'{self.peso} e {self.altura}')
  
  def frete_kabum(self):
    return ('ALO')

  def frete(self):

    return jsonify(f'Tou aqui {self.peso}')













if __name__ == '__main__':
  app.run(debug=True,host='127.0.0.1', port=5000)
