from main.py import request and lift_movement and direction_of_travel


#the function deals with... it's in the name
def look_functionality()
    #checks if the lift if heading in the direction of the target floor
    if direction_of_travel == 1 and destination > current_floor or direction_of_travel == -1 and destination < current_floor:
        pass
    #this handles the case where it isn't heading in the right direction
    elif direction_of_travel == 1 and destination < current_floor or direction_of_travel == -1 and destination > current_floor:
        direction_of_travel = -(direction_of_travel)
    return direction_of_travel