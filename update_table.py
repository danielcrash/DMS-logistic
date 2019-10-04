import sqlite3
path = r'C:\sqlite\DB2'

conn = sqlite3.connect(path+r'\clientes_carga.db')
cursor = conn.cursor()

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

conn.commit()

print('Dados atualizados com sucesso')

conn.close()
