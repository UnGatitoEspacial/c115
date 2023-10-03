import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler

from_dir ="C:/Users/gatop/Downloads"
to_dir ="C:/Users/gatop/Desktop"

dir_tree={
    "Image_Files":['.jpg','.jpeg','.png','.gif','.jfif'],
    "Video_Files":['.mpg','.mp2','.mpeg','.mpe','.mpv','.mp4','.m4v','.avi','.mov'],
    "Document_Files":['.ppt','.xls','.xlsx','.csv','.pdf','.txt'],
    "Setup_Files": ['.exe','.bin','.cmd','.msi','.dmg']
}

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
# bucle for que evalua el tiempo de respuesta

        time.sleep(1)
        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value: 

                file_name = os.path.basename(event.src_path)

                print("Descargando" + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):

                    print("Directorio Existe...")
                    print("Moviendo " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print ("Haciendo directo...")
                    os.makedirs(path2)
                    print("Moviendo" + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

# Iniciar la Clase Event Handler
event_handler = FileMovementHandler()

# Inicializar Observer
observer = Observer()

# Programar Observer
observer.schedule(event_handler, from_dir, recursive=True)

#Iniciar Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("ejecutando...")
except KeyboardInterrupt:
    print("¡detenido!")
    observer.stop()