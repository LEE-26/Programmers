def solution(wallpaper):
    # 최소, 최대 문제
    coordinates_x = []
    coordinates_y = [] 

    for idx, w in enumerate(wallpaper) :
        for i, c in enumerate(w) :
            if c == '#' : 
                coordinates_x.append(idx)
                coordinates_y.append(i)
    
    return [min(coordinates_x), min(coordinates_y), max(coordinates_x)+1, max(coordinates_y)+1]