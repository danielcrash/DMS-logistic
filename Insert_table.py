import sqlite3
path = r'C:\sqlite\DB2'

conn = sqlite3.connect(path+r'\clientes_carga01.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE cargas (id integer not null primary key autoincrement, \
                        cliente text not null, contato text not null, custo real not null, preco real not null, \
                        data_env text not null, data_cheg text not null)')

create_table()

def dateentry():
	c.execute("INSERT INTO cargas (cliente, contato, custo, preco, data_env, data_cheg) VALUES('SOS Logistics', '21 24489-6491', 15750.15, \
			30800.15, '2019-04-14', \
			'2019-04-14')")
	c.execute("INSERT INTO cargas (cliente, contato, custo, preco, data_env, data_cheg) VALUES('MetalForm', '51 27819-2241', 10410.25, \
			18500.21, '2019-05-20', \
			'2019-07-01')")
	c.execute("INSERT INTO cargas (cliente, contato, custo, preco, data_env, data_cheg) VALUES('Food Solutions', '13 29681-1796', 10410.25, \
			18500.55, '2019-05-20', \
			'2019-07-01')")
	c.execute("INSERT INTO cargas (cliente, contato, custo, preco, data_env, data_cheg) VALUES('Yellow Dreams', '31 99813-6491', 10410.25, \
			18500.37, '2019-05-20', \
			'2019-07-01')")
	c.execute("INSERT INTO cargas (cliente, contato, custo, preco, data_env, data_cheg) VALUES('Icarus Importação', '20 92818-1425', 10440.17, \
			17770.65, '2019-11-03', \
			'2019-12-25')")
	c.execute("INSERT INTO cargas (cliente, contato, custo, preco, data_env, data_cheg) VALUES('Plastic Industry', '55 33333-5566', 24275.55, \
			33722.55, '2018-10-03', \
			'2019-01-12')")
	c.execute("INSERT INTO cargas (cliente, contato, custo, preco, data_env, data_cheg) VALUES('Universal Wood Solutions', '32 48712-8511', 5450.15, \
			8100.65, '2017-06-13', \
			'2017-07-25')")
	conn.commit()

dateentry()
print('Tabela criada com sucesso!')

