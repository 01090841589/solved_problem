import math

from linkedgraph import LinkedGraph
from linkedstack import LinkedStackNode
from linkedstack import LinkedStack

class PrimGraphEdge:
    def __init__(self, fromNodeID, toNodeID, weight):
        self.fromNodeID = fromNodeID
        self.toNodeID = toNodeID
        self.weight = weight

# Prim 알고리즘
def mstPrim(pGraph, startNodeID):
    pReturn = None
    pSelected = None
    i = 0
    nodeCount = 0
    mstNodeCount = 0
    fromNodeID = 0
    minWeightEdge = None

    if (pGraph == None):
        print("Graph is None")
        return pReturn

    nodeCount = pGraph.nodeCount
    pReturn = LinkedGraph(LinkedGraph.LINKED_GRAPH_TYPE_UNDIRECT, nodeCount)

    pSelected = []
    for i in range(pGraph.nodeCount):
        pSelected.append(0)

    pSelected[startNodeID] = 1
    mstNodeCount = 1

    while (mstNodeCount < nodeCount):
        minWeightEdge = PrimGraphEdge(0, 0, math.inf)

        for i in range(nodeCount):
            if (pSelected[i] == 1):
                fromNodeID = i
                getMinWeightEdge(pGraph, pReturn, fromNodeID, minWeightEdge)

        pReturn.addEdgeLG(minWeightEdge.fromNodeID, minWeightEdge.toNodeID, minWeightEdge.weight)
        pSelected[minWeightEdge.toNodeID] = 1
        mstNodeCount = mstNodeCount + 1

        print("[%d], 최소 가중치: (%d, %d)-> %d, 노드 %d 추가" % (mstNodeCount, minWeightEdge.fromNodeID, minWeightEdge.toNodeID,minWeightEdge.weight, minWeightEdge.toNodeID))

    return pReturn


def checkEdge(pGraph, fromNodeID, toNodeID):
    ret = False
    pEdgeList = None
    pEdgeNode = None

    if (pGraph != None):
        pEdgeList = pGraph.ppAdjEdge[fromNodeID]
        if (pEdgeList != None):
            for pEdgeNode in pEdgeList:
                if (pEdgeNode.toNodeID == toNodeID):
                    ret = True
                    break
    return ret

# 정점(fromNodeID)과 연결된 간선들 중,
# 가중치가 가장 작으면서 순환을 발생시키지 않는 간선을 선택.
def getMinWeightEdge(pGraph, pMST, fromNodeID, pMinWeightEdge):
    pListNode = None
    isCycle = False
    isAlready = False
    pEdgeList = pGraph.ppAdjEdge[fromNodeID]

    # pListNode: V(T)에 부속된 간선들 중 하나를 선택.
    for pListNode in pEdgeList:
        toNodeID = pListNode.toNodeID
        weight = pListNode.weight

        # 최소값인지 점검.
        if (pListNode.weight < pMinWeightEdge.weight):
            # 기존의 E(T)에 속한 간선인지 점검
            isAlready = checkEdge(pMST, fromNodeID, toNodeID)
            if (False == isAlready):
                # 순환을 발생시키는지 점검
                isCycle = checkCycle(pMST, fromNodeID, toNodeID)

            if (False != isCycle):
                print("순환 발생: (%d,%d).%d, Skip" % (fromNodeID, toNodeID, pListNode.weight))

            # 기존에 이미 E(T)에 속한 간선이 아니면서,
            # 순환을 발생시키지 않는,
            # 최소 가중치 간선을 선택.
            if (isAlready == False and isCycle == False):
                pMinWeightEdge.fromNodeID = fromNodeID
                pMinWeightEdge.toNodeID = toNodeID
                pMinWeightEdge.weight = weight

# 간선 추가로 인해 순환이 발생하는 지 검사.
# 기존에 경로가 있었다면, 순환이 발생한다.
# 기존의 깊이우선탐색(DFS)를 사용.
def checkCycle(pGraph, fromNodeID, toNodeID):
    pReturn = 0
    i = 0
    vertextID = 0
    pStack = None
    pStackNode = None
    pListNode = None
    pVisited = None

    if (pGraph == None):
        return pReturn

    pStack = LinkedStack()

    # 초기화.
    pVisited = []
    for i in range(pGraph.nodeCount):
        pVisited.append(0)

    pVisited[fromNodeID] = 1
    pStack.pushLS(fromNodeID)

    while (pStack.isLinkedStackEmpty() == False):
        pStackNode = pStack.popLS()
        if (pStackNode != None):
            vertextID = pStackNode.data
            if (vertextID == toNodeID):
                # print("(%d,%d)-기존에 경로가 존재합니다." % (fromNodeID, toNodeID))
                pReturn = True
                break

            for pListNode in pGraph.ppAdjEdge[vertextID]:
                vertexID = pListNode.toNodeID
                if (pVisited[vertexID] == 0):
                    pVisited[vertexID] = 1
                    pStack.pushLS(vertexID)

    return pReturn
