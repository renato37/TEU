class Node:
    def __init__(self, id, title='', text='', image='', parentId=None):
        self.id = id
        self.title = title
        self.text = text
        self.image = image
        self.parentId = parentId
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def getChild(self, id):
        for i in self.children:
            if i.id == id:
                return i

    def setTitle(self, title):
        self.title = title

    def setText(self, text):
        self.text = text

    def setImage(self, image):
        self.image = image

    def toList(self, l, dic):
        l.append(dic[self.id].__dict__)
        for c in self.children:
            l = dic[c].toList(l, dic)
        return l

    def toDict(self, d, dic):
        d[self.id] = dic[self.id].__dict__
        for c in self.children:
            d = dic[c].toDict(d, dic)
        return d
