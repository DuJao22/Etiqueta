def data_para_letras(data, operador):
    # Assume que a data está no formato DD-MM-YYYY
    dia, mes, ano = data.split('-')
    
    # Pega os dois últimos dígitos do ano
    ano = ano[2:]
    
    # Formata o retorno no estilo "YYMMDD" seguido do operador
    retorno = f"{ano}{mes}{dia}{operador}"
    
    return retorno
