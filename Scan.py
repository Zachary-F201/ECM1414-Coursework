def scan_algorithm(current_floor, requests, num_floors, direction=1):
    """
    Implements the SCAN (Elevator) Algorithm.
    
    : parameter current_floor: The current position of the lift.
    : parameter requests: A list of all the requested floors for the lift to go to.
    : parameter num_floors: Total number of floors.
    : parameter direction: Initial direction, 1 for up, -1 for down.
    
    :return: Returns a list of floors in the order they will be visited.
    """
  if not requests:
        return [] #returns an empty list
    requests = sorted(requests)  #sorts requests for SCAN orders
    
    if direction == 1:  # If the lift is heading up
        up_requests = [floor for floor in requests if floor >= current_floor]   #floors requested that are at the current level or higher than the current floor
        down_requests = [floor for floor in requests if floor < current_floor]  #floors requested that are below the current level
    else:  # If the lift is going down
        up_requests = [floor for floor in requests if floor > current_floor]   #floors requested that are above the current floor
        down_requests = [floor for floor in requests if floor <= current_floor]   #floors requested that are at the current level or lower than the current floor

# Process in SCAN order
    served_order = [] #creates an empty list
    if direction == 1:
        served_order.extend(up_requests)  #adds all upward requests to the serving order
        if down_requests:
            served_order.append(num_floors - 1)  #move to top floor before reversing
            served_order.extend(reversed(down_requests))  #changes to downward requests
    else:
        served_order.extend(reversed(down_requests))  # Serve all downward requests
        if up_requests:
            served_order.append(0)  #move to ground floor before reversing
            served_order.extend(up_requests)  #changes to upward requests
    
    return served_order
