# automation

Faire attention au fichier farm_manager.py

Pour le fichier config.yaml:
import glob

l.171/172
user_path = ''.join(glob.glob("/home/*",recursive=True))
farmManager = FarmManager(user_path + "/.programs/handddle_jetson_python/config.yaml")
