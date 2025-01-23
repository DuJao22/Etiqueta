<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport">
    <title>Gerador de Etiquetas | TRIADE 3D</title>
    <script src="https://cdn.jsdelivr.net/npm/jsbarcode@3.11.0/dist/JsBarcode.all.min.js"></script>
    <script>
        function ClosePrint() {
            setTimeout(function () { window.print(); }, 700);
        }

        // Função para gerar o código de barras
        function generateBarcode() {
            JsBarcode(".barcode", "{{ produto.codigo }}", {
                format: "CODE128",
                displayValue: false,
                height: 13,
                fontSize: 10,
                margin: 0,
                fontOptions: "bold"
            });
        }

        // Chamar a função quando o documento estiver pronto
        document.addEventListener("DOMContentLoaded", function () {
            generateBarcode();
        });
    </script>
    <style>
        @media print {
            @page {
                size: 40mm 25mm; /* Define o tamanho da etiqueta */
                margin: 0;
            }

            body {
                margin: 0;
                padding: 0;
                -webkit-print-color-adjust: exact;
            }
        }

        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
            width: 100%;
        }

        .etiqueta {
            width: 40mm;
            height: 25mm;
            box-sizing: border-box;
            text-align: center;
            font-family: Arial, sans-serif;
            font-size: 8px;
        }

        .etiqueta2 {
            width: 40mm;
            height: 25mm;
            text-align: center;
            font-family: Arial, sans-serif;
            font-size: 6px;
        }

        p {
            padding: 10px;
        }

        .barcode {
            width: 100%;
            height: 15px; /* Ajuste da altura */
            margin: 0; /* Remove espaçamentos */
        }
        
        /* Remover padding adicional */
        .etiqueta2 span {
            display: block;
            margin: 0;
            padding: 0;
        }
    </style>
</head>
<body onload="ClosePrint()">
<div class="container">
    <div class="etiqueta">
        <strong style="font-size: 9pt;">{{ produto.material }}</strong><br/>
        <strong style="font-size: 9pt;">{{ produto.cor }}</strong><br/>
        <span style="font-size: 8pt;">{{ produto.descricao }}</span><br/>
        <small style="font-size: 7pt;">{{ produto.informacoes_adicionais }}</small>
    </div>
    <p></p>
    <div class="etiqueta2">
        <span style="font-family: arial; font-size: 15px;"><strong>{{ produto.material }}</strong></span>
        <span style="font-family: arial; font-size: 11px;"><strong>{{ produto.cor }}</strong></span>
        <span style="font-size: 10px">{{ produto.descricao }}</span>
        <svg class="barcode"></svg>
        <span style="font-family: arial; font-size: 13px;"><strong>{{ produto.codigo }}</strong></span>    
    </div>
</div>
</body>
</html>
