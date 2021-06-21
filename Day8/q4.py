# Fractional Knapsack
# value when i.weight > remaining weight
# (remaining_weight*i.value)/i.weight


def fractionalknapsack(self, W, Items, n):

   # code here
    Items.sort(reverse=True, key=lambda i: (i.value/i.weight))
    remaining_weight = W
    total_value = 0
    for i in Items:
        # print(i.weight,remaining_weight,total_value)
        if(remaining_weight == 0):
            break
        if(i.weight <= remaining_weight):
            remaining_weight -= i.weight
            total_value += i.value
        # elif(i.weight>remaining_weight):
        else:
            total_value += ((remaining_weight*i.value)/i.weight)
            remaining_weight = 0
    return total_value
# Time = O(nlogn + n) == O(nlogn)
# Space = O(1)
