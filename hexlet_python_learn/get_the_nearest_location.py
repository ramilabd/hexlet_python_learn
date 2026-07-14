import math


def get_distance(point1, point2):
    (x1, y1), (x2, y2) = point1, point2
    xs = x2 - x1
    ys = y2 - y1

    return math.sqrt(xs ** 2 + ys ** 2)


def get_the_nearest_location(locations: list, current_point: list):
    if locations == []:
        return None

    nearest_point = locations[0]
    min_dist = get_distance(current_point, nearest_point[1])

    for name_point, point in locations:
        dist = get_distance(current_point, point)

        if dist < min_dist or dist == min_dist:
            min_dist = dist
            nearest_point = [name_point, point]
    
    return nearest_point
        


locations = [
  ['Park', [10, 5]],
  ['Sea', [1, 3]],
  ['Museum', [8, 4]],
]

current_point = [5, 5]

print(get_the_nearest_location(locations, current_point))


