# Quarto Modulo - Backend com Python

## Backend com Python

+ Protocolos de comunicação (HTTP, TCP, UDP, Socket)
+ Conceitos de Arquitetura Distribuída
+ Conceitos seguraça de APIs
    * Autenticação
    * Tokens
    * Sessões
  

### Protocolos de comunicação

+ São protocolos utilizados na comunicação entre sistemas
+ Permitem a conexão, comunicação e transferência de dados entre sistemas (Regem as regras para a comunicação ocorrer)
+ Eles definem as regras da comunicacção
+ Ex de Protocolo:
  * Socket
  * TCP
  * UDP
  * HTTP

#### Protocolo Socket

+ Socket é um protocolo de baixo nível que faz a comunicação com o Sistemas Operacional (Trabalha na camada ISO)  
+ Todos os demais protocolos utilizam socket para se comunicarem

Servidor - Cria o socket - Bind - Listener - Accept - Recebe Bytes - Envia Bytes

Cliente - Cria o socket - Connect - Envia Bytes - Recebe Bytes

#### Protocolo TCP

+ Transfer Control Protocol
+ Um dos principais protocolos da internet
+ Complementa o protocolo IP (internet protocol)
+ Provê um comunicação confiável, ordenada e garante a entrefa dos dados corretamnete
+ Um pacote perdido é re-transmitido

#### Protocolo UDP

+ User Datagram Protocol
+ Também complementa o protocolo IP
+ As aplicações podem enviar pacotes por uma rede IP sem efetuar a conexão
+ Deve ser utilizado para propósitos os quais erro e garantias não são necessários ou são feitos pela aplicação
+ Aplicações de tempo real utilizam esse protocolo devido a não poderem perder tempo com retransmissão de pacotes

#### Protocolo HTTP

+ Hypertext Transfer Protocol
+ Um dos protocolos mais utilizados na atualidade
+ A base da internet
+ Utiliza TCP (é um protocolo de aplicação)
+ É um protocolo de Request/Reply (Requisição/Resposta)
+ Uma mensagem possui cabeçalho (headers), corpo (body) e dados da requisição (verbo e url)
+ Trabalha com os verbos: GET, POST, PUT, DELETE e HEAD

### Arquitetura Distribuída

+ Sistema distribuído é um sistema que interliga diversos nós computacionais em um único sistema (diversos computadores separados com funcionamento conjunto)
+ Existem diversas técnicas/arquiteturas para distribuir um sistema
+ Uma página da internet é um exemplo de arquitetura distribuída chamada Cliente/Servidor

## Segurança de APIs

+ Garantir que somente quem pode acessar os dados possa acessá-los (autorização)
+ Identificar o emissor
+ Previnir exposição de dados sensíveis
+ Podemos utilizar algumas técnica para isso (também podem ser utilizadas em conjunto) ex: crypto
  
Autenticação:

+ Identifica qual o Usuário está acessando o sistema
+ Permite restringir acesso e permissões para cada usuário
+ Garante que um usuário é ele mesmo
+ Deve ser utilizado com outra técnica para fazer sentido em uma API
+ É utilizado em conjunto com sessão em páginas web

Tokens:

+ Um token é um pedaço de informação que garante a autenticidade dos dados
+ Pode Conter alguns dados dentro, tais como: validade, identidade e outros dados
+ O servidor abre o token e verifica o seu contéudo, se não for vaĺido ele recusa a requisição

Sessão:

+ Utilizada para manter um contexto sobre o usuário, gravado dados sobre a sessão
+ Geralmente utilizado com cookies em web apps
+ Não é muito recomendado para utilização em APIs