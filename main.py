from random import randint as r
import time
pending_requests = []
floor_requests = []
number_of_floors = []

def number_of_floors(n):
    number of floors = [i for i in range(n)]
    return number_of_floors

max_floor = number_of_floors[-1]




def making_floors(floors):
    for x in range(2*floors):
        if x%2 == 0:
            pending_requests.append([0,0,1])
        else:
            pending_requests.append([0,0,-1])
    
#example use of the time library to keep track 
#time.time()

def request(floor, destination): 
    pending_requests.append([floor,destination,time.time()])

def initial_requests(total_floors, num_requests = 10):
    #Creates an initial list of requests for the lift to use as a base
    for x in range(num_requests):
        floor = r(0,total_floors)
        destination = r(0,total_floors)
        while destination == floor:
            destination = r(0,total_floors)
        request(floor,destination)

def lift_movement(current_floor, algorithm = "SCAN"):
    if algorithm == "SCAN":
        print("Scan")
        #Call SCAN algorithm, defined elsewhere
    elif algorithm == "LOOK":
        print("LOOK")
        #Call LOOK algorithm, defined elsewhere
    elif algorithm == "Real-Time":
        print("More")
        #... ...
    #Should return a destination

#In general, we will define the direction for up as +1, and down as -1, and for it being stationary as 0 and return these as boolean values
def direction_of_travel(current_floor, destination):
    if current_floor < destination:
        direction_of_travel = 1
    elif current_floor > destination:
        direction_of_travel = -1
    else:
        direction_of_travel = 0
    return direction_of_travel

def main_process(current_floor = 0):
    time_taken = []
    initial_requests(10)
    while pending_requests != []:
        current_floor = lift_movement(current_floor)
        for i in range(len(pending_requests)):
            pending_requests[i][2] += 1 #Incrementing time
            if pending_requests[i][1] == current_floor:
                time_taken.append(pending_requests[i][2])
                pending_requests.pop(pending_requests[i][1])
            else:
                pass


#dealing with requests people make on the floors for the elevator
# pending requests format [if request made,time,direction]
def processing_requests(floor, direction_of_travel):
    if direction_of_travel == 1 and pending_requests[2*floor][0] == 0:
        pending_requests[2*floor] = [1,time.time(),direction_of_travel]
    elif direction_of_travel == -1 and pending_requests[2*floor+1][0] == 0:
        pending_requests[2*floor+1] = [1,time.time(),direction_of_travel]

    

#deal with floor requests people make inside the elevator, once they've been picked
#removed direction of travel as it isn't required as the people in the elevator have already chosen direction
destination_floor_list = []
def dropoff_floors():
    try:
        floor_requests.append(request())
        destination_floor = floor_requests[-1][1]
        if destination_floor not in destination_floor_list:
            destination_floor_list.append(destination_floor)
        else:
            pass
        return destination_floor_list
    except ValueError or IndexError:
        return None
    



