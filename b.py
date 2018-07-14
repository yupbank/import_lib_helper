import sys
NAME = 'b'
assert 'tensorflow' not in sys.modules
assert 'dog' not in sys.modules
import dog
assert 'dog' in sys.modules
