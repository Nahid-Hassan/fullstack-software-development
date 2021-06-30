# store the gas station
# here 0 value is the start point
# 200, 375, 550, 750 is the gas station 
# 950 is the end point
gas_stations = [0, 200, 375, 550, 750, 950]
# number of miles crossed when it is tank is full
distance_with_full_tank = 400


def min_refills(gas_stations, n, distance_with_full_tank):
    """
        Take the gas staions, number of gas station and distance crossed with full tank
        Return the number of minimum refills and gas station index
    """
    # store current refills
    current_refill = 0
    # store the solution
    nums_of_refills = 0
    gas_stations_idx = []

    # Since current refill is less than gas station number
    while current_refill <= n:
        # make last refill to current refill
        last_refill = current_refill
        
        while current_refill <= n and gas_stations[current_refill + 1] - gas_stations[last_refill] <= distance_with_full_tank:
            print(gas_stations[current_refill + 1] - gas_stations[last_refill])
            current_refill += 1

        if current_refill == last_refill:
            return "IMPOSABLE"
        if current_refill <= n:
            gas_stations_idx.append(current_refill)
            nums_of_refills += 1

    return nums_of_refills, gas_stations_idx


out = min_refills(gas_stations, len(gas_stations) - 2, distance_with_full_tank)
print(out[1])
