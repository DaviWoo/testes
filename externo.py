



def criar_saudacao(saudacao):
    def saudar(nome):
        return(f'{saudacao}, {nome}!')
    
    return print(saudar('Davi'))


bom_dia = criar_saudacao('Bom dia')