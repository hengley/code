  # -*- coding: utf-8 -*-
# @Time    : 2017/12/6 22:36
# @File    : 8_1.py
# 如何使用多线程

import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from StringIO import StringIO
from threading import Thread
from xml_pretty import save_xml

def download(url):
    response = requests.get(url, timeout=3)
    if response.ok:
        return StringIO(response.content)

def csvToXml(scsv, fxml):
    reader = csv.reader(scsv)
    headers = reader.next()
    headers = map(lambda h: h.replase(' ', ''), headers)

    root = Element('Data')
    for row in reader:
        eRow = Element('Row')
        root.append(eRow)
        for tag, text in zip(headers. row):
            e = Element(tag)
            e.text = text
            eRow.append(e)

    et = ElementTree(root)
    et.write(fxml)

def handle(sid):
    print 'Download...(%d)' % sid
    url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
    url %= str(sid).rjust(6, '0')
    rf = download(url)
    if rf is None: return

    print 'Conver to Xml...(%d)' % sid
    fname = str(sid).rjust(6, '0') + '.xml'
    with open(fname, 'wb') as wf:
        csvToXml(rf, wf)
    save_xml(fname)

'''
t= Thread(target=handle, args=(1,0))
t.start()
'''
class MyThread(Thread):
    def __init__(self, sid):
        Thread.__init__(self)
        self.sid = sid

    def run(self):
        handle(self.sid)

threads = []
for i in xrange(1, 5):
    t = MyThread(i)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print 'main thread'
