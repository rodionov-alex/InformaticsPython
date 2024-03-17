from lib4 import ege_n4

word = 'ТЕНСИВ'
alf = dict.fromkeys('ТЕНСИВ', '')
alf['Т'] = '010'
alf['Е'] = '0100'
alf['С'] = '01000'
alf['И'] = '0110'
alf['В'] = '1110'

print(ege_n4(word, alf, -1))