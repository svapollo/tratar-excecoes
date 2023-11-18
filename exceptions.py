class SaldoInsuficienteError(Exception):
    def __init__(self, message='', saldo=None, valor=None, *args):
        self.saldo = saldo
        self.valor = valor
        msg = 'Saldo insuficiente para efetuar a transacao\n' \
              f'Saldo atual: {self.saldo}\nValor a ser sacado: {self.valor}'
        super(SaldoInsuficienteError, self).__init__(message or msg, self.saldo, self.valor, *args)
