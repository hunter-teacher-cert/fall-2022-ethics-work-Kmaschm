#Ethics - Fall 2022
#Names: Adam Driggers, Kate Maschmeyer, Marisa Shuman

# Economy Plus - people can pick their seat

#Blocks of tickets can be purchased and they are attempted to be together 
import random


def create_plane(rows,cols):
    plane = []
    for r in range(rows):
        s = ["win"]+["avail"]*(cols-2)+["win"]
        plane.append(s)
    return plane

def get_number_economy_sold(economy_sold):
    ## economy_sold is a dictionary -- ex:   {'Robinson':3, 'Lee':2 } 
    sold = 0
    for v in economy_sold.values():
        sold = sold + v
    return sold #returning the number of seats sold



def get_avail_seats(plane,economy_sold):
    avail = 0;
    for r in plane:
        for c in r:
            if c == "avail" or c == "win":
                avail = avail + 1
    avail = avail - get_number_economy_sold(economy_sold)
    return avail


def get_total_seats(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane
    """
    return len(plane)*len(plane[0])


def get_plane_string(plane):
   
    s = ""
    for r in plane:
        r = ["%14s"%x for x in r] # This is a list comprehension - an advanced Python feature
        s = s + " ".join(r)
        s = s + "\n"
    return s


def purchase_economy_plus(plane,economy_sold,name):
    """
    Params: plane - a list of lists representing a plane
            economy_sold - a dictionary representing the economy sold but not assigned
            name - the name of the person purchasing the seat
    """
    rows = len(plane)
    cols = len(plane[0])

    # total unassigned seats
    seats = get_avail_seats(plane,economy_sold)

    # exit if we have no more seats
    if seats < 1:
        return plane


    # 70% chance that the customer tries to purchase a window seat
    # it this by making a list of all the rows, randomizing it
    # and then trying each row to try to grab a seat

    
    if random.randrange(100) > 30:
        # make a list of all the rows using a list comprehension
        order = [x for x in range(rows)]

        # randomzie it
        random.shuffle(order)

        # go through the randomized list to see if there's an available seat
        # and if there is, assign it and return the new plane
        for row in order:
            if plane[row][0] == "win":
                plane[row][0] = name
                return plane
            elif plane[row][len(plane[0])-1] == "win":
                plane[row][len(plane[0])-1] = name
                return  plane

    # if no window was available, just keep trying a random seat until we find an
    # available one, then assign it and return the new plane
    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
    return plane

# help functions, return the num of available seats

# here is what we were working on...
# A helper function
# def determine_avail_seats_row(plane, row):
#     counter = 0
#     for num in len(row): 
#         if plane[row][num] == "win" or plane[row][num] == "avail":           
#             counter += 1

#     return counter

def seat_economy(plane, economy_sorted, group):

    rows = len(plane)
    cols = len(plane[0])

    # if economy_sorted[group] > 6: #this will sort for all groups larger than 6 so they can be split into 3/3/2/2, 3/3/3, 3/3/2, or 2/2/3
    #     #assigning next consecutive seats
    #     found_seat = False

    #     while not(found_seat):
    #         for row in rows:
    #             for col in cols: 
    #                 if plane[row][col] == "win" or plane[row][col] == "avail":
                        
    #                     plane[r_row][r_col] = group
    #                     found_seat = True

    ## while we have haven't seated the group,
        # find the number of availabel seats in the row
        # if the vailable seats is les than or equal to the group size


    

    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = group
            found_seat = True
    return plane


def purchase_economy_block(plane,economy_sold,number,name):
    """
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary

    """
    seats_avail = get_total_seats(plane)
    seats_avail = seats_avail - get_number_economy_sold(economy_sold)

    if seats_avail >= number:
        economy_sold[name]=number
    return economy_sold




def fill_plane(plane):

    economy_sold={}
    total_seats = get_total_seats(plane)
    total_avail = get_avail_seats(plane, economy_sold)
    
    # these are for naming the pasengers and families by
    # appending a number to either "ep" for economy plus or "u" for unassigned economy seat
    ep_number=1
    f_id=1

    # MODIFY THIS
    # you will probably want to change parts of this
    # for example, when to stop purchases, the probabilities, maybe the size for the random
    # regular economy size

    max_family_size = 10
    while total_avail > 1:
      # set a random family size;
        rFamSize = random.randint(1, max_family_size + 1)
        economy_sold = purchase_economy_block(plane,economy_sold, rFamSize ,"fam-%d"%f_id)
        f_id += 1
        total_avail = get_avail_seats(plane, economy_sold)
    # print(economy_sold)

#screw economy plus
##We can ignore economy plus -- and just try to focus on grouping everyone with at least one person they are traveling with (as long as their group is >1)

# sell all the tickets, keeping track of the group size, and accessibility request.
# once the plane is fully booked, start placing people in seats.
# First, place passengers needing accessible seating, and their party
# go from the biggest party size to the smallest party size. 
# if a party can't be seated all together, split them into two groups, readd to the list, try again.
    

## NEED TO EDIT: 
#  (comment out) purchase_economy_plus(plane,economy_sold,name)
#  seat_economy(plane,economy_sold,name)
#  fill_plane(plane) 

## LEAVE: purchase_economy_block(plane,economy_sold,number,name)
        

          
        
    # once the plane reaches a certian seating capacity, assign
    # seats to the economy plus passengers
    # you will have to complete the seat_economy function
    # Alternatively you can rewrite this section
    
    # sort test
    economy_sorted = sorted(economy_sold.items(), key=lambda kv:(kv[1], kv[0]))
    
    ##Their code 
    #This is currently only seating an individual person
    #loop through the sorted list, from 

    #Want to look at the largest group (the last in the economy_sorted) and seat them. 
    #Continue through the list from right to left
    #If a family can't be seated together, then use conditionals to break them up into 2-3 groups

    # for group in reversed(range(len(economy_sorted))) :
    #     plane = seat_economy(plane, economoy_sorted, group)

    
    #print(economy_sorted)
    
    for group in economy_sold.keys():
        for i in range(economy_sold[group]):
            plane = seat_economy(plane,economy_sold,group)


    return plane
    
    
    
def main():
    plane = create_plane(10,5) #creates a plane that is 10 rows of 5 seats
    plane = fill_plane(plane) #simulation of picking seats
    print(get_plane_string(plane))
if __name__=="__main__":
    main()







##Next Steps: 

# Uncomment out our determine_avail_seats_row function -- that will calculate how many seats are available in each row
# We will use our sorted key dictionary (economy_sorted) to look at the largest groups first
# We will seat groups of 10 (3/3/2/2), 9 (3/3/3), 8 (3/3/2), 7 (3/2/2), 6 (3/3/3), 5 (3/2), 4 (2/2), 3, 2, 1
    # This will be done by splitting up the group based on the total number and then finding associated availabile seats
# Groups will be sorted from the front of the plane to the back. 