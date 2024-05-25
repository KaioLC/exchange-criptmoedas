
# função principal do programa
def main():
    import json
    from datetime import datetime # Importa biblioteca para pegar a hora e dia exato das ações do usuário
    import os #biblioteca para limpar terminal
    import copy # para copiar os dados
    from random import randint #aleatoriza os numeros para atualizar cotacoes

    msg = None #Cria variavel que carregara alguma  mensagem especificada
    dados = {}

    
    def le_dados():
        with open('datas.json', 'r', encoding='utf8') as ler: #lendo dados
            dados = json.load(ler)
            return dados
    
    def salva_dados(cpf,nome,senha,saldo,extrato,dados):
        with open('datas.json', 'w', encoding='utf8') as escrever: # Escrevendo dados no arquivo json
            cadastros = dados
            cadastros[cpf] = {
                'nome':nome, 
                'senha':senha, 
                'saldo':saldo, 
                'extrato':extrato
                }
            json.dump(cadastros, escrever, indent=2, ensure_ascii=False)
    
    def atualiza_dados(dados):
        with open('datas.json', 'w', encoding='utf8') as escrever:
            json.dump(dados,escrever,indent=2,ensure_ascii=False)

    def le_cotas(): 
        with open('cotas.json', 'r', encoding='utf8') as ler:
            cotas = json.load(ler)
            return cotas

    def atualiza_cotas():
        with open('cotas.json', 'w', encoding='utf8') as atualiza:
            ct = cotacao
            for chave in ct.keys():
                variacao = randint(0,5)
                incr_decr = randint(0,1)
                
                if incr_decr == 0:
                    ct[chave]+= (ct[chave]*variacao/100)
                else:
                    ct[chave]-= (ct[chave]*variacao/100)
            json.dump(ct,atualiza,indent=2,ensure_ascii=False)        
    def sessao():
        dados = le_dados()
        cpf = resposta_login[1]
        return dados[cpf]
    
    saldo = {   # Saldo inicial da carteira do usuario
        'reais': 0.0,
        'btc': 0.0,             
        'eth': 0.0,
        'xrp': 0.0
    }
    cotacao = le_cotas()
    tx_compra = { # taxa de compra das criptomoedas
        'btc': 0.02,
        'eth': 0.01,
        'xrp': 0.01,
    }
    tx_venda = { # taxa de venda
        'btc': 0.03, 
        'eth': 0.02,
        'xrp': 0.01,
    }
    extrato = [] # Extrato inicial do usuario
    
    while True:
        # Função que exibe a tela inicial (Cadastro e login)
        def tela_inicial(msg):
            os.system('cls')
            if msg:
                print(msg)
            opcoes = ['Cadastrar', 'Login'] # Opcoes geradas
            print("-"*30) # Imprime - 25 vezes

            for i in range(len(opcoes)): # Imprime as opcoes com numero indicado ao lado
                print(f'[{i+1}]', end=' - ') # Imprime o numero da respectiva opcao
                for _ in range(1):
                    print(opcoes[i]) # Imprime a opcao
            print("-"*30)
            opcao_inicio = input('Escolha uma opção válida: ') # Pega a opcao escolhida pelo usuario
            print("-"*30)
            return opcao_inicio # Retorna ela na funcao
        
        # Função que realiza o cadastro
        def cadastro(msg):
            os.system('cls') # Limpa terminal
            nome = input('Digite seu nome: ') # Pede o apelido do usuario
            # Loop infinito para coleta obrigatoria de dados do usuario
            
            while True:
                os.system('cls')
                
                if msg:
                    print(msg)
                print('Digite seu nome:',nome)
                print("-"*30)
                # Verificando se o CPF digitado são números
                try:
                    cadastrar_cpf = int(input('Insira seu CPF, sem pontos e sem traços: ')) # Coleta o cpf do usuario
                    cadastrar_cpf = str(cadastrar_cpf)
                    if len(cadastrar_cpf) < 10 or len(cadastrar_cpf) > 11:
                        msg = 'CPF inválido'# Verificação basica se contem 11 digitos
                        continue # Volta pro inicio do laço
                    else:
                        msg = None
                    try:
                        dados = le_dados()
                        if cadastrar_cpf in dados:
                            msg = 'CPF já cadastrado'
                            continue
                    except:
                        ...
                    
                    # Laço para coleta de senha do usuario
                    while True:
                        os.system('cls')
                        if msg:
                            print(msg) # Exibindo aviso, caso tenha
                        print("-"*30)
                        print('Digite seu nome:',nome)
                        print("-"*30)
                        print('Insira seu CPF, sem pontos e sem traços:', cadastrar_cpf)
                        # Coletando a senha
                        print("-"*30)
                        cadastrar_senha = str(input('Cadastre a senha de 6 digitos inteiros: '))
                        # Verificando se a senha possui 6 digitos
                        try:
                            eh_int = int(cadastrar_senha)
                            if len(cadastrar_senha) != 6:
                                msg = 'A senha precisa ser de 6 digitos inteiros.'
                            else:
                                break # Caso possua, sair do primeiro laço
                        except:
                            msg  = 'A senha precisa ser digitos numéricos'
                            print("-"*30)
                    try:
                        dados = le_dados()
                        salva_dados(cadastrar_cpf,nome,cadastrar_senha,saldo,extrato,dados)
                    except:
                        dados = {}
                        salva_dados(cadastrar_cpf,nome,cadastrar_senha,saldo,extrato,dados)
                    break
                except:
                    msg = "CPF são APENAS números"
                           
        # Função que realiza o login
        def login(msg):
            
            resposta = False # Resposta do login false = não feito com êxito
            while True:
                os.system('cls')
                if msg:
                    print(msg)
                print("-"*30)
                # Coleta o login para  verificar se coincide com o cadastrado
                login = input('Digite seu CPF: ')
                senha = input('Digite sua senha de 6 digitos: ') # Juntamente da senha
                # Verifica se o login e senha são iguais aos cadastrados
                print("-"*30)

                if login in dados:
                    if senha == dados[login]['senha']:
                        resposta = True # Caso seja, login feito com êxito
                        return resposta, login # Retorna essa informação
                    else:
                        msg = 'Senha incorreta!'
                else: # Caso contrario, informar ao usuario que alguma informação está incorreta
                    msg = 'Login Incorreto!'

        # Função que gera o menu com as opções para o usuario escolher
        def menu(msg):
            os.system('cls')

            cpf = resposta_login[1]
            nome = usuario['nome']

            print(f'Nome: {nome}    CPF: {cpf}')
            if msg:
                print("-"*30)
                print(msg)
            print("-"*30)
            # Opções de escolhe do usuário
            opcoes = ['Consultar saldo', 'Consultar extrato', 'Depositar', 
            'Sacar', 'Comprar criptomoedas', 'Vender criptomoedas', 
            'Atualiar cotação', 'Sair']
            # Imprime as opções 
            qtd_op = [] # Lista para pegar a quantiddade de opcoes
            for indice in range(len(opcoes)):
                print(f'{indice+1}', end=' - ')
                qtd_op.append(indice+1)
                for _ in range(1):
                    print(opcoes[indice])
            # Coleta a opção desejada
            print("-"*30)
            opcao = input('Escolha uma opção: ')
            print("-"*30)
            return opcao, qtd_op # Retorna na função

        # Essa função consulta o saldo do usuario
        def consultar_saldo():

            saldos = usuario['saldo']

            opcoes = ['Voltar'] # Opções do usuário nessa aba do programa
            while True:
                senha = input('Digite a senha cadastrada: ')
                if senha == usuario['senha']:
                    print('\nReais:','{:.2f}'.format(saldos['reais'])) # Conteúdo página
                    print('Bitcoin:','{:.6f}'.format(saldos['btc'])) # Conteúdo página
                    print('Ethereum:','{:.3f}'.format(saldos['eth'])) # Conteúdo página
                    print('Ripple:','{:.2f}'.format(saldos['xrp'])) # Conteúdo página
                    print('\n')

                # Imprime as opções
                for indice in range(len(opcoes)):
                    print(f'{indice+1}', end=' - ')
                    for _ in range(1):
                        print(opcoes[indice])
                print("-"*30)
                # Coleta as opções do usuário
                opcao = input('Opcao: ')
                if opcao == '1':
                    break
            return opcao # Retorna na função
        
        # Essa função consulta o extrato do usuario
        def consultar_extrato():

            opcoes = ['Voltar'] # Opções do usuário
            while True:
                senha = input('Digite a senha cadastrada: ')
                if senha == usuario['senha']:
                    for dado in usuario['extrato']:
                        print(dado)


                for indice in range(len(opcoes)): 
                    print(f'{indice+1}', end=' - ')
                    for _ in range(1):
                        print(opcoes[indice])
                print("-"*30)
                # Coleta a opção escolhida pelo usuário        
                opcao = input('Opcao: ')
                if opcao == '1':
                    break
                else:
                    print('Opcao inválida')
            return opcao
        
        # Essa função permite que o usuario deposite
        def depositar():

            depositar = 0
            deposito = False
            save_acao = ''
            opcoes = ['Voltar', 'Depositar novamente'] # Opções de escolhe do usuário
            while True:
                print('\nQuantos R$ deseja depositar: ',end='') # Conteúdo da página
                try:
                    depositar = float(input()) # verifica se é numero
                    
                    if depositar > 0: # Verificando se o deposito é um valor positivo
                        print('\nDeposito Realizado com Sucesso!')
                        print('\n')
                        print('Saldo atual: ',usuario['saldo']['reais']+depositar)
                        deposito = True
                    else:
                        print('\nDigite um valor válido')
                
                    print('\n'*2)
                    # Imprime as opções
                    for indice in range(len(opcoes)):
                        print(f'{indice+1}', end=' - ')
                        for _ in range(1):
                            print(opcoes[indice])
                    print("-"*30)
                    if deposito:
                            hoje = datetime.now()
                            data = hoje.date()
                            sinal = "+" if depositar > 0 else "-"
                            usuario['saldo']['reais'] += depositar
                            reais = copy.deepcopy(usuario['saldo']['reais'])
                            cota = copy.deepcopy(cotacao['reais'])
                            bitcoin = copy.deepcopy(usuario['saldo']['btc'])
                            ethereum = copy.deepcopy(usuario['saldo']['eth'])
                            ripple = copy.deepcopy(usuario['saldo']['xrp'])
                            save_acao = f'{data} {hoje.hour}:{hoje.minute} {sinal} {depositar:.2f} REAL CT: {cota} TX: 0.00 REAL: {reais:.2f} BTC: {bitcoin:.6f} ETH: {ethereum:.4f} XRP: {ripple:.2f}'
                            usuario['extrato'].append(save_acao)
                    # Coleta a opção escolhida do usuário
                    opcao = input('Opcao: ')
                    if opcao == '1':
                        return opcao, depositar, deposito
                    
                    elif opcao == '2':
                        continue
                    else:
                        'Digite uma opcao válida'
                        while opcao != '1' or opcao != '2':
                            opcao = input('Opcao: ')
                    
                except:
                    print('Digite números.')
                    continue
                
        # Essa função permite o saque do usuario
        def sacar():

            opcoes = ['Sacar novamente','Voltar'] # Opções de escolha do usuario
            while True:
                print('\nDeseja sacar quanto: ', end='') # Conteúdo da página
                try:
                    sacou = False
                    saque = float(input())
                    if saque > usuario['saldo']['reais']:
                        saque = 0
                        print('\n')
                        print('Não tem saldo suficiente')
                        print('\n')

                    else:
                        print('\n'*1)
                        print('Saque realizado com sucesso!')
                        sacou = True
                        print('\n')
                        print('Saldo atual: ',usuario['saldo']['reais']-saque)
                        usuario['saldo']['reais'] -= saque
                        hoje = datetime.now()
                        data = hoje.date()
                        reais = copy.deepcopy(usuario['saldo']['reais'])
                        cota = copy.deepcopy(cotacao['reais'])
                        bitcoin = copy.deepcopy(usuario['saldo']['btc'])
                        ethereum = copy.deepcopy(usuario['saldo']['eth'])
                        ripple = copy.deepcopy(usuario['saldo']['xrp'])
                        save_acao = f'{data} {hoje.hour}:{hoje.minute} - {saque:.2f} REAL CT: {cota} TX: 0.00 REAL: {reais:.2f} BTC: {bitcoin:.6f} ETH: {ethereum:.4f} XRP: {ripple:.2f}'
                        usuario['extrato'].append(save_acao)
                    # Imprime as opções do usuário
                    for indice in range(len(opcoes)):
                        print(f'{indice+1}', end=' - ')
                        for _ in range(1):
                            print(opcoes[indice])
                    print("-"*30)
                    opcao = input('Opcao: ')
                    if opcao == '1':
                        continue
                    elif opcao == '2':
                        return opcao, sacou
                except:
                    print('Digite números.')
                    continue
                
        
        # Essa função permite que o usuario compre alguma criptomoeda
        def comprar_cripto():

            opcoes = ['Voltar'] # Opções de escolha do usuário
            compra = False
            while True:
                senha = input('Digite a senha cadastrada: ')

                if senha == usuario['senha']:
                    # Exibindo opcoes de compra
                    criptos = ['Bitcoin', 'Ethereum', 'Ripple', 'Voltar']
                    # pegando as taxas
                    cota = []
                    for ct in cotacao.values():
                        cota.append(ct)
                    # Exibindo opcoes
                    indice = 1
                    for i, moedas in enumerate(criptos):
                        for _ in range(1):
                            try:
                                print(f'{i+1} - {moedas}: R${cota[indice]}')
                            except:
                                print(f'{i+1} - {moedas}')
                        indice+=1
                    # Coletando a opcao
                    opcao = input('Opcao: ')
                    def salvar_acao(valor, opcao, moeda):
                        hoje = datetime.now()
                        data = hoje.date()
                        reais = copy.deepcopy(usuario['saldo']['reais'])
                        cota = copy.deepcopy(cotacao[moeda])
                        bitcoin = copy.deepcopy(usuario['saldo']['btc'])
                        ethereum = copy.deepcopy(usuario['saldo']['eth'])
                        ripple = copy.deepcopy(usuario['saldo']['xrp'])
                        tx = copy.deepcopy(tx_compra[moeda])
                        if opcao == '1':
                            cripto = 'BTC'
                        elif opcao == '2':
                            cripto = 'ETH'
                        elif opcao == '3':
                            cripto = 'XRP'
                        save_acao = f'{data} {hoje.hour}:{hoje.minute} + {valor:.2f} {cripto} CT: {cota} TX: {tx:.2f} REAL: {reais:.2f} BTC: {bitcoin:.6f} ETH: {ethereum:.4f} XRP: {ripple:.2f}'
                        usuario['extrato'].append(save_acao)
                    try:
                        if opcao == '1': # Caso seja 1 [bitcoin]
                            valor = float(input('Quantos R$ em bitcoins: '))
                            if valor > usuario['saldo']['reais'] or valor <= 0: # Valor desejado superar o saldo disponivel
                                print('Não é possivel realizar a compra com esse valor')
                            else: # Caso seja possivel a compra, realizar
                                save_saldo = usuario['saldo']['reais']
                                usuario['saldo']['reais'] -= valor + (valor*tx_compra['btc']) # Cobrando os Reais da carteira com taxa
                                if usuario['saldo']['reais'] < 0:
                                    print('Saldo Insuficiente para taxa')
                                    usuario['saldo']['reais'] = save_saldo
                                else:
                                    usuario['saldo']['btc'] += (valor / cotacao['btc']) # Calculo para qntd de moedas
                                    salvar_acao(valor,opcao, 'btc')
                                    compra = True
                                
                        elif opcao == '2': # Caso seja 2 [Ethereum]
                            valor = float(input('Quantos R$ em ethereums: '))
                            if valor > usuario['saldo']['reais'] or valor <= 0:
                                print('Não é possivel realizar a compra com esse valor')
                            else:
                                save_saldo = usuario['saldo']['reais']
                                usuario['saldo']['reais'] -= valor + (valor*tx_compra['eth']) # Cobrando os Reais da carteira com taxa
                                if usuario['saldo']['reais'] < 0:
                                    print('Saldo Insuficiente para taxa')
                                    usuario['saldo']['reais'] = save_saldo
                                else:
                                    usuario['saldo']['eth'] += (valor / cotacao['eth']) # Calculo para qntd de moedas
                                    salvar_acao(valor,opcao, 'eth')
                                    compra = True
                        elif opcao == '3': # Caso seja 3 [Ripple]
                            valor = float(input('Quantos R$ em Ripple: '))
                            if valor > usuario['saldo']['reais'] or valor <= 0:
                                print('Não é possivel realizar a compra com esse valor')
                            else:
                                save_saldo = saldo['reais']
                                usuario['saldo']['reais'] -= valor + (valor*tx_compra['xrp']) # Cobrando os Reais da carteira com taxa
                                if usuario['saldo']['reais'] < 0:
                                    print('Saldo Insuficiente para taxa')
                                    usuario['saldo']['reais'] = save_saldo
                                else:
                                    usuario['saldo']['xrp'] += (valor / cotacao['xrp']) # Calculo para qntd de moedas
                                    salvar_acao(valor,opcao, 'xrp')
                                    compra = True
        
                        elif opcao == '4': # Caso seja 4 [Voltar]
                            return opcao, compra
                        else: # Caso não seja nenhum desses
                            print('Opcao invalida')
                    except:
                        print('Digite números.')

                else:
                    print('Senha inválida')
                # Imprime as opções do usuário no terminal 
                for indice,opc in enumerate(opcoes):
                    print(f'{indice+1} - {opc}')
                # Coleta a opção escolhida pelo usuário
                print('\n'*2)
                opcao = input('Opcao: ')
                if opcao == '1':
                        break      
                else:
                    print('Opção inválida')
            return opcao, compra

        # Essa função permite que o usuario venda suas criptomoedas   
        def vender_cripto():
            
            vendeu = False
            print('Vender Criptomoedas')
            opcoes = ['Voltar'] # Opções de escolha do usuário caso erre a senha    
            senha = input('Digite a senha cadastrada: ')      
            while True:
                

                if senha == usuario['senha']:
                    # Exibindo opcoes de compra
                    criptos = ['Bitcoin', 'Ethereum', 'Ripple', 'Voltar']
                    # pegando as taxas
                    cota = []
                    for ct in cotacao.values():
                        cota.append(ct)
                    carteira = []
                    for wallet in usuario['saldo'].values(): # pegando quanto possui na carteira
                        carteira.append(wallet)
                    # Exibindo opcoes
                    indice = 1
                    for i, moedas in enumerate(criptos):
                        for _ in range(1):
                            try:
                                print(f'{i+1} - {moedas}: R${cota[indice]} - Você tem: {carteira[indice]}')
                            except:
                                print(f'{i+1} - {moedas}')
                        indice+=1
                    opcao = input('Opcao: ')
                    if opcao == '4':
                        opcao == '1'
                        return opcao, vendeu
                    try:
                        valor = float(input('Quantos R$  deseja vender: '))
                        def buybuy(valor,moeda):
                            tem_rs = usuario['saldo'][moeda]*cotacao[moeda]
                            if valor > tem_rs or valor <= 0:
                                print('Saldo insuficiente')
                                return False
                            
                            tem_rs -= valor
                            usuario['saldo'][moeda] = tem_rs/cotacao[moeda]
                            usuario['saldo']['reais'] += valor-(tx_venda[moeda]*valor)
                            return True
                            
                        def salvar_acao(valor, opcao, moeda):
                            hoje = datetime.now()
                            data = hoje.date()
                            reais = copy.deepcopy(usuario['saldo']['reais'])
                            cota = copy.deepcopy(cotacao[moeda])
                            bitcoin = copy.deepcopy(usuario['saldo']['btc'])
                            ethereum = copy.deepcopy(usuario['saldo']['eth'])
                            ripple = copy.deepcopy(usuario['saldo']['xrp'])
                            tx = copy.deepcopy(tx_compra[moeda])
                            if opcao == '1':
                                cripto = 'BTC'
                            elif opcao == '2':
                                cripto = 'ETH'
                            elif opcao == '3':
                                cripto = 'XRP'
                            save_acao = f'{data} {hoje.hour}:{hoje.minute} - {valor:.2f} {cripto} CT: {cota} TX: {tx:.2f} REAL: {reais:.2f} BTC: {bitcoin:.5f} ETH: {ethereum:.4f} XRP: {ripple:.2f}'
                            usuario['extrato'].append(save_acao)
                        if opcao == '1':
                            compra = buybuy(valor,'btc')
                            if compra:
                                salvar_acao(valor,opcao,'btc')
                                vendeu = True
                        elif opcao ==  '2':
                            compra = buybuy(valor,'eth')
                            if compra:
                                salvar_acao(valor,opcao,'eth')
                                vendeu = True
                        elif opcao == '3':
                            compra = buybuy(valor,'xrp')
                            if compra:
                                salvar_acao(valor,opcao,'xrp')
                                vendeu = True
                        else:
                            print('Opcao invalida')
                    except:
                        print('Digite números.')
                        continue

                else:
                    print('Senha incorreta')
                    while True:
                        for i, op in enumerate(opcao):
                            print(i+1,'-',op)
                        opcao = input('Opcao: ')
                        if opcao == '1':
                            return opcao
                        else:
                            print('Opcao inválida')
            
        # Essa função atualiza a cotação
        def atualiza_cotacao():

            opcoes = ['Voltar'] # Opções de escolha do usuário
            atualiza_cotas()
            cotacao = le_cotas()
            print('Cotação Atualizada! ' )
            print('\n'*1)
            # Exibe cotacao atual
            for indice, chave in enumerate(cotacao):
                print(f'{indice+1} - {chave}: R$',cotacao[chave])
            # Imprime as opções do usuário no terminal
            for indice in range(len(opcoes)):
                print(f'{indice+1}', end=' - ')
                for _ in range(1):
                    print(opcoes[indice])
            print("-"*30)
            # Coleta a opção escolhida pelo usuário
            opcao = input('Opcao: ')
            return opcao
            

        # Essa função encerra o serviço com o usuario
        def sair():
            # Exibe 'Saiu' na tela
            print('\nSaiu.\n')
            print("-"*30)

        # Pega a opção escolhida na tela inicial
        opcao = tela_inicial(msg)
        msg = None
        # Caso seja a opcao 1, realizar o cadastro        
        if opcao == '1':
            cadastros = cadastro(msg)
            cadastrado = True
            msg = 'Cadastrado com sucesso'
        # Caso seja a opcao 2, realizar o login
        if opcao == '2':
            resposta_login = (False, 0)
            try:
                dados = le_dados() # coleta todos os usuarios
                resposta_login = login(msg) # Realizar a função login e coletar a resposta
            except:
                msg  = 'Sem usuarios cadastrados'
            if resposta_login[0] == True:
                usuario = sessao() # Caso resposta == True
                opcao_usuario = menu(msg) # Exibe o menu e coleta a opção do usuario
            else: # Caso não tenha usuários cadastrados no sistema
                msg = 'Sem usuários cadastrados.' # Informa ao usuário
                continue # Volta ao inicio do laço main
        
            # Loop para navegação do menu
            while opcao_usuario != '8':
            # Dessa linha para baixo são a logica de exibição das funções para cada escolha do usuario mostrada no terminal 
                if opcao_usuario[0] == '1': 
                    opcao_geral = consultar_saldo()
                    if opcao_geral == '1': # Aqui, caso escolha a opcao 1, ele retorna ao menu
                        opcao_usuario = menu(msg)


                if opcao_usuario[0] == '2':
                    opcao_geral = consultar_extrato()
                    if opcao_geral == '1': # Aqui, caso escolha a opcao 1, ele retorna ao menu
                        opcao_usuario = menu(msg)


                if opcao_usuario[0] == '3':
                    opcao_geral = depositar()
                    if opcao_geral is not None:
                        if opcao_geral[2]:
                            dados = le_dados()
                            dados[resposta_login[1]] = usuario
                            atualiza_dados(dados)
                    if opcao_geral[0] == '1': # Aqui, caso escolha a opcao 1, ele retorna ao menu
                        opcao_usuario = menu(msg)


                if opcao_usuario[0] == '4':
                    opcao_geral = sacar()
                    if opcao_geral[1]:
                        dados = le_dados()
                        dados[resposta_login[1]] = usuario
                        atualiza_dados(dados)
                    if opcao_geral[0] == '2': # Aqui, caso escolha a opcao 1, ele retorna ao menu
                        opcao_usuario = menu(msg)
                    elif opcao_geral[0] == '1':
                        opcao_usuario = sacar()


                if opcao_usuario[0] == '5':
                    opcao_geral = comprar_cripto()
                    if opcao_geral[1]:
                        dados = le_dados()
                        dados[resposta_login[1]] = usuario
                        atualiza_dados(dados)
                    if opcao_geral[0] == '1': # Aqui, caso escolha a opcao 1, ele retorna ao menu
                        opcao_usuario = menu(msg)


                if opcao_usuario[0] == '6':
                    opcao_geral = vender_cripto()
                    if opcao_geral[1]:
                        dados = le_dados()
                        dados[resposta_login[1]] = usuario
                        atualiza_dados(dados)
                    if opcao_geral[0] == '1': # Aqui, caso escolha a opcao 1, ele retorna ao menu
                        opcao_usuario = menu(msg)


                if opcao_usuario[0] == '7':
                    opcao_geral = atualiza_cotacao()
                    
                    if opcao_geral == '1': # Aqui, caso escolha a opcao 1, ele retorna ao menu
                        opcao_usuario = menu(msg)


                if opcao_usuario[0] == '8': # Aqui, caso escolha 8, ele encerra o menu
                    sair() 
                    break
                if opcao_usuario[0] not in opcao_usuario[1]:
                    opcao_usuario = menu(msg)
            if opcao_usuario[0] == '8': # Caso tenha escolhido 8 também encerra o serviço
                break 
            
        elif opcao != '1'or opcao != '2' and  cadastrado != True: # Verifica se as opções da tela inicial são válidas
            print(opcao)
            msg = 'Opção inválida.'
main()