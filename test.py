import sys
from io import StringIO

# Teste para Smartphone
sys.stdin = StringIO('Smartphone\n9\n')
with open('main.py', 'r') as f:
  exec(f.read())

# Teste para Televisor
sys.stdin = StringIO('Televisor\n6\n')
with open('main.py', 'r') as f:
  exec(f.read())