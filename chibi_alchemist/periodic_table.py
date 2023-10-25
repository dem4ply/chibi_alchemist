from chibi.atlas import Atlas, Chibi_atlas
from chibi.file import Chibi_path
import json


class Element( Chibi_atlas ):
    def __init__( self, *args, **kw ):
        super().__init__( *args, **kw )
        self.atomic_mass = float( self.atomic_mass )
        self.number = int( self.number )

    @property
    def neutrons( self ):
        return round( self.atomic_mass - self.number )

    @property
    def valence_electron( self ):
        pass

    def _electron_external( self ):
        self.electron_configuration.split( ' ' )


def load_all_elements( path='chibi_alchemist/periodic_table.json' ):
    path = Chibi_path( path )
    data = path.open().read()
    elements = list( Element( d ) for d in data )
    return elements
