weights = 1
weights_values = [(14, 2), (20, 4), (18, 3)]


def knapsack_slow(weights_values, weights):
    values_by_weights = [(x / y, y) for x, y in weights_values]
    values_by_weights.sort(reverse=True)
    # print(values_by_weights)

    print(values_by_weights)
    bags = []

    for i in range(len(values_by_weights)):
        if sum(bags) == weights:
            break
        if values_by_weights[i][1] <= weights - sum(bags):
            bags.append(values_by_weights[i][1])
            # weights -= values_by_weights[i][1]
        else:
            # temp = values_by_weights[i][1]
            bags.append(weights)
            print(weights + '----------')
    return bags



def knapsack_fast(weights_values, weights):
    bags = []
    volume = 0
    temp_weights = weights

    values_by_weights = [(x/y, y) for x, y in weights_values]
    values_by_weights.sort()

    for i in range(len(weights_values)):
        if weights == 0:
            return (bags, volume)
        
        if values_by_weights[i][1]:
            pass    

