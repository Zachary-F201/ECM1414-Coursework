pending_requests = []

def request(floor, destination):
    pending_requests.push([floor,destination])

def lift_movement(algorithm = "SCAN", current_floor):
    if algorithm == "SCAN"
        #Call SCAN algorithm, defined elsewhere
    elif algorithm == "LOOK"
        #Call LOOK algorithm, defined elsewhere
    elif algorithm == "Real-Time":
        #... ...
    #Should return a destination
    for i in range(len(pending_requests)):
        if pending_requests[i][1] == current_floor:
            pending_requests.pop(pending_requests[i][1])
        else:
            pass

#In general, we will define the direction for up as +1, and down as -1, and for it being stationary as 0 and return these as boolean values
def direction_of_travel():
    if current_floor < destination:
        direction_of_travel = 1
    elif current_floor > destination:
        direction_of_travel = -1
    else:
        direction_of_travel = 0
    return direction_of_travel