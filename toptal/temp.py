def solution(arr):
    season_length = int(len(arr)/4)
    seasons = {0:'WINTER', 1: 'SPRING', 2: 'SUMMER', 3: 'AUTUMN'}
    max_i = 0
    max_amplitude = 0
    for i in range(0, 4):
        season_start = season_length * i
        season_end = season_length * (i+1)
        season_min = min(arr[season_start: season_end])
        season_max = max(arr[season_start: season_end])
        season_amplitude = season_max - season_min

        if season_amplitude > max_amplitude:
            max_amplitude = season_amplitude
            max_i = i
    return seasons[max_i]


if __name__ == '__main__':
    print(solution([-3, -14, -5, 7, 8, 42, 8, 3]))
    print(solution([2, -3, 3, 1, 10, 8, 2, 5, 13, -5, 3, -18]))
