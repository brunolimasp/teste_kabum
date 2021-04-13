from flask import jsonify
from decimal import Decimal


class Calculo_frete:
  def __init__(self,altura,largura,peso):

    self.altura = altura
    self.largura = largura
    self.peso = peso

  def fretes(self):

    frete_list = []

    if((self.altura >= 10) and (self.altura <= 200) and (self.largura >= 6) and (self.largura <= 140)):
      

      frete_list.append ({
        "nome":"Entrega Ninja",
    	  "valor_frete": format((self.peso * 0.3)/(10), '.2f'),
    	  "prazo_dias": 6
	      })

    else:
      pass
# ----------------------------------------------------------------------------------------------
    if((self.altura >= 5) and (self.altura <= 140) and (self.largura >= 13) and (self.largura <= 125)):
      

      frete_list.append ({
        "nome":"Entrega Kabum",
    	  "valor_frete": 12.00,
    	  "prazo_dias": 6
	      })

    else:
      pass
      
    return jsonify(frete_list)
    
  def frete(self):


    return self.fretes()