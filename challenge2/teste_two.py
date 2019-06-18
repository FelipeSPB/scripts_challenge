
carteiras = [
            {'numero':1,'ativo': True,'bilhete':10},
            {'numero':2,'ativo': False,'bilhete':0},
            {'numero':3,'ativo': True,'bilhete':12},
            {'numero':4,'ativo': False,'bilhete':0},
            {'numero':5,'ativo': True,'bilhete':14},
            {'numero':6,'ativo': True,'bilhete':15}
            ]



def atualiza_socios(lista_socios):
    carteiras_output = list()
    valores_carteira = list()
    carteiras_nova = list()
    for i in carteiras: 
        valores_carteira.append([i['numero'], i['ativo'] ,i['bilhete']]) 
    for lista in lista_socios:
        carteiras_output.append([lista[0],True,lista[1]])
    for i in range(0,len(valores_carteira)):
        for vetor in carteiras_output:
            if valores_carteira[i][0] == vetor[0]:
                valores_carteira[i] = vetor
    for i in carteiras_output:
        if i not in valores_carteira:
            valores_carteira.append(i)
    for i in range (0,len(valores_carteira)):
        valor_index = valores_carteira[i]
        if valor_index not in carteiras_output:
            valores_carteira[i][1] = False
            valores_carteira[i][2] = 0
    for i in valores_carteira:
        carteiras_nova.append({'numero':i[0],'ativo':i[1],'bilhete':i[2]})
    print(carteiras_nova)
    return carteiras_nova
atualiza_socios([(1,16),(4,13),(5,15),(8,18),(9,19)])
