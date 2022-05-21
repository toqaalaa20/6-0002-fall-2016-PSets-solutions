###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    dict1={}
    file= open(filename, 'r')
    for line in file:
        data= line.strip('\n').split(",")
        dict1[data[0]]= int(data[1])
    return dict1

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    sorted_cows= sorted(cows.items(), key= lambda x: x[1], reverse=True)  
    cow_names=[]      
    while len(sorted_cows)>0:  
        taken=[]  
        to_remove=[]
        total_weight= 0        
        for cow in sorted_cows:                                  
            avail= limit-total_weight                                  
            if cow[1]<=avail:
                 total_weight+= cow[1]
                 taken.append(cow[0])
                 to_remove.append(cow)                
        for cow in to_remove:
            sorted_cows.remove(cow)
        cow_names.append(taken)
    return cow_names

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows2= cows.copy()
    cow_names=[]
    for partition in get_partitions(cows2):
        weight_over_limit= False
        for trip in partition:
            sum1=0
            for cow in trip:
                sum1+= cows[cow]
            if sum1>limit:
                weight_over_limit= True 
                break
        if weight_over_limit is True: 
            continue
        elif len(cow_names)==0 or len(partition) < len(cow_names):
            cow_names= partition
    return cow_names
        
        
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows= load_cows("ps1_cow_data.txt").copy()
    start1 = time.time()
    x= greedy_cow_transport(cows,limit=10)
    end1 = time.time()
    time1= end1-start1
    start2 = time.time()
    y= brute_force_cow_transport(cows,limit=10)
   
    end2 = time.time()
    time2= end2-start2
    print(f"Greedy cows: \n{x}")
    print(f"Brute force cows: \n{y}")
    print(f"The number of trips, for greedy algorithm is: {len(x)}, for brute force algorithm is: {len(y)}")
    print(f"Time for greedy algorithm is {time1} \nTime for brute force is {time2}")



compare_cow_transport_algorithms()
