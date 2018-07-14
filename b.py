import sys
NAME = 'b'
assert 'dog' not in sys.modules
import dog
assert 'dog' in sys.modules
