import os

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

class DictObj(object):
    # 继承object
    def __init__(self,map):
        self.map = map

    def __setattr__(self, name, value):
        if name == 'map':
             object.__setattr__(self, name, value)
             # 设置读入对象的属性
             return
        self.map[name] = value

    def __getattr__(self,name):
        v = self.map[name]
        if isinstance(v,(dict)):
            return DictObj(v)
        if isinstance(v, (list)):
            r = []
            for i in v:
                r.append(DictObj(i))
            return r
        else:
            return self.map[name]

    def __getitem__(self,name):
        return self.map[name]

if __name__ == '__main__':
    file = os.path.abspath('TX2015.xml')
#     路径

tree = ET.parse(file)
root = tree.getroot()
# ElementTree得到全部内容
for child_of_root in root:
    if(child_of_root.tag == 'node'):
        book = DictObj(child_of_root.attrib)
# 筛选，对象化
