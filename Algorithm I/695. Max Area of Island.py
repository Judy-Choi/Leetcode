def maxAreaOfIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # DFS
    def dfs(grid , row , col) :
        # 5. Check the boundaries && Whether this element is part of the island
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[row]) or grid[row][col] == 0 : 
            return 0
        
        # 6. If here is the part of the island, set 0 (already checked!)
        grid[row][col] = 0 

        # 7. Check 4 directions
        return (1 + 
                dfs(grid , row + 1 , col) + 
                dfs(grid , row -1 , col) + 
                dfs(grid , row , col + 1) + 
                dfs(grid , row , col -1)) 
        
    
    # 1. Initalize variables    
    row = len(grid) 
    col = len(grid[0])     
    count = 0
    
    # 2. Tour each elements
    for i in range(row): 
        for j in range(col):
            # 3. If this element is part of the island(grid)
            if grid[i][j] == 1:
                # 4. Dive!
                # 8. Store the larger size of an island 
                count = max(count , dfs(grid , i , j)) 
    return count

    
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(grid))