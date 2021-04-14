from flask import jsonify


class Calculo_frete:


  def __init__(self,altura,largura,peso):

    self.altura = altura
    self.largura = largura
    self.peso = peso

  def fretes(self):
# --------------------------------LISTA DE FRETES------------------------------------
    frete_list = []
# -----------------------------------Ninja-------------------------------------------
    if((self.altura >= 10) and 
      (self.altura <= 200) and 
      (self.largura >= 6) and 
      (self.largura <= 140) and 
      (self.peso > 0)):
      
      frete_list.append ({
        "nome":"Entrega Ninja",
    	  "valor_frete": format((self.peso * 0.3)/(10), '.2f'),
    	  "prazo_dias": 6
	      })

    else:
      pass
# ---------------------------------KaBuM---------------------------------------------
    if((self.altura >= 5) and 
      (self.altura <= 140) and 
      (self.largura >= 13) and 
      (self.largura <= 125) and 
      (self.peso > 0)):
      
      frete_list.append ({
        "nome":"Entrega KaBuM",
    	  "valor_frete": format((self.peso * 0.2)/(10), '.2f'),
    	  "prazo_dias": 6
	      })

    else:
      pass
      
    return jsonify(frete_list)

  def frete(self):

    return self.fretes()