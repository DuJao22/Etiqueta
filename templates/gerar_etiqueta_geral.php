<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" >
    <title>Gerador de Etiquetas | 3D Lab</title>
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
                height: 22,
                fontSize: 8,
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
                size: A4 landscape;
                margin: 5;
            }

            body {
                margin: 0;
                padding: 1;
                -webkit-print-color-adjust: exact;
            }
        }

        .container {
            display: flex;
            justify-content: space-around;
            align-items: center;
            height: 90vh;
            width: 125%;
            
        }

        .etiqueta {
            width: 900px; /* Alterada a largura para 230px */
            height: 200px;
            transform: rotate(-90deg);
            position: center;
        }

        .etiqueta2 {
            width: 900px; /* Alterada a largura para 220px */
            height: 240px;
            transform: rotate(-90deg);
        }

        .barcode {
            display: inline-block;
            width: 100%;
            height: 50%;
        }
    </style>
</head>
<body onload="ClosePrint()">
<div class="container">
    <div class="etiqueta">
        <center>
            <p></p>
            <span style="font-family:arial;font-size:15px;"><strong>{{ produto.material }}</strong></span><br/>
            <span style="font-family:arial;font-size:15px;"><strong>{{ produto.cor }}</strong></span><br/>
            <span style="font-family:arial;font-size:14px;text-transform:uppercase;">{{ produto.descricao }}</span>
            <svg class="barcode">
            </svg>
            <span style="font-family:arial;font-size:13px;"><strong>{{ produto.codigo }}</strong></span>
        </center>
    </div>
    <div class="etiqueta2">
        <center>
            
            <span style="font-family:arial;font-size:15px;"><strong>{{ produto.material }}</strong></span><br/>
            <span style="font-family:arial;font-size:15px;"><strong>{{ produto.cor }}</strong></span><br/>
            <span style="font-family:arial;font-size:14px;text-transform:uppercase;">{{ produto.descricao }}</span><br/>
            <span style="font-family:arial;font-size:17px;text-transform:uppercase;"><small>{{ produto.informacoes_adicionais }}</small></span>
        </center>
    </div>
</div>
</body>
</html>
