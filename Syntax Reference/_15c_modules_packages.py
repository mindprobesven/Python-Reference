#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Modules - Packages
#
# Packages are a way of structuring Python’s module namespace by using “dotted module names”.
#
# Module packages can be structured in directories, similar to this:

""" 
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ... 
"""

# The __init__.py files are required to make Python treat directories containing the file as packages.
# In the simplest case, __init__.py can just be an empty file, but it can also execute initialization code for the 
# package or set the __all__ variable
#
# ----------------------------------------------------------------------------------------------------------------

# Import individual modules from the package.
# This loads the submodule sound.effects.echo. It must be referenced with its full name.
import sound.effects.echo

# This loads the submodule echo and makes it available without its package prefix
from sound.effects import echo

# This loads the submodule echo, but this makes its function echofilter() directly available
from sound.effects.echo import echofilter

# Relative imports
#
# You can also write relative imports, with the from module import name form of import statement. These imports use 
# leading dots to indicate the current and parent packages involved in the relative import. From the "surround" module 
# for example, you might use
from . import echo
from .. import formats
from ..filters import equalizer