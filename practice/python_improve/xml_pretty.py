# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 22:55
# @File    : xml_pretty.py
# Make xml to be pretty

import re

def save_xml(self, file_name):
    xml_str = self.m_dom.toprettyxml(indent="    ")
    repl = lambda x: ">%s</" % x.group(1).strip() if len(x.group(1).strip()) != 0 else x.group(0)
    pretty_str = re.sub(r'>\n\s*([^<]+)</', repl, xml_str)
    open(file_name, 'w').write(pretty_str)