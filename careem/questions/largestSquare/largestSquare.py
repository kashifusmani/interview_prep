def largestArea(samples):
    rows = len(samples)
    cols = len(samples[0])
    for i in range(1, rows):
        for j in range(1, cols):
            if samples[i][j]:
                samples[i][j] += min(samples[i-1][j], samples[i-1][j-1], samples[i][j-1])
    return max(v for i, r in enumerate(samples) for j, v in enumerate(r))



if __name__ == '__main__':
    #inp = [[1,1,1,1,1], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,0,0] ,[1,1,1,1,1]]
    #print(largestArea(inp))

    #inp_2 = [[1,1,1], [1,1,0], [1,0,1]]
    #print(largestArea(inp_2))

    inp_3 = [[0,1,1], [1,1,0], [1,0,1]]
    print(largestArea(inp_3))