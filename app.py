from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
from Link_material import Link_material
import qrcode
import os
from lote import data_para_letras
import sqlite3
import sqlitecloud

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

# Configuração do banco de dados SQLiteCloud
DATABASE = 'sqlitecloud://cd6aglqkhz.g2.sqlite.cloud:8860/banco_estiqueta.db?apikey=HMJnjaYXpCk6wFb3aaY9SGb4zw5eYEsCHInAbFyVYhc'

def get_db():
    conn = sqlitecloud.connect(DATABASE)
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS skus (
            sku TEXT PRIMARY KEY,
            material TEXT,
            cor TEXT,
            diametro TEXT,
            peso TEXT,
            info TEXT,
            link TEXT,
            bico TEXT,
            base TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS configuracoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            tamanho_texto INTEGER,
            altura_etiqueta REAL,
            comprimento_etiqueta REAL
        )
    ''')
    # Verifique e adicione as colunas faltantes, se necessário
    cursor.execute("PRAGMA table_info(configuracoes)")
    columns = [column[1] for column in cursor.fetchall()]
    if 'nome' not in columns:
        cursor.execute("ALTER TABLE configuracoes ADD COLUMN nome TEXT")
    if 'altura_etiqueta' not in columns:
        cursor.execute("ALTER TABLE configuracoes ADD COLUMN altura_etiqueta REAL")
    if 'comprimento_etiqueta' not in columns:
        cursor.execute("ALTER TABLE configuracoes ADD COLUMN comprimento_etiqueta REAL")
    conn.commit()
    conn.close()

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

@app.route('/excluir_sku', methods=["POST", "GET"])
def excluir_sku():
    inf_sku = request.form["skuInput"]
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM skus WHERE sku = ?", (inf_sku,))
    sku = cursor.fetchone()
    if sku:
        cursor.execute("DELETE FROM skus WHERE sku = ?", (inf_sku,))
        conn.commit()
        apagado = sku
    else:
        return "nao existe o sku"
    conn.close()
    return render_template("apagar_sku.html", sku=apagado, id=inf_sku)

@app.route('/login_sku_apagar', methods=["POST", "GET"])
def login_sku_apagar():
    return render_template("login_sku_apagar.html")

@app.route("/verificar_chave_apagar", methods=["POST", "GET"])
def verificar_chave_apagar():
    chave = request.form["chave"]
    if chave == "senha123":
        return render_template("apagar_sku.html")
    else:
        return "Acesso negado fdp"

@app.route("/apagar_sku", methods=["POST", "GET"])
def apagar_sku():
    return render_template("apagar_sku.html")

@app.route("/verificar_chave_cliever", methods=["POST", "GET"])
def verificar_chave_cliever():
    chave = request.form["chave"]
    if chave == "senha123":
        return render_template("gerar_sku_cliever.html")
    else:
        return "Acesso negado fdp"

@app.route("/gravar_sku", methods=["GET", "POST"])
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

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO skus (sku, material, cor, diametro, peso, info, link, bico, base)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (sku, material, cor, diametro, peso, info, link, bico, base))
    conn.commit()
    conn.close()

    return render_template("gerar_sku.html")

@app.route("/verificar_chave", methods=["POST", "GET"])
def verificar_chave():
    chave = request.form["chave"]
    if chave == "senha123":
        return render_template("gerar_sku.html")
    else:
        return "Acesso negado"

@app.route('/login_sku', methods=["POST", "GET"])
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
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT sku, material, cor, diametro, peso FROM skus WHERE sku LIKE ? OR material LIKE ? OR cor LIKE ? OR diametro LIKE ? OR peso LIKE ?', 
                   [f'%{termo}%']*5)
    rows = cursor.fetchall()
    for row in rows:
        resultados.append(row)
    conn.close()
    return resultados

@app.route("/", methods=["POST", "GET"])
def etiquetas():
    return render_template("etiquetas_3d.html")

@app.route('/selecao_etiqueta_carretel', methods=["POST", 'GET'])
def selecao_etiqueta_carretel():
    return render_template("gerar_etiqueta.php", produto=produto, altura_etiqueta=altura_etiqueta, comprimento_etiqueta=comprimento_etiqueta, tamanho_texto=tamanho_texto)

diametro = ""
peso = ""

@app.route('/selecao_etiqueta_caixa', methods=["POST", 'GET'])
def selecao_etiqueta_caixa():
    qr_path = generate_qr_code(produto['link'])
    
    return render_template("gerar_etiqueta_caixa.php", qr_path=qr_path, produto=produto, diametro=diametro, peso=peso)

@app.route('/gerador', methods=["POST", "GET"])
def gerador():
    sku = request.form["SKU"]
    op = request.form["LOTE"]
    lote2 = data_para_letras(data, op)
    print(sku)

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM skus WHERE sku = ?", (sku,))
    sku_data = cursor.fetchone()
    conn.close()

    if sku_data:
        material, cor, diametro, peso, info, link, bico, base = sku_data[1:]
        descricao = f"{peso} / {diametro} MM / {lote2}"
        global produto
        produto = {
            'material': material.upper(),
            "cor": cor.upper(),
            'descricao': descricao,
            'informacoes_adicionais': info,
            'codigo': sku,
            "link": link,
            "diametro": diametro,
            "peso": peso,
            "bico": bico,
            "base": base
        }
        
        return render_template("selecionar.html")
    else:
        return "não existe o sku"

@app.route('/configuracoes', methods=["GET", "POST"])
def configuracoes():
    if request.method == 'POST':
        nome = request.form['nome']
        tamanho_texto = request.form['tamanho_texto']
        altura_etiqueta = request.form['altura_etiqueta']
        comprimento_etiqueta = request.form['comprimento_etiqueta']

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO configuracoes (nome, tamanho_texto, altura_etiqueta, comprimento_etiqueta)
            VALUES (?, ?, ?, ?)
        ''', (nome, tamanho_texto, altura_etiqueta, comprimento_etiqueta))
        conn.commit()
        conn.close()

        flash("Configurações salvas com sucesso!")
        return redirect(url_for('configuracoes'))

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM configuracoes')
    configuracoes = cursor.fetchall()
    conn.close()

    print(configuracoes)
    
    return render_template("configuracoes.html", configuracoes=configuracoes)

@app.route('/apagar_configuracao', methods=["POST"])
def apagar_configuracao():
    config_id = request.form['config_id']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM configuracoes WHERE id = ?', (config_id,))
    conn.commit()
    conn.close()
    flash("Configuração apagada com sucesso!")
    return redirect(url_for('configuracoes'))

@app.route('/escolher_configuracao', methods=["POST"])
def escolher_configuracao():
    config_id = request.form['config_id']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM configuracoes WHERE id = ?', (config_id,))
    configuracao = cursor.fetchone()
    conn.close()
    
    # Aqui você pode definir as variáveis globais ou de sessão para a configuração escolhida
    global altura_etiqueta, comprimento_etiqueta, tamanho_texto
    altura_etiqueta = configuracao[3]
    comprimento_etiqueta = configuracao[4]
    tamanho_texto = configuracao[2]
    
    flash("Configuração escolhida com sucesso!")
    return redirect(url_for('configuracoes'))

if __name__ == '__main__':
    init_db()
    print("Sistema online ")
    import time

    app.run(debug=True, host='0.0.0.0', port=5000)