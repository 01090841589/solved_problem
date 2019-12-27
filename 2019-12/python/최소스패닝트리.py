import sys
sys.stdin = open("최소스패닝트리.txt")
#부모 노드를 찾는 함수
def getParent(arr, n) :
    if arr[n] == n : return n
    return getParent(arr, arr[n])


#두 부모 노드를 합치는 함수
def unionParent(arr, n_1, n_2) :
    a = getParent(arr, n_1)
    b = getParent(arr, n_2)
    if a < b : arr[b] = a
    else : arr[a] = b

#같은 부모를 가지는지 확인
def findParent(arr, n_1, n_2) :
    a = getParent(arr, n_1)
    b = getParent(arr, n_2)
    if a == b : return 1
    else : return 0

edges = []
parent = {}
V, E = map(int, input().split())

#간선에 대한 정보를 입력받는다.
#문제에서 노드1, 노드2, 간선의 가중치 순으로 입력이 주어진다.
for _ in range(E) :
    edges.append([*map(int, input().split())])

#부모노드 dict를 초기화 한다.
#모든 노드가 자기 자신을 부모노드로 지정하게된다.
for i in range(V) :
    parent[i + 1] = i + 1

#가중치의 오름차순으로 간선을 정렬한다.
edges.sort(key = lambda val : val[2])

MST = []
#Kruskal's  Algorithm
for e in edges :
    v, u, w = e
    #두 노드의 부모노드가 같은지 비교하게 된다.
    if findParent(parent, v, u) == 0:
    #부모노드가 같지 않다면 두 노드를 연결해주고, 더 낮은 숫자를 가진 노드로 부모노드를 변경해준다.
        unionParent(parent, v, u)
        #최소 비용 신장트리의 결과 리스트에 현재 간선의 정보를 추가해준다.
        MST.append(e)
print(sum([w for v, u, w in MST]))