# -*- coding:utf-8 -*-

from ConfigParser import ConfigParser
from ProjectVar.var import page_object_repository_path

class ParsePageObjectRepositoryConfig(object):
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(page_object_repository_path)

    #获取某个section，所有的key和value，用字典方式返回
    def getItemsFromSection(self,sectionName):
        print self.cf.items(sectionName)
        return dict(self.cf.items(sectionName))

    #获取某一个具体的选项对应的value
    def getOptionValue(self,sectionName,optionName):
        return self.cf.get(sectionName,optionName)