'''
  Function minEditDistance that returns the minimum edit distance
   between two words

  Usage:
   minEditDistance(str1,str2)
'''
def minEditDistance(str1, str2):
    if str1 is None or str2 is None:
        return "strings can't be None"
    n = len(str1)
    m = len(str2)
    if n < 1:
        return m
    if m < 1:
        return n

    distance = [[0 for i in range(0,m+1)]for k in range(0,n+1)]

    # Initialization:
    # the zeroth row and col is the distance from the empty string
    distance[0][0] = 0
    for i in range(1,n+1):
        distance[i][0] = distance[i-1][0] + 1
    for j in range(1,m+1):
        distance[0][j] = distance[0][j-1] + 1

    # Recurrence relation
    for i in range(1,n+1):
        for j in range(1,m+1):
            sub = 2
            if str1[i-1] == str2[j-1]:
                sub = 0
            distance[i][j] = min(distance[i-1][j]+1, 
                                 distance[i-1][j-1]+sub, 
                                 distance[i][j-1]+1)

    # Termination
    return distance[n][m]
