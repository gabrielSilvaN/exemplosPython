import dbm

arquivo = dbm.open('banco', 'c')

arquivo['nome'] = 'Gabriel'
arquivo['idade'] = '23'
arquivo['sexo'] = 'M'


arquivo.close()
