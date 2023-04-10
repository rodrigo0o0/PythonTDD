from codigo.bytebank import Funcionario
from datetime import datetime, timedelta



funcionario = Funcionario("Rodrigo Sandeski", '21/12/1981', 10000)

print(funcionario.calcular_bonus())