# -*- coding: utf-8 -*-
import argparse
import sys
import json
import sys
import logging
import random
from argparse import ArgumentParser
import urllib3
import itertools

from chibi.file import Chibi_path
from chibi.config import basic_config, load as load_config
from chibi_alchemist.periodic_table import load_all_elements, Element
from chibi_alchemist.snippets import split_elements


logger_formarter = '%(levelname)s %(name)s %(asctime)s %(message)s'

parser = ArgumentParser(
    description="calcula cosas de quimica", fromfile_prefix_chars='@'
)

parser.add_argument(
    "elements", nargs='+', metavar="element",
    help="elementos que quieres usar" )

parser.add_argument(
    "--log_level", dest="log_level", default="INFO",
    help="nivel de log",
)

"""
parser.add_argument(
    "sites", nargs='+', metavar="site",
    help="urls de las series que se quieren descargar" )

parser.add_argument(
    "--only_print", dest="only_print", action="store_true",
    help="define si silo va a imprimir la lista de links o episodios"
)

parser.add_argument(
    "--only_metadata", dest="only_metadata", action="store_true",
    help="se define si solo se queire recolectar los datos y no descargar"
)

parser.add_argument(
    "--only_links", dest="only_print_links", action="store_true",
    help="si se usa solo imprimira las urls"
)

parser.add_argument(
    "--user", '-u', dest="user", default="",
    help="usuario del sitio" )

parser.add_argument(
    "--password", '-p', dest="password", default="",
    help="contrasenna del sitio" )


parser.add_argument(
    "-o", "--output", type=Chibi_path, dest="download_path",
    help="ruta donde se guardara el video o manga" )

parser.add_argument(
    "-config_site", type=Chibi_path, dest="config_site",
    help="python, yaml o json archivo con el usuario y password de cada sitio"
)
"""

parser.add_argument(
    "--ionization", dest="ionization", action="store_true",
    help="imprime tabla de ionizacion"
)

parser.add_argument(
    "--oxidation", dest="oxidation", action="store_true",
    help="imprime oxidacion del elemento"
)

parser.add_argument(
    "--electron_config", dest="electron_config", action="store_true",
    help="imprime la configuracion electronica"
)

def main():
    args = parser.parse_args()
    basic_config( args.log_level )
    elements = load_all_elements()

    by_symbol = { e.symbol: e for e in elements }
    chain_of_elements = map( split_elements, args.elements )
    chain_of_elements = itertools.chain.from_iterable( chain_of_elements )
    #select = ( by_symbol[ e ] for e in args.elements )
    select = ( by_symbol[ e ] for e in chain_of_elements )

    if args.ionization:
        for element in select:
            table = "\t".join( map( str, element.ionization_energies ) )
            output = f"{element.name}\t{table}"
            print( output )

    if args.oxidation:
        for element in select:
            import pdb
            pdb.set_trace()
            table = "\t".join( map( str, element.ionization_energies ) )
            output = f"{element.name}\t{table}"
            print( output )

    if args.electron_config:
        for element in select:
            print( element.electron_configuration )

    for element in select:
        print( element.name )

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
