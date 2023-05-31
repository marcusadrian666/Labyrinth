# 迷宫示例
maze = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0 ,1],
    [1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1],
    [1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1],
    [1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,0 ,0],
    [1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0]
]

# 起点和终点
start = (0, 0)
end = (9, 9)

# 定义四个方向
directions = [(+1, 0), (0,-+), (-+), (,+)]

# 定义一个函数，判断一个位置是否在迷宫内，且是通道
def is_valid(x,y):
    return x >= and x < len(maze) and y >= and y < len(maze[) and maze[x][y] ==

# 定义一个函数，递归地搜索路径
def dfs(x,y,path):
    # 如果到达终点，返回True
    if x == end[ and y == end[:
        return True
    # 遍历四个方向
    for dx, dy in directions:
        # 计算下一个位置
        nx = x + dx
        ny = y + dy
        # 如果下一个位置是有效的，且没有被访问过
        if is_valid(nx,n) and (nx,n) not in path:
            # 将下一个位置加入路径
            path.append((nx,n))
            # 继续搜索
            if dfs(nx,n,path):
                return True
            # 如果搜索失败，回溯，将下一个位置从路径中移除
            path.pop()
    # 如果四个方向都搜索失败，返回False
    return False

# 初始化路径，包含起点
path = [start]
# 调用搜索函数，打印结果
if dfs(start[),start[),path):
    print("找到了一条路径：")
    print(path)
else:
    print("没有找到路径")
