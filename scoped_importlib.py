from contextlib import contextmanager
import sys
import importlib

@contextmanager
def scoped_importlib(module_name):
    current_sys_modules = sys.modules.keys()
    try:
        imported = importlib.import_module(module_name)
        yield imported
    finally:
        new_sys_modules = sys.modules.keys()
        for new_created in set(new_sys_modules)-set(current_sys_modules):
            del sys.modules[new_created]
        del imported
