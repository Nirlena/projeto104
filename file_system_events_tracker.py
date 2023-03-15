import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'C:/Users/eaevi/OneDrive/Área de Trabalho/Pastas/Gamecode/baixados'

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f'Olá, {event.src_path} Foi criado!')
    def on_deleted(self, event):
         print(f'Opa, Alguém excluiu {event.src_path}!')
    def on_moved(self, event):
        print(f'Opa,{event.src_path} Alguém moveu o arquivo!')
    def on_modified(self, event):
        print(f'Opa, alguém modificou o arquivo {event.src_path}!')

event_handler = FileMovementHandler()

observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()
