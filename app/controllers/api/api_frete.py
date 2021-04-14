from app import *
from app.controllers.api.calculo import Calculo_frete




@app.route("/api/frete", methods=['POST'])
def api_frete():

  # COLEÇÂO DE DADOS
  data = request.get_json()

  dimensao = data['dimensao']
  altura = dimensao['altura']
  largura = dimensao['largura']
  peso = data['peso']

  resultado = Calculo_frete(altura,largura,peso).frete()

  return (resultado)