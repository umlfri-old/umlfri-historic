from ProjectNode import CProjectNode

class CProjekt:
    def __init__(self, file):
        self.root = None
    
    def Find(self,node):
        lst.append(node)
        while len(lst) > 0:
            tmp = lst.pop(0)
            lst += tmp.GetChilds()
            if tmp is node:
                return tmp
        else:
            return None


    def AddNode(self, node, parent):
        parent.AddChild(node)

    def MoveNode(self, node, newParent):
        node.GetParent(node).RemoveChild(node)
        node.SetParent(newParent)
        newParent.AddChild(node)

    def RemoveNode(self, node):
        node.GetParent(node).RemoveChild(node)
