from lib4 import ege_n4

word = 'ЭТОРОФЛ'
alf = dict.fromkeys('ЭТОРОФЛ', '')
alf['Э'] = '110'
alf['Л'] = '10'
alf['Т'] = '111'

print(ege_n4(word, alf))
