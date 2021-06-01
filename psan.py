import sys

pattern = ['a1','a2','a3','a4','a5','a6','a7','a8','a9','a0','b1','b2','b3','b4','b5','b6','b7','b8','b9','b0','c1','c2','c3','c4','c5','c6','c7','c8','c9','c0','d1','d2','d3','d4','d5','d6','d7','d8','d9','d0','e1','e2','e3','e4','e5','e6','e7','e8','e9','e0','f1','f2','f3','f4','f5','f6','f7','f8','f9','f0','g1','g2','g3','g4','g5','g6','g7','g8','g9','g0','h1','h2','h3','h4','h5','h6','h7','h8','h9','h0','i1','i2','i3','i4','i5','i6','i7','i8','i9','i0','j1','j2','j3','j4','j5','j6','j7','j8','j9','j0']

try:
    sys.argv[1]
except:
    sys.exit(': Usage '+sys.argv[0]+' *scirpt.psan')
try:
    sco = open(sys.argv[1], 'r')
except FileNotFoundError:
    raise FileNotFoundError('File not found')
sc = sco.read().splitlines()
sco.close()
if sc[0] == 'lp':
    loop = True
elif sc[0] == 'fr':
    loop = False
else:
    raise SyntaxError('Invalid Start')
exec('a = '+sc[1])
base = ''
nl = False
for i in pattern:
    if nl:
        base += '\n'
        nl = False
    try:
        if a[i]:
            base += '3'
    except KeyError:
        base += ' '
    else:
        base += ' '
    if i.endswith('0'):
        nl = True
print(base)
