from flask import Flask, render_template, request, redirect, url_for,flash,jsonify
from datetime import datetime
from skus import Sku
from Link_material import Link_material
import qrcode
import os 
from lote import data_para_letras

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]



data = datetime.now().strftime('%d-%m-%Y')
letra_mes = ['','A','B','C','D','E','F','G','H','I','J','K','L']
mes_name = ['',"JAN",'FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']
mostra_pd = {}
user = ''

productions = {}
registro_pd = {}
app = Flask(__name__)
app.secret_key = "SJBJOAOLAYONADA"
Meta = 1600
contagem_produzida = []
contagem_perda = []
contagem_low = []
testes = {}
produta = {}
###############################################

@app.route('/executar_automacao', methods=['POST'])
def executar_automacao():
    # Exemplo de automação com PyAutoGUI
    print("automacao")
    return jsonify({"status": "Automação executada com sucesso"})



def generate_qr_code(data, filename="qrcode.png"):
    # Gera o QR code com os dados fornecidos
    qr = qrcode.make(data)
    
    # Define o diretório e o caminho do arquivo para salvar o QR code
    save_path = os.path.join("static", "qrcodes")
    os.makedirs(save_path, exist_ok=True)
    file_path = os.path.join(save_path, filename)
    
    # Salva a imagem do QR code
    qr.save(file_path)
    return file_path

@app.route('/excluir_sku',methods=["POST","GET"])
def excluir_sku():
    inf_sku = request.form["skuInput"]
    if inf_sku in Sku:
        apagado = Sku[inf_sku]
        del Sku[inf_sku]
    else:
        return "nao existe o sku"
    return render_template("apagar_sku.html",sku=apagado,id = inf_sku)

@app.route('/login_sku_apagar',methods=["POST","GET"])
def login_sku_apagar():
    return render_template("login_sku_apagar.html",Sku=Sku)



@app.route("/verificar_chave_apagar", methods=["POST","GET"])
def verificar_chave_apagar():
    chave = request.form["chave"]
    if chave == "senha123":
        return render_template("apagar_sku.html")
    else:
        return "Acesso negado fdp"

@app.route("/apagar_sku",methods=["POST","GET"])
def apagar_sku():
    return render_template("apagar_sku.html")





@app.route("/verificar_chave_cliever", methods=["POST","GET"])
def verificar_chave_cliever():
    chave = request.form["chave"]
    if chave == "senha123":
        return render_template("gerar_sku_cliever.html")
    else:
        return "Acesso negado fdp"

    
@app.route("/gravar_sku",methods=["GET","POST"])
def grava_sku():
    sku = request.form["sku"]
    material = request.form["material"]
    cor = request.form["cor"]
    diametro = request.form["diametro"]
    peso = request.form["peso"]
    base = request.form["base"]
    bico = request.form["bico"]
    link = request.form["link"]
    
    info = f'Bico:{bico} Base:{base}'
    
    novo = {sku:[material,cor,diametro,peso,info,link,bico,base]}

    Sku.update(novo)

    txt = open("Skus.py","w",encoding='utf-8')
    txt.write(f"# -*- coding: utf-8 -*-\nSku = {Sku}")
    txt.close()
    return render_template("gerar_sku.html")

@app.route("/verificar_chave", methods=["POST","GET"])
def verificar_chave():
    chave = request.form["chave"]
    if chave == "senha123":
        return render_template("gerar_sku.html")
    else:
        return "Acesso negado"

@app.route('/login_sku',methods=["POST","GET"])
def login_sku():
    return render_template("login_sku.html")



@app.route('/buscar', methods=['GET', 'POST'])
def etiqueta_geral():
    resultados = []
    if request.method == 'POST':
        termo_busca = request.form['termo_busca']
        resultados = buscar(termo_busca)
    return render_template('etiquetas_3d.html', resultados=resultados)

def buscar(termo):
    resultados = []
    for sku, dados in Sku.items():
        if termo.lower() in str(sku) or termo.lower() in ' '.join(map(str, dados)).lower():
            resultados.append((sku, dados))
    return resultados

@app.route("/",methods=["POST","GET"])
def etiquetas():
    return render_template("etiquetas_3d.html")


@app.route('/selecao_etiqueta_carretel',methods=["POST",'GET'])
def selecao_etiqueta_carretel():
    return render_template("gerar_etiqueta.php",produto=produto)

diametro = ""
peso = ""

@app.route('/selecao_etiqueta_caixa',methods=["POST",'GET'])
def selecao_etiqueta_caixa():
    qr_path = generate_qr_code(produto['link'])
    
    return render_template("gerar_etiqueta_caixa.php",qr_path=qr_path,produto=produto, diametro=diametro,peso =peso)

@app.route('/gerador',methods=["POST","GET"])
def gerador():
    sku = request.form["SKU"]
    op = request.form["LOTE"]
    lote2 = data_para_letras(data,op)
    print(sku,Sku)
    global diametro , peso
    if sku in Sku:
        material = Sku[sku][0]
        cor = Sku[sku][1]
        diametro = Sku[sku][2]
        peso = Sku[sku][3]
        descricao = f"{peso} / {diametro} MM / {lote2}"
        info = Sku[sku][4]
        global produto
        link = Sku[sku][5]
        bico = Sku[sku][6]
        base = Sku[sku][7]
        print(link)
        produto = {
            'material': material.upper(),
            "cor" : cor.upper(),
            'descricao': descricao,
            'informacoes_adicionais': info,
            'codigo': sku,
            "link": link,
            "diametro":diametro,
            "peso":peso,
            "bico":bico,
            "base":base
        }
        
        return render_template("selecionar.html")
    else :
        return "não existe o sku"


if __name__ == '__main__':
    print("Sistema online ")
    import time
    
    app.run(debug=True,host='0.0.0.0',port=5000)
