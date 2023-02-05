from generateCSV import generateCsvFile
from importCSV import importCsvFile
from LoggerConfig import LoggerConfig
from datetime import date

logger = LoggerConfig.logger
if int(date.today().strftime('%d')) == 5:
    generateCsvFile()
    importCsvFile()
else:
    logger.error(f"Nada foi executado, ainda estamos no dia {date.today().strftime('%d')} ")
