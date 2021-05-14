import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Objeto Cliente

client.connect(('localhost', 7777))
print('Conectado!!\n')

namefile = str(input('Arquivo>')) #Usuário passa o nome do arquivo que ele deseja.

client.send(namefile.encode())  #A informação enviada por byte, transforma a string em bytes

with open(namefile, 'wb') as file:  #Pega os dados do servidor
  while 1:
    data = client.recv(100000)
    if not data:
      break
    file.write(data)

print(f"{namefile} recebido!\n")