def maxMoves( grid) :

        l = []   
         
        def recor(i,grid, j = 0,count = 0):
            
            if i== len(grid) or j == len(grid[0]) or i==0:
                l.append(count)
                
                
                return count
            elif (i>0 and j<len(grid[0])-1 and  grid[i][j]<grid[i-1][j+1]) and (j<len(grid[0])-1 and  grid[i][j]<grid[i][j+1]) and (i < len(grid)-1 and j<len(grid[0])-1 and grid[i][j]<grid[i+1][j+1]):
                return max(recor(i-1,grid,j+1,count+1),recor(i,grid,j+1,count+1),recor(i+1,grid,j+1,count+1))
            
            elif (i>0 and j<len(grid[0])-1 and  grid[i][j]<grid[i-1][j+1]) and (j<len(grid[0])-1 and  grid[i][j]<grid[i][j+1]):
                return max(recor(i-1,grid,j+1,count+1),recor(i,grid,j+1,count+1))
            
            elif i>0 and j<len(grid[0])-1 and  grid[i][j]<grid[i-1][j+1] and i < len(grid)-1 and j<len(grid[0])-1 and grid[i][j]<grid[i+1][j+1]:
                return max(recor(i-1,grid,j+1,count+1),recor(i+1,grid,j+1,count+1))
            
            elif j<len(grid[0])-1 and  grid[i][j]<grid[i][j+1] and i < len(grid)-1 and j<len(grid[0])-1 and grid[i][j]<grid[i+1][j+1]:
                return max(recor(i,grid,j+1,count+1),recor(i+1,grid,j+1,count+1))
            
            elif i>0 and j<len(grid[0])-1 and  grid[i][j]<grid[i-1][j+1]:
                i,j = i-1,j+1
                count +=1
                return recor(i,grid,j,count)
                
            elif j<len(grid[0])-1 and  grid[i][j]<grid[i][j+1]:
                i,j = i, j+1
                count +=1
                return recor(i,grid,j,count)
            elif i < len(grid)-1 and j<len(grid[0])-1 and grid[i][j]<grid[i+1][j+1]:
                i,j = i+1, j+1
                count +=1
                return recor(i,grid,j,count)
            else:
                l.append(count)
                return count
            
        for i in range(len(grid)):
            recor(i,grid)
        
            
        return max(l)
            
print(maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))         
        
