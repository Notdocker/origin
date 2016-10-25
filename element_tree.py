import os

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

class DictObj(object):
    # �̳�object
    def __init__(self,map):
        self.map = map

    def __setattr__(self, name, value):
        if name == 'map':
             object.__setattr__(self, name, value)
             # ���ö�����������
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
#     ·��

tree = ET.parse(file)
root = tree.getroot()
# ElementTree�õ�ȫ������
for child_of_root in root:
    if(child_of_root.tag == 'node'):
        book = DictObj(child_of_root.attrib)
# ɸѡ������
