
Estabelece uma comunicacao de entrada e saida entre os clientes usando o socket e fazendo a distribuição de carga entre servidores usando um servidor para balanceamento.
Ao total usei 3 servidores:
-2 servicos que vao receber as conexoes com as portas 10001 e 10002
-1 servico para distribuição  com a porta 4000
E o codigo de conexão do cliente quie acessa diretamente o balanceamento
O docker foi usado para fazer a virtualização dos serviços, mas as portas e o ip usadas foram a da maquina local 

--o script ta usando poetry com o python 3.12

usei os seguintes comandos:

--"poetry new techshop" # é os caminhos do jeito que o petry usa

--"pyenv local 3.12" # usa essa vrsao do python dentro da pasta que foi dado o comando 

--"poetry env use 3.12"  #tem que colocar a versao do python  no pyprojet.toml

--"poetry shell na pasta techshop/techshop/" #inicia o ambiente virtual

****NESSA PARTE AQUI VC JA PRECISA TER O DOCKER INSTALADO NA SUA MAQUINA****

--"docker-compose up --build" # da esse comando na mesma pasta que o dockerfile e o docker-compose.yml estao, eles que vao criar os containers

--"docker-compose up --remove-orphans --force-recreate" #  esse comando esse comando elimina os containers dps que eles param

--ai vc ja pode dar um comando em outro shell "python ./conexaoCliente/Cliente.py" # abre outros terminais e da esse comando, ai vc ja vai conseguir ver que os todos os terminais vao ficar tipo um chat

