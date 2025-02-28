
Estabelece uma comunicacao de entrada e saida entre os clientes usando o socket e fazendo a distribuição de carga entre servidores usando um servidor para balanceamento.
Ao total usei 3 servidores:
-2 servicos que vao receber as conexoes com as portas 10001 e 10002
-1 servico para distribuição  com a porta 4000
E o codigo de conexão do cliente quie acessa diretamente o balanceamento
O docker foi usado para fazer a virtualização dos serviços, mas as portas e o ip usadas foram a da maquina local 
