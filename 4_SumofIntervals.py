def sum_of_intervals(intervals):
    result = set()
    
    for target_interval in intervals:
        for target in range(target_interval[0],target_interval[1]):
            result.add(target)
            
    return len(result)

print(sum_of_intervals( [
   [1,4],
   [7, 10],
   [3, 5]
] )) # answer should be 7

# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/python