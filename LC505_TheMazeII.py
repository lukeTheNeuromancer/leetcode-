# LC 505. 迷宫 II (The Maze II) 是 LC 490 的直接进阶版本。

# 不同于 LC 490 只需用普通 BFS/DFS 判断“能否到达”，本题要求计算到达终点的最短总滚动步数（若无法到达则返回 -1）。

# 核心算法：Dijkstra 算法
# 我们将迷宫建模为图：

# 节点：小球可以停靠的位置 (r, c)。

# 边权：从当前停靠点往某个方向一直滚到撞墙所经过的步数。

# 我们使用 优先队列 (Min-Heap) 维护元组 (dist, r, c)，每次优先弹出当前总步数最短的点进行拓展，同时维护一个 distance 矩阵进行松弛操作 (Relaxation)。


import heapq

class Solution:
    def shortestDistance(self, maze: list[list[int]], start: list[int], destination: list[int]) -> int:
        m, n = len(maze), len(maze[0])
        start_r, start_c = start
        dest_r, dest_c = destination
        
        # distance[r][c] 记录从起点到达 (r, c) 的最短步数，初始为无穷大
        distance = [[float('inf')] * n for _ in range(m)]
        distance[start_r][start_c] = 0
        
        # 优先队列 (min-heap): (d, r, c)
        heap = [(0, start_r, start_c)]
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while heap:
            d, r, c = heapq.heappop(heap)
            
            # 如果到达终点，由于优先队列的性质，此时得到的肯定是绝对最短路径
            if r == dest_r and c == dest_c:
                return d
                
            # 剪枝：如果弹出的步数大于当前记录的最短步数，直接跳过
            if d > distance[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r, c
                step_count = 0
                
                # 沿当前方向一直滚动，直到撞墙或越界
                while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                    step_count += 1
                    
                # 松弛操作：如果通过当前路径到达 (nr, nc) 的步数更短，则更新并入队
                if d + step_count < distance[nr][nc]:
                    distance[nr][nc] = d + step_count
                    heapq.heappush(heap, (distance[nr][nc], nr, nc))

"""
        LC 505. The Maze II - Dijkstra 最短路径解法

        与 LC 490 (BFS) 的核心差异：
        --------------------------------------------------
        1. 去重与更新条件：
           - LC 490 只要 `(nr, nc) not in visited` 即可入队。
           - LC 505 必须满足 `d + step_count < distance[nr][nc]`（能松弛出更短距离）才压入堆。

        2. 提前终止条件：
           - 当从堆顶弹出 `(d, r, c)` 且 `r == dest_r and c == dest_c` 时，可立刻返回 `d`。
           - 原因：Dijkstra 算法保证从小顶堆弹出的元素一定是该节点当前可达的全局最短距离。

        复杂度分析：
        --------------------------------------------------
        - 时间复杂度: O(M * N * log(M * N))
          * 状态空间最多有 M * N 个停靠节点。
          * 堆内最大元素数为 M * N，每次堆操作耗时 O(log(M * N))。
          * 沿方向滚动的探查最多耗时 O(max(M, N))。
        - 空间复杂度: O(M * N)
          * 用于存储距离矩阵 distance 和优先队列 heap。
        """
      
        return -1
