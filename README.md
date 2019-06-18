# Scripts_challenge

1 - Criar dois scripts que ao inputar uma string retorne outra no formato dos exemplos abaixo (a partir da contagem dos caracteres).


         input : "teste conaz" 
         output: {'a': 1, ' ': 1, 'c': 1, 'e': 2, 'o': 1, 'n': 1, 's': 1, 't': 2, 'z': 1}

         input: "aaaaabbbbccccccaaaaaaa" 
         output: "5a4b6c7a"


2 - O time Guarani da Costeira mensalmente sorteia uma camisa do seu time de bocha para os sócios do clube.

salvando no seu banco de dados a seguinte estrutura:

carteiras = [
    {
        'numero': 1,
        'ativo': True,
        'bilhete': 10,
    },
    {
        'numero': 2,
        'ativo': False,
        'bilhete': 0,
    },
    {
        'numero': 3,
        'ativo': True,
        'bilhete': 12,
    },
    {
        'numero': 4,
        'ativo': False,
        'bilhete': 0,
    },
    {
        'numero': 5,
        'ativo': True,
        'bilhete': 14,
    },
    {
        'numero': 6,
        'ativo': True,
        'bilhete': 15,
    },
]

O departamento de sorteios recebe todo mês uma lista com os bilhetes a serem atualizados no banco, utilizando o formato:

lista_socios = [
    (1, 16), 
    (3, 13), 
    (5, 15), 
    (8, 10), 
    (9, 19),
]

Onde o primeiro número é o número do sócio e o segundo o bilhete do sorteio do mês. 
Essa lista é aproveitada para adicionar novos sócios e desativar inativos. Se o número do banco não está na lista, deve ser desativado, se o número da lista ainda não está no banco, deve ser adicionado já com seu bilhete pro sorteio do mês. Se o número da lista já está no banco, o número do sorteio deve ser atualizado.

Sua missão é escrever uma função atualiza_socios que recebe uma lista conforme o formato da lista_socios e faça a atualização do “banco” (representado pela estrutura carteiras) printando seu resultado final.

Os dados acima são só para exemplos.

Boa Sorte.

def atualiza_socios(lista_socios):
.
.
.




    

    



