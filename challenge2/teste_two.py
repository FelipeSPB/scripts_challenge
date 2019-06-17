carteiras = [
             {'numero':1,'ativo':True,'bilhete':10},
             {'numero':2,'ativo':False,'bilhete':0},
             {'numero':3,'ativo':True,'bilhete':12},
             {'numero':4,'ativo':False,'bilhete':0},
             {'numero':5,'ativo':True,'bilhete':14},
             {'numero':6,'ativo':False,'bilhete':0}
             ]


lista_socios = [
            (1,16),
            (3,13),
            (5,15),
            (8,10),
            (9,19),
        ]

def atualiza_socios(lista_socios):
    carteiras_output = []
    for lista in lista_socios:
        carteiras_output.append({'numero':lista[0],'ativo': True,'bilhete':lista[1]})
    print(carteiras_output)
    