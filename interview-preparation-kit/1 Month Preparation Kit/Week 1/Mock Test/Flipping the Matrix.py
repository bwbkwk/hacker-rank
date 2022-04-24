#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
def flippingMatrix(matrix):
  d = len(matrix)
  hd = d//2
  ul = [matrix[i][:hd] for i in range(hd)]
  ur = [matrix[i][hd:] for i in range(hd)]
  br = [matrix[i][hd:] for i in range(hd,d)]
  bl = [matrix[i][:hd] for i in range(hd,d)]

  total = 0
  for i in range(hd):
    for j in range(hd):
      total +=max(ul[i][j], ur[i][hd-j-1], bl[hd-i-1][j],br[hd-i-1][hdj-1])
  return total
