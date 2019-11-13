# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 22:27
# @File    : 6_4.py
# 读写excel文件

import xlrd, xlwt

rbook = xlrd.open_workbook('C:\Users\cyf\Desktop\Demo.xlsx')
rsheet = rbook.sheet_by_index(0)
nc = rsheet.ncols
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, u'总分', None)

for row in xrange(1, rsheet.nrows):
    n = sum(rsheet.row_values(row, 1))
    rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, n, None)

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyxf('align: vertical center, horizontal center')

for r in xrange(rsheet.nrows):
    for c in xrange(rsheet.ncols):
        wsheet.write(r, c, rsheet.cell_value(r, c), style)

wbook.save('C:\Users\cyf\Desktop\Demo1.xls')