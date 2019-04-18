class AnalysTree:

    def __init__(self, value):
        self.root = [value, [], []]

    def insertLeft(self, newBranch):
        t = self.root.pop(1)
        if len(t) > 1:
            self.root.insert(1,[newBranch,t,[]])
        else:
            self.root.insert(1,[newBranch, [], []])
        return self.root

    def insertRight(root,newBranch):
        t = root.pop(2)
        if len(t) > 1:
            self.root.insert(2,[newBranch,[],t])
        else:
            self.root.insert(2,[newBranch,[],[]])
        return self.root

    def getRootVal(root):
        return self.root[0]

    def setRootVal(self, newVal):
        self.root[0] = newVal

    def getLeftChild(self):
        return self.root[1]

    def getRightChild(self):
        return self.root[2]
