from validate_docbr import CPF

def valida_cpf(numero):
    cpf = CPF()
    return cpf.validate(numero)


if __name__ == '__main__':
    print(valida_cpf("084.322.570-01"))
    print(valida_cpf("08432257001"))
    print(valida_cpf("054.312.475-01"))