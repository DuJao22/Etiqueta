<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Etiqueta de Filamento</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 50mm;
            height: 70mm;
            border: 1px solid #000;
            padding: 2mm;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
        }

        /* Estilo do título no fundo vermelho */
        .material {
            background-color: #d32f2f;
            color: white;
            text-align: center;
            padding: 2mm 0;
            font-size: 14pt;
            font-weight: bold;
            border: 2px solid black;
            margin-bottom: 2mm;
        }

        /* Caixa de informações preta com texto e QR code */
        .info-wrapper {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .info-material {
            background-color: black;
            color: white;
            padding: 2mm;
            height:90%;
            font-size: 8pt;
            font-weight: bold;
            margin-bottom: 2mm;
            width: 65%; /* Largura total da div */
            box-sizing: border-box;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        /* Estilo para o QR code */
        
    /* Estilo para o QR code com borda */
        .qr-code {
            background-color: white;
            padding: 1mm;
            width: 20mm;
            height: 20mm;
            text-align: center;
            border: 1px solid black; /* Adiciona a borda */
            box-sizing: border-box;
        }


        /* Texto ao lado do QR code */
        .text-info {
            padding-left: 2mm;
            text-align: left;
            color: white;
            font-size:8px;
        }

        /* Peso (1kg) e Tamanho do Filamento (2.85mm) */
        .weight-box {
            background-color: white;
            border: 1px solid black;
            padding: 1mm;
            font-size: 6px;
            font-weight: bold;
            text-align: center;
            width: 15mm;
            height: 10mm;
            box-sizing: border-box;
        }

        .filament-size {
            background-color: white;
            border: 1px solid black;
            padding: 2mm;
            font-size: 9px;
            font-weight: bold;
            text-align: center;
            width: 15mm;
            height: 7mm;
            box-sizing: border-box;
        }

        /* Código de Barras */
        .barcode-section {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2mm;
        }

        .barcode {
            width: 100%; /* Ajuste da largura do código de barras */
        }

        .barcode img {
            width: 100%;
            height: auto;
            position: center;
        }

        /* Contêiner para agrupar o código de barras e o número */
        .barcode-container {
            display: flex;
            flex-direction: column;
            align-items: center; /* Centraliza o número abaixo do código de barras */
            width: 60%; /* Ajusta a largura do contêiner */
        }

        /* Wrapper para agrupar os quadros "1kg" e "ISO 9001" em coluna */
        .side-box-wrapper {
            display: flex;
            flex-direction: column; /* Exibe os itens na vertical */
            justify-content: space-between;
            height: 100%; /* Para ocupar o espaço disponível */
        }

        .side-box {
            background-color: white;
            border: 1px solid black;
            padding: 2mm;
            font-size: 9px;
            font-weight: bold;
            text-align: center;
            width: 15mm;
            
            box-sizing: border-box;
        }

        .side-box2 {
            background-color: white;
            border: 1px solid black;
            padding: 2mm;
            font-size: 6px;
            font-weight: bold;
            text-align: center;
            width: 15mm;
            
            box-sizing: border-box;
        }

        /* Alinhamento do número do código de barras */
        .barcode-number {
            text-align: center;
            font-size: 8pt;
        }

        /* ISO 9001 */
        .iso {
            text-align: center;
            font-size: 8pt;
            margin-top: 2mm;
        }

        p {
            padding: 3px;
        }

        .info-wrapper {
            display: flex;
            justify-content: space-between;
            align-items: stretch;
        }

        .info-material {
            background-color: black;
            color: white;
            
            height: 100%;
            font-size: 8pt;
            font-weight: bold;
            padding: 1mm;
            width: 65%;
            box-sizing: border-box;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .filament-size, .weight-box {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            
            font-size: 8px;
            font-weight: bold;
            background-color: white;
            border: 1px solid black;
            width: 17mm; /* Ajuste conforme necessário */
            height: auto; /* Ajuste conforme necessário */
            box-sizing: border-box;
        }
        .etiquetas-wrapper {
            display: flex;
            gap: 10px; /* Espaçamento entre as etiquetas, ajuste conforme necessário */
            justify-content: space-between; /* Distribui as etiquetas igualmente, se houver mais espaço */
            align-items: flex-start; /* Alinha as etiquetas no topo */
        }

        .container {
            width: 50mm;
            height: 70mm;
            border: 1px solid #000;
            padding: 2mm;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
        }


    </style>
</head>
<body onload="generateBarcode(); window.print();">

<div class="etiquetas-wrapper">
        <!-- Primeira etiqueta -->
        <div class="container">
            <!-- Conteúdo da primeira etiqueta -->
            <div class="material">{{produto.material}}</div>
            <div class="info-wrapper">
                <div class="info-material">
                    <img src="{{ qr_path }}" alt="QR Code" width="50%">
                    <div class="text-info">{{produto.cor}}</div>
                </div>
                <div>
                    <div class="filament-size">{{produto.diametro}}MM</div>
                    <div class="weight-box">BICO : <br> {{produto.bico}} <br> MESA : <br> {{produto.base}}</div>
                </div>
            </div>
            <div class="barcode-section">
                <div class="barcode-container">
                    <svg class="barcode"></svg>
                    <div class="barcode-number">{{produto.codigo}}</div>
                </div>
                <div class="side-box-wrapper">
                    <div class="side-box">{{produto.peso}}</div>
                    <div class="side-box2">Carretel vazio <br> 270g</div>
                </div>
            </div>
        </div>

        <!-- Segunda etiqueta (duplicada) -->
        <div class="container">
            <!-- Conteúdo da segunda etiqueta -->
            <div class="material">{{produto.material}}</div>
            <div class="info-wrapper">
                <div class="info-material">
                    <img src="{{ qr_path }}" alt="QR Code" width="50%">
                    <div class="text-info">{{produto.cor}}</div>
                </div>
                <div>
                    <div class="filament-size">{{produto.diametro}}MM</div>
                    <div class="weight-box">BICO : <br> {{produto.bico}} <br> MESA : <br> {{produto.base}}</div>
                </div>
            </div>
            <div class="barcode-section">
                <div class="barcode-container">
                    <svg class="barcode"></svg>
                    <div class="barcode-number">{{produto.codigo}}</div>
                </div>
                <div class="side-box-wrapper">
                    <div class="side-box">{{produto.peso}}</div>
                    <div class="side-box2">Carretel vazio <br> 270g</div>
                </div>
            </div>
        </div>
    </div>


<!-- Incluindo JsBarcode (biblioteca necessária) -->
<script src="https://cdn.jsdelivr.net/npm/jsbarcode@3.11.0/dist/JsBarcode.all.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>

<!-- Função para gerar o código de barras -->
<script>
    function generateBarcode() {
        JsBarcode(".barcode", "{{ produto.codigo }}", {
            format: "CODE128",
            displayValue: false,
            height: 45,
            fontSize: 10,
            margin: 0,
            fontOptions: "bold"
        });

        
    }
</script>

</body>
</html>
