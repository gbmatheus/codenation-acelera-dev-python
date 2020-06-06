# Terceiro Modulo - Funções e Orientação a Objeto

## Testes com Python

+ Tipos de testes
+ Porque usar TDD?
+ Pytest

### Tipos de testes

+ Sistema - teste do sistema como um todo
+ Integração - integração entre partes do sistema
+ Unitáriio - menor parte do sistema

Quanto mais alto na hierarquia maior o custo e o tempo de execução.
Teste de sistema é mais demorado do que o teste unitário.

Exemplo de teste

+ Sistema: Teste de aceitação
+ Integração: Teste de integração (ex: duas classe ou dois módulos diferentes)
+ Unitário: Teste unitário (ex: função ou classe)

### Porque usar TDD? - se faz vários pequenos passos, para desevolver tal funcionalidade

+ Desenvolvimento orientado a testes (No decorrer do desenvolvimento, é desenvolvido teste)
+ É uma maneira de desenvolver pensando em teste (pensa em teste em dev)
+ Guia o design da aplicacação
+ Nos ajuda a entender melhor o problema que estamos resolvendo
+ Gareante uma boa qualidade na aplicação dando seguraça para alterá-la
+ Ciclo de desenvolvimento usando TDD:
    * Escreva um teste
    * Implementa o mínimo para que o teste passe
    * Refatore (para exemplos complexo)
    * Repita
