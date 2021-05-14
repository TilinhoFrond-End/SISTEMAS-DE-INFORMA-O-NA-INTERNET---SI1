#Primeiro você cria uma pasta socket, cliente e servidor(que pode conter .exe, imagem e um pdf) que vai enviar para o cliente.



import socket # Biblioteca Socket, responsável pelas conecções

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Server retorna o Objeto Socket, já o AF_INET tem conecções aceitas via IPV4 ou um domínio. E o SOCK_STREAM Vai ser via protocolo TCP.

server.bind(('localhost', 7777)) #Conectar o socket a um endereço do servidor, que pode ser o seu ip(localhost), na porta 7777.

print('Ouvindo conexões!\n')

server.listen(1) #Quantidade de conexões

connection, address = server.accept() #Objeto connection - conexão com o cliente. E address, o endereço do cliente. accept - aceita e armazena as o endereço e objeto de conexão.

namefile = connection.recv(1024).decode() #namefile(nome do Arquivo que deseja receber), '1024' quantidade mínima de bytes para o envio. utilizamos a função decode para transformar bytes em strings.


with open(namefile, 'rb') as file: # Abri o arquivo, se estiver corrompido, o with não abre
  for data in file.readlines():  #Ler todo o arquivo
    connection.send(data)   #Pra cada dado envia, o arquivo.

  print('Arquivo enviado')