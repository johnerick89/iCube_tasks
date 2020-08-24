
outer_radius = 10
middle_radius = 5
inner_radius =1 
center_x = 0
center_y = 0

scores = {"outer":1,"middle":5,"inner":10}

def check_if_point_in_circle(x,y, radius):
    '''
    Function to check if point is within circle with a given radius
    '''
    return (x-center_x)**2 + (y - center_y)**2 <= radius**2

def score(x,y):
    '''
    Function to check if point in within the circles
    '''
    is_in_outer_radius = check_if_point_in_circle(x,y, outer_radius)
    is_in_middle_radius = check_if_point_in_circle(x,y, middle_radius)
    is_in_inner_radius = check_if_point_in_circle(x,y, inner_radius)

    if is_in_inner_radius:
        return scores["inner"]
    elif is_in_middle_radius:
         return scores["middle"]
    elif is_in_outer_radius:
         return scores["outer"]
    return 0

''''
Function driver code
'''
x=0
y=0
dart_score = score(x, y)
print(dart_score)