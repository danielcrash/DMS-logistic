import sqlite3
path = r'C:\sqlite\DB2'
choice = 0
while choice != 6:
    print ('============================================================')
    print ('         BEM-VINDO AO BANCO DE DADOS DMS LOGISTICS         ')
    print ('============================================================')
    print ('============================================================')
    print ('                DIGITE O OPÇÃO DESEJADA')
    print ('      CÓD [1] PARA INSERIR NOVAS SOLICITAÇÕES DE CARGAS     ')
    print ('      CÓD [2] TODAS AS SOLICITAÇÕES DE CLIENTES E CONTATO')
    print ('      CÓD [3] TOTAL DE CUSTOS EFETUADOS')
    print ('      CÓD [4] TOTAL DE LUCRO OBTIDO')
    print ('      CÓD [5] DELETAR DADO ESPECÍFICO')
    print ('      CÓD [6] SAIR DO PROGRAMA')
    print ('============================================================')
    choice = int(input('\nDigite a opção: '))

    if choice==1:
    
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

    elif choice==2:
        print('   NOME               CONTATO')
        conn = sqlite3.connect('clientes_carga01.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT cliente, contato FROM cargas;""")
        for linha in cursor.fetchall():
            print(linha)
        print('\n\n\n\n')
    elif choice==3:
        print('     CUSTOS')
        conn = sqlite3.connect('clientes_carga01.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT custo FROM cargas;""")
        for linha in cursor.fetchall():
            print('R$ %.2f'%linha)
        print('\nTOTAL DE CUSTOS')
        conn = sqlite3.connect('clientes_carga01.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT SUM(custo) FROM cargas;""")
        for linhas in cursor.fetchall():
            print('R$ %.2f'%linhas)
        print('\n\n\n\n')
    elif choice==4:
        print('    PREÇOS')
        conn = sqlite3.connect('clientes_carga01.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT preco FROM cargas;""")
        for linha in cursor.fetchall():
            print('R$ %.2f'%linha)
        print('    CUSTOS')
        conn = sqlite3.connect('clientes_carga01.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT custo FROM cargas;""")
        for linha1 in cursor.fetchall():
            print('R$ %.2f'%linha1)
        conn = sqlite3.connect('clientes_carga01.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT SUM(preco) - SUM(custo) FROM cargas;""")
        for linha2 in cursor.fetchall():
            print('\nTOTAL DE LUCRO')
            print('R$ %.2f'%linha2)
        print('\n\n\n\n')
    elif choice==5:
        print('\nID    CLIENTE        CONTATO')
        conn = sqlite3.connect('clientes_carga01.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT id, cliente, contato FROM cargas;""")
        for linha in cursor.fetchall():
            print(linha)
        conn = sqlite3.connect('clientes_carga01.db')
        cursor = conn.cursor()
        id_cliente = input('\nDigite o ID a ser DELETADO: ')
        cursor.execute("""DELETE FROM cargas WHERE id = ?""", (id_cliente,))
        conn.commit()
        print('Registro excluido com sucesso!')
        print('\n\n\n\n')
print('Fim do programa! Muito Obrigado!')
