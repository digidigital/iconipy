from typing import List
import os
import sys

# Add the some directories to the Python path
sys.path.insert(0, os.path.dirname(__file__))
                                   
def get_hook_dirs()-> List[str]:
    return [os.path.join(os.path.dirname(__file__), 'pyinstaller_hooks')]
