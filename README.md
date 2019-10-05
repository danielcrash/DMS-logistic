# Programa de banco de dados DMS
## Programa feito para o 'Processo Seletivo TI - Desafio' pela empresa DMS Logistics
### O desafio:
> No mundo da logística lidamos diariamente com massas enormes de dados relacionado a importação e exportação de produtos. Através desses dados conseguimos extrair métricas importantes para garantir aos nossos clientes um bom acompanhamento de suas importações e precisamos de sua ajuda para cumprir com esse objetivo.</p>

> 1 - Utilizando Python e sqlite crie um pequeno programa onde poderemos inserir os dados relacionados abaixo referente a uma carga.

> <p>● Cliente</p> 
> <p>● Contato</p>
> <p>● Custo</p> 
> <p>● Preço</p> 
> <p>● Data de envio</p> 
> <p>● Data de chegada</p>

> 2 - Após inserir vários dados diferentes no banco, deixe nas instruções do README.md as querys necessárias para que consigamos consultar:

> <p>● Todos os clientes que solicitaram serviço e seu contato</p> 
> <p>● O custo de todos os processos já efetuados</p>
> <p>● O Lucro (preço - custos) obtido em todos os processos já realizados</p>

## Começando
Essas instruções fornecerão uma cópia do projeto em execução na sua máquina local para fins de desenvolvimento e teste.
### Pré-requisitos
O sofware foi feito para rodar em sistemas operacionais Windows, Linux ou Mac. Vai estar disponível no repositório duas versões do programa, uma na pasta [Programa DMS](https://github.com/danielcrash/samantha666/tree/master/Programa%20DMS) no qual basta fazer o download e executar o ``` exe ``` para rodar o programa. Já no repositório principal estarão os arquivos ``` Insert_table.py ```, ``` Update_table.py ``` e ``` Programa DMS.py ``` no qual podem ser rodados pelo [Ambiente de Desenvolvimento](https://www.python.org/downloads/) da linguagem Python. Caso opte por essa forma de execução, é necessário que mantenha o arquivo de banco de dados ``` clientes_carga01.db ``` para que funcione corretamente.

### Executando os testes
Os arquivos ``` Insert_table.py ``` e ``` Update_table.py ``` foram usados para moldar o banco de dados préviamente existente no programa, contudo o mesmo roda independete destes, basta executar o ``` Programa DMS.py ```. Já a versão em ``` exe ``` foi feita nesse formato para facilitar a execução já que a mesma não necessita de um ambiente de desenvolvimento para tal. 

### Testes de ponta a ponta
No menu principal temos todas as opções no qual o programa se propõe a fazer. Basta digitar no teclado a opção desejada.

![menu](https://github.com/danielcrash/samantha666/blob/master/menu%20programa.png)

Digitando a opção ``` [1] ``` será possível cadastrar um novo cliente no banco do dados do sistema com todos os campos no qual o desafio foi proposto.

![menu opção 1](https://github.com/danielcrash/samantha666/blob/master/menu%20opcao%201.png)

Digitando a opção ``` [2] ``` será possível visualizar todos os **clientes** e seu **contato** já cadastrados no banco de dados. 

![menu opção 2](https://github.com/danielcrash/samantha666/blob/master/menu%20opcao%202.png)

Digitando a opção ``` [3] ``` será possível vizualizar todos os **custos** referentes as solicitações dos clientes.

![menu opçãp 3](https://github.com/danielcrash/samantha666/blob/master/menu%20opcao%203.png)

Digitando a opção ``` [4] ``` será possível vizualizar os **preço**s, os **custos** e o total de **LUCRO** de todos os *clientes* cadastrados até o momento.

![menu opçãp 4](https://github.com/danielcrash/samantha666/blob/master/menu%20opcao%204.png)

Digitando a opção ``` [5] ``` será possível **deletar** um cliente já cadastrado.

![menu opçãp 5](https://github.com/danielcrash/samantha666/blob/master/menu%20opcao%205.png)

Digitando a opção ``` [6] ``` o programa será fechado com uma calorosa saudação.

![menu opçãp 6](https://github.com/danielcrash/samantha666/blob/master/menu%20opcao%206.png)

### Testes de codificação

Inicialmente foi utilizado um ``` while choice != 6: ``` para criar um loop no menu principal, enquanto a opção fosse diferente de ``` [6] ```.
O programa foi feito utilizando ``` if ``` e ``` elif ``` na sua estrutura principal para criar as opções.
No bloco de código abaixo é possível ver o primeiro ``` if ``` no qual fazemos um acesso ao banco de dados ``` SQLite3 ``` para que possa ser inserido pelo usuário as informações. Vale lembrar que a biblioteca ``` SQLite3 ``` é nativa do Python e pode ser chamada pelo comando ``` import sqlite3 ``` ao inicio do código.
```
        conn = sqlite3.connect('clientes_carga01.db')
        cursor = conn.cursor()

        p_cliente = input('Cliente: ')
        p_contato = input('Contato (xx xxxxx-xxxx): ')
        p_custo = input('Custo ex: (R$ 10250.15): R$ ')
        p_preco = input('Preço ex: (R$ 10250.15): R$ ')
        p_data_env = input('Data de Envio (yyyy-mm-dd): ')
        p_data_cheg = input('Data de Chegada (yyyy-mm-dd): ')

        cursor.execute("""INSERT INTO cargas (cliente, contato, custo, preco, data_env, data_cheg)
        VALUES (?,?,?,?,?,?)""", (p_cliente, p_contato, p_custo, p_preco, p_data_env, p_data_cheg))
        conn.commit()

        print ('Dados Inseridos com sucesso.')
        print ('\n\n\n\n')
```

Nesse bloco de código além do comando ``` SELECT ``` nativo do banco de dados para chamar a coluna **cliente** e **contato**, temos um ``` for ``` seguido do método ``` cursor.fetchall(): ``` que busca o resultado das querys solicitadas e retorna todas as rows de uma lista de tuplas. 
```
        cursor.execute("""SELECT cliente, contato FROM cargas;""")
        for linha in cursor.fetchall():
            print(linha)

```
No bloco de código abaixo é utilizado através do ``` cursor.execute ``` a syntax ``` SELECT SUM ``` no qual faz uma soma do total dos valores preenchidos na query. No programa os valores foram do tipo ``` float ```. 

```
        cursor.execute("""SELECT SUM(custo) FROM cargas;""")
        for linhas in cursor.fetchall():
            print('R$ %.2f'%linhas)
```

Nesse bloco de código foi utilizado novamente a syntax ``` SELECT SUM ``` para buscar o total dos valores, porém seguido do caracter ```-``` que fez a subtração dos valores totais da coluna **preço** em relação a coluna **custo** assim dando o total de **LUCRO**.

```     
        cursor.execute("""SELECT SUM(preco) - SUM(custo) FROM cargas;""")
        for linha2 in cursor.fetchall():
            print('\nTOTAL DE LUCRO')
            print('R$ %.2f'%linha2)
```
O trecho de código abaixo se refere ao arquivo ``` Insert_table.py ``` o qual foi utilizado para criar o banco de dados inicialmente. Este foi feito através de uma função utilizando a palavra reservada ``` def ```. A tabela foi criada para que não fosse possível deixar algum elemento nulo e também o elemento ``` id ``` usado como ``` primary key ``` sendo o mesmo ``` autoincrement ```. No final do trecho é executado a função.

```
  def create_table():
	c.execute('CREATE TABLE cargas (id integer not null primary key autoincrement, \
                        cliente text not null, contato text not null, custo real not null, preco real not null, \
                        data_env text not null, data_cheg text not null)')

create_table()
```
Aqui é feito uma segunda função para que seja inserido dados préviamente no programa através da syntax ``` INSERT INTO ``` e gravadas ao final atravez do comando ``` conn.commit() ```.

```
def dateentry():
	c.execute("INSERT INTO cargas (cliente, contato, custo, preco, data_env, data_cheg) VALUES('SOS Logistics', '21 24489-6491', 15750.15, \
			30800.15, '2019-04-14', \
			'2019-04-14')")
	c.execute("INSERT INTO cargas (cliente, contato, custo, preco, data_env, data_cheg) VALUES('MetalForm', '51 27819-2241', 10410.25, \
			18500.21, '2019-05-20', \
			'2019-07-01')")
	conn.commit()
```
O bloco abaixo se refere ao arquivo ``` update_table.py ``` no qual fiz apenas para demonstrar a possibilidade de alterar o banco de dados através da syntax ``` UPDATE ``` e utilizando a chave primária ``` id ``` para localizar a query desejada.

```  
  id = 4
novo_custo = 14315.75
novo_preco = 19002.20
#novo_data_env = '2019-07-30'
#novo_data_cheg = '2019-10-02'

cursor.execute("""
UPDATE cargas
SET custo = ?, preco = ?, data_env = ?, data_cheg = ?
WHERE id = ?
""", (novo_custo, novo_preco, novo_data_env, novo_data_cheg, id))
```

## Construído com
- Linguagem utilizada: **Python 3.7.4**
- Biblioteca utilizada: **SQLite3**
- Ambiente utilizado: IDLE
- Ambiente utilizado para vizualização do banco de dados: [Sqliteman-1.2.2](https://sourceforge.net/projects/sqliteman/files/sqliteman/1.2.2/)
- Software utilizado para criar o executável: [Auto py to exe](https://nitratine.net/blog/post/auto-py-to-exe/)

## Autores

- Daniel Nicácio
