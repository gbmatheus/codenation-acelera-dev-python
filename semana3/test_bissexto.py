"""
    Fonte: http://dojopuzzles.com/problemas/exibe/ano-bissexto

    ...o mês de fevereiro fica com 29 dias...

    Um determinado ano é bissexto se:
    O ano for dívispivel por 4, mas não divisível por 100, exceto se ele for tambpem divisível por 400.

    Anos bissextos: 1600, 1732, 1888, 1944, 2008

    Anos não bissextos: 1742, 1889, 1951, 2011
"""

# baby_step - sequecias de pequenos passo a serem feitos para fazer um teste passar
# Instalar a lib do pytest - "pip3 install pytest"
# O arquivo deve começar com a "test_nome_do_arquivo"
# No console basta rodar pytest, que os teste são executados automaticamentes
    # São detectados
# 
# Escrever os teste, codar o mínimo para ele passar, depois refatorar

# def test_alguma_coisa():
#     assert 1 == 1

import pytest

def eh_bissexto(ano):
    resto = ano % 4

    resto100 = ano % 100

    resto400 = ano % 400
    
    print(resto, resto100, resto400)
    print(resto == 0, resto100 == 0, resto400 == 0)

    if not resto:
        if not resto400:
            return True
        elif resto100:
            return True
        # Minha resolução antes da resolução aula ser vista
        # if not resto400:
        #     return True
        # 
        # elif not resto100:
        #     return False
        # 
        # else:
        #     return True

    return False


# defini o nome de uma variavel que será injetada, e depois executa com todos os casos
@pytest.mark.parametrize('ano', [1600, 1732, 1888, 1944, 2008]) # ('quais os nomes serão inseridos no teste', [lista de ano no caso])
def test_deve_ser_bissexto(ano):
    resp = eh_bissexto(ano)

    assert resp is True


@pytest.mark.parametrize('ano', [1742, 1889, 1951, 2011]) # ('quais os nomes serão inseridos no teste', [lista de ano no caso])
def test_nao_deve_ser_bissexto(ano):
    resp = eh_bissexto(ano)

    assert resp is False


# def test_deve_ser_ano_bissexto():
#     ano = 1600
# 
#     resp = eh_bissexto(ano)
# 
#     assert resp is True


# def test_nao_deve_ser_bissexto():
#     ano = 1742
# 
#     resp = eh_bissexto(ano)
# 
#     assert resp is False


# def test_deve_ser_ano_bissexto_1732():
#     ano = 1732
# 
#     resp = eh_bissexto(ano)
# 
#     assert resp is True


def test_nao_deve_ser_bissexto_500():
    # estrutura do teste (setup, execução e verificação)
    # setup
    ano = 500

    # execução do teste
    resp = eh_bissexto(ano)

    # verificação do resultado
    assert resp is False