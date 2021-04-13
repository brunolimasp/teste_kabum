from app import *
from app.models.rm.rm import *
from datetime import date

@app.route("/rm")
def rm():
    
    registros_rm = Rm.query.all()  

    print (registros_rm)

    return render_template ('rm/main.html', registros_rm=registros_rm)




@app.route('/cadastro_rm', methods=['POST'])
@cross_origin()
def cadastro_rm():

    data = request.get_json()
    
    categoria = data['rm_categoria']
    fk_os = data['rm_os']
    fk_user = session['email']
    rm_requisitante = data['rm_requisitante']
    departamento = data['rm_departamento']
    itens = data['lista']
    observacao = data['rm_observacao']
    status = ('Aberta')
    data = date.today()


    inserir = Rm(fk_os, fk_user, categoria, rm_requisitante, itens, status, observacao, data)
    db.session.add(inserir)
    db.session.commit()


    return jsonify({"alert": "Item registrada com sucesso!",
                    "status": 200})
    



    # try:
    #     inserir = Estoque(estoque_id, estoque_partnumber, estoque_descricao, estoque_min, estoque_max, estoque_localizacao, quantidade, registro_data)
    #     db.session.add(inserir)
    #     db.session.commit()
        
    #     return jsonify({"alert": "Item registrada com sucesso!",
    #                     "status": 200})
    # except:

    #     return jsonify({"alert": "Erro, verifique se os dados estão corretos",
    #                     "status": 401})
