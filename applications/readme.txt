PATH = /usr/local/handddle/applications


Raccourcis sur le bureau pour accéder sous forme d'application à la page de l'app en cas de pb : (handddle.desktop) en plein écran sans possibilité de supprimer le plein écran (sauf ALT+F4). Pareil pour la page localhost:8080 (maintenance.desktop)


Attention : il n'y a pas google-chrome sur les jetson nano mais chromium-browser


Pour le créer:
- créer un fichier desktop (raccourci),

- lancer la commande : 
gio set handddle.desktop metadata::trusted true
gio set maintenance.desktop metadata::trusted true

- puis : 
chmod u+x handddle.desktop
chmod u+x maintenance.desktop
