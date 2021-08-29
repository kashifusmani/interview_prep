def largestArea(samples):
    rows = len(samples)
    cols = len(samples[0])
    for i in range(1, rows):
        for j in range(1, cols):
            if samples[i][j]:
                samples[i][j] += min(samples[i-1][j], samples[i-1][j-1], samples[i][j-1])
    return max(v for i, r in enumerate(samples) for j, v in enumerate(r))