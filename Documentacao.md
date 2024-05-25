# Projeto - Exchange de Criptomoedas
## Sobre
  Esse programa foi feito para simular um aplicativo de compras e vendas de criptomoedas, nele é possível realizar diversas ações como, cadastrar
  novos usuários, efetuar o login, realizar o depósito da moeda REAL, sacar uma quantia dessa moeda igual ou inferior à que possui na 
  conta, também é possível utilizar dessa moeda REAL para realizar a compra das criptomoedas disponíveis no programa, após a compra de 
  qualquer criptomoeda, é possível vende-las, cada uma dessas ações citadas acima ficam gravadas na aba "Consultar Extrato", o programa também
  possui o mecanismo de atualizar a cotação de moedas, onde ele varia o valor de cada moeda em -5% a +5% do seu valor anterior. Lembrando que,
  as moedas **são fictícias**, portanto não possuem significado algum fora do programa.

## Funcionamento
  ### 1. Página inicial do programa

  <p align="center">Ao abrir o pograma você irá se deparar com a seguinte interface:</p>
  
   <p align="center">                 
    <img src=https://github.com/KaioLC/exchange-criptmoedas/assets/170814907/da4138c1-60a7-40c8-88fb-c7719b5ab38f>
   </p>
   <p align="center">Nela, só é possível escolher uma das duas opções (cadastrar ou login) </p>

   #### 1.1 Página de Cadastro
   
   <p align="center">
     Ao entrar na página de cadastro, insira o seu nome, CPF (Sem pontos e traços) e uma senha NUMÉRICA de 6 dígitos.
   </p>
   
   #### 1.2 Página de Login
   <p align="center">
     Após ser efetuado o cadastro, é possível realizar o login utilizando o CPF e senha cadastrados anteriormente
   </p> 
   
   ### 2. Menu de opções
   <p align="center">
     Login realizao com sucesso! você deve se deparar com essa tela:
     <br><br>
     <img src=https://github.com/KaioLC/exchange-criptmoedas/assets/170814907/87a37b51-2d5e-48c2-aa65-15d2e6dd32b0>
     <br>
      Nela é possível escolher uma dentre as opções disponíveis, basta digitar o respectivo número da opção que deseja
   </p>

   #### 2.1 Consultar o saldo
   <p align="center">
     Ao selecionar essa opção, é pedido a senha do usuário para conseguir visualizar o saldo, caso a senha seja inserida corretamente a tela com o saldo de todas as moedas
     será exibida para o usuário:
     <br><br>
      <img src=https://github.com/KaioLC/exchange-criptmoedas/assets/170814907/1d727111-baaa-4ea1-b1a4-2d3cf8cf267e>
   </p>

   ### 2.2 Consultar extrato
   <p align="center">
     Ao selecionar a opção 2, o usuário será direcionado para a tela de consultar extrato, onde será pedido a senha cadastrada pelo usuário, após inserir a senha corretamente
     o usuário checar o seu histórico de ações como, deposito, saque, compra e venda também é mostrado a data e a hora que foi realizado essas operações, 
     dependendo da ação é informada a taxa cobrada junto com o saldo atualizado com a taxa:
     <img src=https://github.com/KaioLC/exchange-criptmoedas/assets/170814907/3309b4c6-babd-40ac-b775-113334833d6d>

   </p>

   ### 2.3 Depositar
   <p align="center">
     A opção 3 é onde você realiza o deposito de dinheiro em R$, que cai diretamente no seu saldo como mostrado na imagem abaixo:
     <br><br>
     <img src=https://github.com/KaioLC/exchange-criptmoedas/assets/170814907/8cbdcf90-9bd6-4246-8b92-804948a7794b>
     <br> 
     Com o depósito feito, é mostrado o saldo atual do usuário após o depósito, e também é mostrado para o usuário duas opções, a primeira opção (1) é Voltar para o menu de opções, a segunda opção (2) é realizar 
     outro depósito.
   </p>

   ### 2.4 Sacar
   <p align="center">
     Na opção 4 é usada para realizar o saque de dinheiro R$ obtido no saldo da conta, onde o usuário pode determinar o valor contanto que seja um valor menor ou igual ao disponível no saldo:
     <br><br>
     <img src=https://github.com/KaioLC/exchange-criptmoedas/assets/170814907/5b32baf3-52ec-4a5c-b292-e31714836d58>
     <br>
     Após realizar o saque, é mostrado o saldo atualizado da conta junto de duas opções, a opção número 1 o usuário realiza novamente o saque na conta, a opção número 2, direciona o usuário a tela de menu de opções

   </p>
  
  ### 2.5 Comprar criptomoedas
  <p align="center">
    Opção de número 5 é usada para efetuar a compra de criptomoedas, ao selecionar essa opção o usuário deve digitar a senha cadastrada, após inserir corretameente a senha será exibida a seguinte tela:
    <br><br>
    <img src=https://github.com/KaioLC/exchange-criptmoedas/assets/170814907/3d1ad2dd-4cf1-4149-bec7-1dc2a2eb1458>
    <br>
    Nessa tela o usuário vê as criptomoedas disponíveis para compra, junto de suas cotações em R$, ele pode selecionar a criptomoeda pelo número especificado ou digitar 4 para voltar ao menu de opções.
    <br>
    Caso o usuário tenha escolhido alguma criptomoeda para comprar, será pedido o valor em R$ que deseja investir nela, ao inserir um valor válido, será calculado a quantidade unitária de moedas de acordo com a     cotação e a quantidade de valor investido pelo usuário, é possível checar essa quantidade na página de consultar saldos.
    <br><br>
    <img src=https://github.com/KaioLC/exchange-criptmoedas/assets/170814907/95b7d2ee-a2fc-4052-b5f4-84abd76b40ff>
  </p>

  ### 2.6 Vender criptomoedas
   <p align="center">
     A opção número 6 permite que o usuário venda suas criptomoedas, para acessá-la é pedido a senha cadastrada do usuário, feito isso será mostrado a seguinte tela:
     <br><br>
     <img src=https://github.com/KaioLC/exchange-criptmoedas/assets/170814907/47218431-e68c-46a6-8a47-82d5169688e8>
     <br>
     Nela é possível ver a cotação atual de cada moeda, junto da quantidade unitária de moedas possuidas pelo usuário, ao escolher a opção da moeda desejada, será pedido a quantidade em R$ que o usuário pretende 
     vender da sua moeda, após selecionar uma quantia válida, é mostrado a mesma tela da imagem anterior, porém agora a quantidade da moeda escolhida está atualizada após a venda:
     <br><br>
     <img src=https://github.com/KaioLC/exchange-criptmoedas/assets/170814907/41409229-471b-4892-a852-829471e9c652>
   </p>
  
### 2.7 Atualizar cotação
 <p align="center">
   Ao selecionar a opção número 7, será atualizada a cotação de todas as criptomoedas, variando o preço em -5% até +5% do seu valor atual, logo em seguida exibindo a cotação atualizada de cada criptomoeda
   <br><br>
   <img src=https://github.com/KaioLC/exchange-criptmoedas/assets/170814907/b3264637-6de9-4fde-bf6a-fe088becdfb0>
   <br>
   Isso é feito de forma automática, então o usuário só precisa digitar a opção de número 7 que já será feito o processo de atualização das cotas.
 </p>

 ### 2.8 Sair
   <p align="center">
     Essa opção é usada para encerrar o serviço, finalizando a interação com o usuário e fechando o programa.
  
