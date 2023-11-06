from random import randint

def gera_lancamentos():
    lancamentos = [str(randint(1, 6)) for _ in range(100)]
    return lancamentos

lancamentos = gera_lancamentos()

print(lancamentos)