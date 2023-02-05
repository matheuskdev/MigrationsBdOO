from DatabaseOracle import DatabaseOracle
from LoggerConfig import LoggerConfig
import csv

logger = LoggerConfig.logger

def importCsvFile():
    db = DatabaseOracle('user', 'password', 'host:port', 'database')
    db.connect()

    temp_table = "TEMP_TABLE_CHAMADO_TI"
    query = f'''create table { temp_table }
    (
    ID                   NUMBER not null,
    DT_ABERTURA_CHAMADO           DATE not null,
    COD_USUARIO                   NUMBER not null,
    STATUS_CHAMADO                VARCHAR2(50) not null,
    DT_SOLUCAO_FECHAMENTO_CHAMADO DATE,
    COD_SETOR_GLPI                NUMBER(6) not null,
    NOME_USUARIO_GLPI             VARCHAR2(50),
    NOME_SETOR_GLPI               VARCHAR2(100),
    COD_SETOR_MV                  NUMBER(6),
    NOME_SETOR_MV                 VARCHAR2(100),
    DT_INTEGRACAO                 DATE
    )
    '''
    db.execute(query)
    db.execute_commit(f"grant select, insert, update, delete, references on { temp_table } to YOUR_OPTION")


    input_file = csv.DictReader(open("result.csv", encoding='utf-8'))
    if (input_file != False):
        logger.info('Iniciando o Uploud de dados.')
        for row in input_file:
        # Create INSERT statement
            db.execute_commit(f"INSERT INTO { temp_table } \
                                VALUES (:1, TO_DATE(:2, 'DD/MM/YYYY HH24:MI:SS'), :3, :4, TO_DATE(:5, 'DD/MM/YYYY HH24:MI:SS'), :6, :7, :8, :9, :10, TO_DATE(:11, 'DD/MM/YYYY HH24:MI:SS'))" , 
                                (row['ID'],row['DT_ABERTURA_CHAMADO'],row['COD_USUARIO'], 
                                row['STATUS_CHAMADO'], row['DT_SOLUCAO_FECHAMENTO_CHAMADO'], 
                                row['COD_SETOR_GLPI'],row['NOME_USUARIO_GLPI'], row['NOME_SETOR_GLPI'], 
                                row['COD_SETOR_MV'],row['NOME_SETOR_MV'], row['DT_INTEGRACAO']))
        logger.info(f'Os dados foram inseridos na tabela { temp_table } com sucesso.')


    main_table = 'CHAMADO_GLPI_TI'
    db.execute_commit(f'''MERGE INTO { main_table } m USING { temp_table } t ON 
                                                    (m.ID = t.ID) 
                                                    WHEN NOT MATCHED THEN INSERT 
                                                    (
                                                    m.ID, m.DT_ABERTURA_CHAMADO, 
                                                    m.COD_USUARIO, m.STATUS_CHAMADO, 
                                                    m.DT_SOLUCAO_FECHAMENTO_CHAMADO, m.COD_SETOR_GLPI, 
                                                    m.NOME_USUARIO_GLPI, m.NOME_SETOR_GLPI, 
                                                    m.COD_SETOR_MV, m.NOME_SETOR_MV, m.DT_INTEGRACAO 
                                                    ) 
                                                    VALUES 
                                                    (
                                                    t.ID, t.DT_ABERTURA_CHAMADO, 
                                                    t.COD_USUARIO, t.STATUS_CHAMADO, 
                                                    t.DT_SOLUCAO_FECHAMENTO_CHAMADO, t.COD_SETOR_GLPI, 
                                                    t.NOME_USUARIO_GLPI, t.NOME_SETOR_GLPI, 
                                                    t.COD_SETOR_MV, t.NOME_SETOR_MV, t.DT_INTEGRACAO 
                                                    )''')                                                                             
    logger.info(f'Os dados foram inseridos na tabela { main_table } com sucesso.')


    db.execute_commit(f"DROP TABLE { temp_table }")
    logger.warning('Tabela temporaria apagada com sucesso.')
    db.close()