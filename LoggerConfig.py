import logging

class LoggerConfig():

    log_format = 'DtTm: %(asctime)s -- Lvl: %(levelname)s -- Arqv: %(filename)s -- Msg:%(message)s'
    logging.basicConfig(filename='chamado_ti.log',
                        # w -> sobrescreve o arquivo a cada log
                        # a -> não sobrescreve o arquivo
                        filemode='a',
                        level=logging.DEBUG,
                        format=log_format)
    logger = logging.getLogger('root')

