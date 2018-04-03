#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


import xml.etree.ElementTree as ET

new_xml = ET.Element("personinfolist")   #根节点
personinfo = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"})
name = ET.SubElement(personinfo, "name")
name.text = "Jack"
age = ET.SubElement(personinfo, "age", attrib={"checked": "no"})  #personinfo下有两个节点
sex = ET.SubElement(personinfo, "sex")
age.text = '56'
personinfo2 = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "no"})
name = ET.SubElement(personinfo2, "name")
name.text = "Oldboy Ran"
age = ET.SubElement(personinfo2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)   #写入

ET.dump(new_xml)  # 打印生成的格式