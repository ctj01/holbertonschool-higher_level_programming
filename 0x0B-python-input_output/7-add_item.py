#!/usr/bin/python3
from sys import argv
save_json = __import__('5-save_to_json_file.py').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    lista = load_json(filename)
except (ValueError, FileNotFoundError):
    lista = []
for args in argv[1:]:
    lista.append(args)
save_json(lista, filename)
