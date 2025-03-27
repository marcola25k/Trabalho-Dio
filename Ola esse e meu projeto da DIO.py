# Ola esse e meu projeto da DIO

# fazendo tela de cadatro de cliente do banco 
print('OLA SEJA BEM VINDO AO BANCO YBR \n TELA DE CADASTRO DE USUARIO:')
# Criando a funcao para receber os valores de user e senha 
def cadastro():
    user = str(input("Crie seu nome de Usuario com 8 letras e numeros: "))
    password = int(input("Digite uma senha com numeros 6 digitos inteiros: "))
    return user, password
# criando a funcao para fazer as comparacoes de user e senha
def verificacao(conta_cadastrado, senha_cadastrado):   
    tentativas = 0
    max_tentativas = 3
    
    while tentativas < max_tentativas:
        user = str(input("Digite seu usuario: "))
        try:
            password = int(input("Digite sua senha de 6 digitos: "))
            if user == conta_cadastrado and password == senha_cadastrado:
                print("Obrigado por utilizar o YBR, aproveite!")
                break  # Sai do loop se o login estiver correto
            else:
                tentativas += 1
                print(f"Login ou senha estao incorretos. Tentativa {tentativas}/{max_tentativas}")
                if tentativas == max_tentativas:
                    print("Numero maximo de tentativas atingido. Acesso bloqueado.")
        except ValueError:
            print("Erro: A senha deve conter apenas numeros inteiros!")
            tentativas += 1
            print(f"Tentativa {tentativas}/{max_tentativas}")
            if tentativas == max_tentativas:
                print("Numero maximo de tentativas atingido. Acesso bloqueado.")
    
print("---cadastramento de de cliente ---")
user, password = cadastro()    

print("login de acesso")
verificacao(user, password)
# Proxima tela depois de login 
menus = """
    [1] consultar Saldo:
    [2] Extratos:
    [3] fazer um Deposito
    [4] Sacar
    [5] Sair
    
 >= """
saldo = 0
extrato = " "
LIMITE = 1000   
DIARIO = 3
numero_saques = 0
while True:
    opcoes = input(menus)
    
    if opcoes == "1":
        recebe = saldo
        print(f" seu saldo de: {recebe}")
    
    elif opcoes == "2":
        print("\n================ EXTRATO ================")
        print("foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcoes == "3":
        print("vamos fazer seu deposito")
        entrando = int(input("Digite valor de Deposito: "))
        print(f"Deposito de: {entrando} realizado com sucesso")
        
        if entrando > 0:
            saldo += entrando
            extrato += f"Depósito: R$ {entrando:.2f}\n"
        else: 
            print(" Algo deu errado por favor tente novamente mas tarde!")
            
    elif opcoes == "4":
        valor_saque = int(input("digite valor de saque: "))
        if valor_saque > LIMITE:
            print("Esse valor ultrapassa limite por saque")
        elif valor_saque <= saldo:
            print(f"transaçao feita com sucesso \n Saque no valor de: {valor_saque}")
        if valor_saque == DIARIO:
            print("Esse valor ultrapassa limite diario")
        if valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
        elif valor_saque > saldo:
             print(f"O valor de saque: {valor_saque} e maior que o de saldo \n O limite diario de: {LIMITE} por saque")
            
    elif opcoes == "5":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
            
            
            
        

       
            
        
      
 

 
    
    









 
