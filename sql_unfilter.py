import sys

input = sys.argv[1]

input = input.replace(' ', '/**/')
input = input.replace(',', '/*!,*/')
if 'select' in input:
    input = input.replace('select','selSELECTect')
elif 'SELECT' in input:
    input = input.replace('SELECT','selSELECTect')
if 'union' in input:
    input = input.replace('union','uniUNIONon')
elif 'UNION' in input:
    input = input.replace('UNION','uniUNIONon')

print input
