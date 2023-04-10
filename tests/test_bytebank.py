import pytest
from pytest import mark
from codigo.bytebank import Funcionario
#pytest --cov=codigo tests/ --cov-report html

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        #given when then
        #Given-Contexto
        entrada = '13/03/2000'
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        #When ação
        resultado = funcionario_teste.idade()

        assert resultado == esperado #Then Desfecho


    def test_quando_nome_recebe_rodrigo_sandeski_deve_retornar_sandeski(self):
        #given when then
        #Given-Contexto
        entrada = 'Rodrigo Sandeski'
        esperado = 'Sandeski'

        funcionario_teste = Funcionario(entrada, '13/03/2000', 1111)
        #When ação
        resultado = funcionario_teste.sobrenome()

        assert resultado == esperado #Then Desfecho

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(selfs):
        #Given-contexto
        entrada_salario = 100000
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '13/03/2000', entrada_salario)
        #When Ação
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado


    #pytest test_bytebank.py -v -m calcular_bonus
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        #Given-contexto
        entrada_salario = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '13/03/2000', entrada_salario)
        #When Ação
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        #Given-contexto
        with pytest.raises(Exception):
            entrada_salario = 1000000

            funcionario_teste = Funcionario('Teste', '13/03/2000', entrada_salario)
            # When Ação
            resultado = funcionario_teste.calcular_bonus()

            assert resultado






            assert esperado == funcionario_teste.__str__()

    def test_nome_property(self):
        #Criar instancia de funcionario
        esperado = 'João Pedro'
        nome = 'João Pedro'
        funcionario_teste = Funcionario(nome, '13/03/2000', 5000)

        resultado = funcionario_teste.nome

        assert resultado == esperado

