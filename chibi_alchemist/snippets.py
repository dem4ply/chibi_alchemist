import re


re_element = re.compile( '[A-Z][a-z]?\d*' )


def split_elements( molecule ):
    return re_element.findall( molecule )
