from challenge2.teste_two import *
import pytest

def teste_two_1():
    assert atualiza_socios([(1,4),(2,5),(7,9)]) == [{'numero':1,'ativo': True,'bilhete':4},
                                                     {'numero':2,'ativo': True,'bilhete':5}, 
                                                     {'numero':7,'ativo': True,'bilhete':9}]
