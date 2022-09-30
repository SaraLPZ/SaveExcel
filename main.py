import xlwt

myfile = xlwt.Workbook()
sheet1 = myfile.add_sheet("Hola")
sheet1.write(0,0, "Sara")
myfile.save("sample.xls")


