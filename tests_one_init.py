from challenge1.teste_one import *
import pytest

def test_count_dictionary_1():
    assert count_dictionary('teste conaz') == {' ': 1, 'a': 1, 'c': 1, 'e': 2, 'n': 1, 'o': 1, 's': 1, 't': 2, 'z': 1}

def test_count_dictionary_2():
    assert count_dictionary('bananada de goiaba') == {' ':2, 'a': 6, 'b':2, 'd':2,'e':1 ,'g':1 ,'i':1, 'n': 2, 'o': 1}


def test_count_dictionary_3():
    assert count_dictionary('marmelada de banana') == {' ': 2, 'a': 6, 'b':1, 'd': 2, 'e': 2, 'l':1, 'm':2, 'n': 2, 'r': 1}

def test_count_sum_1():
    assert count_sum('aaaaabbbbccccccaaaaaaa') == '5a4b6c7a'

def test_count_sum_2():
    assert count_sum('yyynnabbjjj') == '3y2n1a2b3j'

def test_count_sum_3():
    assert count_sum('pera') == '1p1e1r1a'
