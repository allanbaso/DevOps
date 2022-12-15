import xlrd

# Open the Workbook
workbook = xlrd.open_workbook("Sample_moves.xls")

# Open the worksheet
worksheet = workbook.sheet_by_index(0)

# Iterate the rows and columns
for i in range(0, 16):
    for j in range(0, 1):
        # Print the cell values with tab space
        print(worksheet.cell_value(i, j), end='\t')
    print('')