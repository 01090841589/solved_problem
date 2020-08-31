from linkedgraph import LinkedGraph
import mst_prim

pG3 = None
pMST1 = None

# 그래프 생성
pG3 = LinkedGraph(LinkedGraph.LINKED_GRAPH_TYPE_UNDIRECT, 6)
if (pG3 != None) :
    # 그래프 초기화: 간선 추가
    pG3.addEdgeLG(0, 1, 4)
    pG3.addEdgeLG(0, 2, 3)
    pG3.addEdgeLG(1, 2, 2)
    pG3.addEdgeLG(2, 3, 1)
    pG3.addEdgeLG(3, 4, 1)
    pG3.addEdgeLG(3, 5, 5)
    pG3.addEdgeLG(4, 5, 6)
    print("G3:")
    pG3.displayGraphLG()

    # Prim 알고리즘으로 MST 생성
    print("\nPrim MST:")
    pMST1 = mst_prim.mstPrim(pG3, 1)
    pMST1.displayGraphLG()