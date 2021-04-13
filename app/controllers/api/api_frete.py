from app import *
from app.controllers.api.calculo import Calculo_frete




@app.route("/api/frete", methods=['POST'])
def api_frete():

  # COLEÇÂO DE DADOS
  data = request.get_json()

  dimensao = data['dimensao']
  altura = float(dimensao['altura'])
  largura = float(dimensao['largura'])
  peso = float(data['peso'])

  resultado = Calculo_frete(altura,largura,peso).frete()

  return (resultado)