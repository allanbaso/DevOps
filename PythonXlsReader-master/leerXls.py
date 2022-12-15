import xlrd

book = xlrd.open_workbook("Book4.xls")
sh = book.sheet_by_index(0)
for col in range(sh.ncols):
    for rx in range(sh.nrows):
        fila = sh.row_values(rx)
        new_list = [word.strip() for word in fila]#se le quita los espacios y caracteres demas
if "HOLDPROD" in new_list:
    #print("El nombre del elmento #"+str(rx+1)+" de la lista es : "+str(new_list))
    if "H" in new_list:
        print('Listas para borrar Libman2 con stage 2')
        #se agrega cod para borrar con stage H
    else:
        print('Lista para borrar en Libman2')
        #se agrega cod para borrar en lib2
if "PROD" in new_list:
    if "H" in new_list:
        print('No existe stage H en Libman1')
    else:
        print('Lista para borrar en Libman1')
        #se agrega cod para borrar en lib1