def data_para_letras(data,operador):
    # Alfabeto de A a J, onde 0 -> A, 1 -> B, ..., 9 -> J
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    # Extrai apenas os dígitos da data, ignorando os separadores
    digitos = [int(digito) for digito in data if digito.isdigit()]
    
    # Converte cada dígito para a letra correspondente no alfabeto
    letras = [alfabeto[digito] for digito in digitos]
    
    retorno = f"{''.join(letras)}{operador}"
    # Junta a lista de letras em uma única string
    return retorno


