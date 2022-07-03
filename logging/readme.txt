Dans le fichier python :
 - modifier le LOG_FILE -> emplacement du fichier log, mettre par ex : "/var/log/handddle_jetson_python/farm_manager/farm_manager.log"
 - modifier le file_logger -> mettre le nom souhaité
 
 
 import logging
 from logging.handlers import TimedRotatingFileHandler

LOG_FILE = ""
FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")

file_logger = logging.getLogger('farm_manager')
file_logger.setLevel(logging.DEBUG)

file_handler = TimedRotatingFileHandler(LOG_FILE, when="midnight", interval=1, backupCount=7)
file_handler.setFormatter(FORMATTER)

file_logger.addHandler(file_handler)
file_logger.propagate = False






pour 'logger' :
 - file_logger.info('------------------------------')
 - info / warning / debug / critical / error





Creer les dossiers suivants (/var/log/handddle_jetson_python/):
- client
- commands
- datas
- demo
- farm_manager
- gui
- master
- message
- scanner
- server
- slave
- tlv_message
- watchdog
