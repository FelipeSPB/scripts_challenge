from challenge2.two import atualiza_socios, carteiras
import pytest


def teste_two_1():
    assert atualiza_socios([(1,16),(3,13),(5,15),(8,10),(9,19)]) == [{'numero': 1, 'ativo': True, 'bilhete': 16},
                                                                   {'numero': 2, 'ativo': False, 'bilhete': 0},
                                                                   {'numero': 3, 'ativo': True, 'bilhete': 13},
                                                                   {'numero': 4, 'ativo': False, 'bilhete': 0},
                                                                   {'numero': 5, 'ativo': True, 'bilhete': 15},
                                                                   {'numero': 6, 'ativo': False, 'bilhete': 0},
                                                                   {'numero': 8, 'ativo': True, 'bilhete': 10},
                                                                   {'numero': 9, 'ativo': True, 'bilhete': 19}]

def teste_two_2():
    assert atualiza_socios([(1,4),(2,5),(7,9)]) == [{'numero':1,'ativo': True,'bilhete':4},
                                                     {'numero':2,'ativo': True,'bilhete':5},
                                                     {'numero': 3, 'ativo': False, 'bilhete': 0},
                                                     {'numero': 4, 'ativo': False, 'bilhete': 0},
                                                     {'numero': 5, 'ativo': False, 'bilhete': 0},
                                                     {'numero': 6, 'ativo': False, 'bilhete': 0},
                                                     {'numero':7,'ativo': True,'bilhete':9}]

def teste_two_3():
    assert atualiza_socios([(5,10)]) == [{'numero':1,'ativo': False,'bilhete':0},
                                                     {'numero':2,'ativo': False,'bilhete':0},
                                                     {'numero': 3, 'ativo': False, 'bilhete': 0},
                                                     {'numero': 4, 'ativo': False, 'bilhete': 0},
                                                     {'numero': 5, 'ativo': True, 'bilhete': 10},
                                                     {'numero': 6, 'ativo': False, 'bilhete': 0}
                                                     ]
def teste_two_4():
     assert atualiza_socios([(7,11)]) == [{'numero':1,'ativo': False,'bilhete':0},
                                                     {'numero':2,'ativo': False,'bilhete':0},
                                                     {'numero': 3, 'ativo': False, 'bilhete': 0},
                                                     {'numero': 4, 'ativo': False, 'bilhete': 0},
                                                     {'numero': 5, 'ativo': False, 'bilhete': 0},
                                                     {'numero': 6, 'ativo': False, 'bilhete': 0},
                                                     {'numero': 7, 'ativo': True,  'bilhete': 11}
                                                     ]