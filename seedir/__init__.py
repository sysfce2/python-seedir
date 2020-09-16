# -*- coding: utf-8 -*-
"""
seedir: Python package for creating and reading folder tree diagrams

@author: Tom Earnest
GitHub: https://github.com/earnestt1234/seedir
"""

#imports for package namespace
from .seedir import (recursive_folder_structure,
                     seedir)

from .fakedir import (FakeDir,
                      FakeFile,
                      FakeItem,
                      fakedir,
                      fakedir_fromstring,
                      populate,
                      randomdir,
                      recursive_add_fakes,
                      recursive_fakedir_structure,
                      sort_fakedir)

from .errors import SeedirError, FakedirError

from .printing import (format_indent,
                       get_styleargs,
                       is_match,
                       STYLE_DICT,
                       words)