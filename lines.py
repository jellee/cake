
# Write a function to determine if a set of Cartesian points are collinear (lie on same line).

# input: [[1,2], [2,3], ..., [x,y], [3,4]]
# output: true|false

# y = mx + b
# m = slope
# b = y-intercept
# ------------------------------------
# create a line with the first two points
# check rest of the points to see if it fits within line

def isLine (points) :
    points = list(set(points))
    if len(points) < 3 : return true
    
    if points[1][0] == points[0][0] and points[1][1] != points[0][1] : 
        x = points[0][0]
        for point in points :
            if point[0] != x : return false
        return true
    
    m = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
    
    b = points[0][1] - (m * points[0][0])
    for point in points :
        if point[1] != m*point[0] + b :
            return false
    return true