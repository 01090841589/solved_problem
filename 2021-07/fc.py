visited = [0] * 101
nums = 1
cal_nums = []
def solution(n, edges):
    def bfs(num, node1, node2):
        global nums
        for i in MAP[num]:
            if i in node1 and num in node1:
                continue
            if i in node2 and num in node2:
                continue
            if visited[i] == 0:
                nums += 1
                visited[i] = 1
                bfs(i, node1, node2)
    def find_nodes(node1, node2):
        global nums
        del cal_nums[:]
        for j in range(n+1):
            visited[j] = 0
        for i in range(n):
            nums = 1
            if not visited[i]:
                visited[i] = 1
                bfs(i, node1, node2)
                print(nums)
                if nums not in cal_nums:
                    if nums < n//3 or nums > (n//3)*2:
                        return
                    cal_nums.append(nums)
                elif nums == n//3:
                    cal_nums.append(nums)
                if sum(cal_nums) == n:
                    return
    answer = []
    MAP = [[] for _ in range(n+1)]
    for node in edges:
        MAP[node[0]].append(node[1])
        MAP[node[1]].append(node[0])
    for i in range(n-1):
        node1 = edges[i]
        find_nodes(node1, [])
        if len(cal_nums) >= 2:
            for j in range(i+1, n-1):
                node2 = edges[j]
                find_nodes(node1, node2)
                if len(cal_nums) == 3:
                    answer = [i, j]
                    answer.sort()
    return answer

print(solution(9, [[0, 2], [2, 1], [2, 4], [3, 5], [5, 4], [5, 7], [7, 6], [6, 8]]))
print(solution(6, [[0, 1], [0, 3], [1, 4], [4, 5], [2, 5]]))
print(solution(12, [[0, 4], [4, 8], [4, 5], [1, 2], [2, 6], [2, 3], [3, 7], [7, 11], [9, 11], [10, 11], [0, 1]]))


