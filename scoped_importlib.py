from contextlib import contextmanager
import sys
import importlib


@contextmanager
def scoped_importlib(module_name):
    current_sys_modules = sys.modules.keys()
    imported = importlib.import_module(module_name)
    yield imported
    new_sys_modules = sys.modules.keys()
    for new_created in set(new_sys_modules)-set(current_sys_modules):
        if not new_created.startswith('pkg_resources'):
            del sys.modules[new_created]
    del imported
