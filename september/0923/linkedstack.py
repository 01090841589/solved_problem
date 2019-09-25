class LinkedStackNode:
    def __init__(self, data, pLink):
        self.data = data
        self.pLink = pLink
        return

class LinkedStack:
    def __init__(self):
        self.currentCount = 0
        self.pTop = None
        return

    def isLinkedStackFull(self):
        return False

    def isLinkedStackEmpty(self):
        ret = False
        if (self.currentCount == 0):
            ret = True
        return ret

    def pushLS(self, data):
        ret = 0
        pNode = LinkedStackNode(data, self.pTop)
        self.pTop = pNode
        self.currentCount = self.currentCount + 1
        return True

    def popLS(self):
        pReturn = None
        if (self.isLinkedStackEmpty() == False):
            pReturn = self.pTop
            self.pTop = pReturn.pLink
            pReturn.pLink = None
            self.currentCount = self.currentCount - 1
        return pReturn

    def peekLS(self):
        pReturn = None
        if (self.isLinkedStackEmpty() == False):
            pReturn = self.pTop
        return pReturn
