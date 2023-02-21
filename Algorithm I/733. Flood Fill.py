def floodFill(image, sr, sc, color):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type color: int
    :rtype: List[List[int]]
    """    
    # DFS
    # 1. old_color = color of starting point
    old_color = image[sr][sc]
    
    # 2. Set the image boundary
    max_row = len(image)
    max_col = len(image[0])

    def dfs(row, col):
        # 4. Check image boundary
        if not (0 <= row < max_row and 0 <= col < max_col):
            return
                
        # 5. If color is already changed, return
        if image[row][col] != old_color:
            return

        # 6. Change the color
        image[row][col] = color
        
        # 7. Search neighbor points
        dfs(row - 1, col)            
        dfs(row + 1, col)            
        dfs(row, col - 1)
        dfs(row, col + 1)

    # 3. In this point, change color && search neighbor points
    if old_color != color:
        # Start from the starting point
        dfs(sr, sc)
        
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

print(floodFill(image, sr, sc, color))