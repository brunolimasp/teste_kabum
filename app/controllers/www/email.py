
from app import *
from flask import render_template, session, redirect, request, g, jsonify, session



#------Recuperação de senha-------------------

@app.route('/enviar_email', methods=['POST'])
def enviar_email():

  dados = g.user
  usuario_email = g.user[0]
  whatsapp = g.user[1]

  id_anuncio = str(request.form['id_anuncio'])
  assunto = str(request.form['assunto'])
  mensagem = (request.form['mensagem'])

  cursor = mysql.connection.cursor()
  cursor.execute(f"SELECT Usuarios.id_email, Usuarios.whatsapp, Classificados.whatsapp, Classificados.id_anuncio FROM Usuarios JOIN Classificados ON Usuarios.whatsapp = Classificados.whatsapp WHERE Classificados.id_anuncio = {id_anuncio};")
  email = cursor.fetchone()

  email = email[0]

    
  try:

    msg = Message( 
                assunto, 
                sender ='feiradoroloonline@bbreno.com.br', 
                recipients = [email, usuario_email]
                ) 
    msg.body = (mensagem)
    mail.send(msg)

  except:
    pass

  return render_template('index/index.html', alerta=f'Sua senha foi enviada para {email}', classificado=None, dados=None)

