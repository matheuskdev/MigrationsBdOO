from DatabaseMySQL import DatabaseMySQL
from LoggerConfig import LoggerConfig
import pandas as pd



def generateCsvFile():
    logger = LoggerConfig.logger
    db = DatabaseMySQL('user','password','host','database')
    db.connect()

    query = ('''SELECT 
                        tkt.id ID,
                        DATE_FORMAT(STR_TO_DATE(tkt.date, '%Y-%m-%d %H:%i:%s'), 
                                    '%d-%m-%Y %H:%i:%s') as DT_ABERTURA_CHAMADO,
                        tkt.users_id_recipient COD_USUARIO,
                CASE 
                        WHEN tkt.status = 1 THEN 'Novo'
                        WHEN tkt.status = 2 THEN 'Atribuido/Em Atendimento'
                        WHEN tkt.status = 5 THEN 'Solucionado'
                        WHEN tkt.status = 6 THEN 'Fechado'
                        WHEN tkt.is_deleted = 1 THEN 'Chamado Deletado'
                END     STATUS_CHAMADO,

                        DATE_FORMAT(STR_TO_DATE(tkt.date_mod, '%Y-%m-%d %H:%i:%s'),
                                '%d-%m-%Y %H:%i:%s') AS DT_SOLUCAO_FECHAMENTO_CHAMADO,

                        tkt.locations_id COD_SETOR_GLPI,
                        usu.name NOME_USUARIO_GLPI,
                        loc.name NOME_SETOR_GLPI,

                        DATE_FORMAT(STR_TO_DATE(sysdate(), '%Y-%m-%d %H:%i:%s'), 
                                    '%d-%m-%Y %H:%i:%s') as DT_INTEGRACAO

                FROM 
                        glpi_tickets   tkt,
                        glpi_users     usu,
                        glpi_locations loc  

                WHERE   tkt.users_id_recipient = usu.id
                AND     tkt.locations_id = loc.id  
                AND 	tkt.is_deleted != 1
                AND tkt.status IN (5,6)
                AND tkt.date_mod IS NOT NULL  
                ORDER BY tkt.id''')

            
    df = pd.read_sql(query, db.conn)
    try:
        if ( df.to_csv("result.csv",
            encoding = 'utf-8',
            index = False, sep= ',', header= True) != False ) :
            logger.info('Arquivo gerado com sucesso.')
        else:
            logger.warning('Algo nao saiu como o esperado.')
    except ValueError:
        logger.warning('Erro.')
    db.close()
    logger.info("Conexao MySQL fechada")