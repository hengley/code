# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 20:54
# @File    : 8_2.py
# 线程之间的通讯(生产者和消费者模式）

import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from StringIO import StringIO
from threading import Thread
from Queue import Queue

class DownloadThread(Thread):
    def __init__(self, sid, queue):
        Thread.__init__(self)
        self.sid = sid
        self.queue = queue
        self.url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
        self.url %= str(sid).rjust(6, '0')

    def download(self, url):
        response = requests.get(url, timeout=3)
        if response.ok:
            return StringIO(response.content)

    def run(self):
        print 'Download', self.sid
        data = self.download(self.url)
        self.queue.put((self.sid, data))

class ConvertThread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def csvToXml(self, scsv, fxml):
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

    def run(self):
        while True:
            sid, data = self.queue.get()
            print 'Convert Thread', sid
            if sid == -1:
                break
            if data:
                fname = str(sid).rjust(6, '0') + '.xml'
                with open(fname, 'wb') as wf:
                    self.csvToXml(data, wf)

q = Queue()
dThreads = [DownloadThread(i, q) for i in xrange(1,11)]
cThread = ConvertThread(q)
for t in dThreads:
    t.start()
cThread.start()

for t in dThreads:
    t.join()
q.put((-1, None))

print 'main thread'
