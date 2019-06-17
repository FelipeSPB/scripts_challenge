def atualiza_socios(lista_socios):
    carteiras_output = []
    for lista in lista_socios:
        carteiras_output.append({'numero':lista[0],'ativo': True,'bilhete':lista[1]})
    print(carteiras_output)
    