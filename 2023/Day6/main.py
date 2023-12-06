# FINAL SOLUTION
import math

def get_roots(a, b, c):
    first = ((-1 * b) - ((b**2 - 4*a*c)**(0.5))) / (2*a)
    second = ((-1 * b) + ((b**2 - 4*a*c)**(0.5))) / (2*a)
    return first, second

# times = [56, 97, 77, 93]
# distances = [499, 2210, 1097, 1440]
times = [56977793]
distances = [499221010971440]

result = 1
for i in range(len(times)):
    total_time = times[i]
    record_d = distances[i]
    start, end = get_roots(1, -(total_time), record_d) #S = D/(T-S) ==> S^2 - S*T + D = 0
    # speed needed >start and <end
    start, end = math.ceil(start), math.floor(end)
    wins_count = end - start + 1 #(start and end inclusive)
    result *= wins_count
print(result)



# FIRST ATTEMPT

# import math

# def get_roots(a, b, c):
#     first = ((-1 * b) - ((b**2 - 4*a*c)**(0.5))) / (2*a)
#     second = ((-1 * b) + ((b**2 - 4*a*c)**(0.5))) / (2*a)
#     return first, second

# # times = [56, 97, 77, 93]
# # distances = [499, 2210, 1097, 1440]
# times = [56977793]
# distances = [499221010971440]

# result = 1
# for i in range(len(times)):
#     total_time = times[i]
#     record_d = distances[i]
#     wins = 0
#     start, end = get_roots(1, -(total_time), record_d) #S = D/(T-S) ==> S^2 - S*T + D = 0
#     # speed needed >start and <end
#     start, end = math.ceil(start), math.floor(end)
#     print(start, end)
    
#     # Part 2: buttom loop is just verification, (end - start) is the answer. 
#     # Though, buttom loop is answer of Part 1.
#     for i in range(int(start), int(end)+1):
#         speed = i
#         left_time = total_time - speed
#         d = speed * left_time
#         if d > record_d:
#             wins+=1
#         if d < record_d:  # fails for end+1
#             print("breaking", speed, d, speed, left_time)
#             break
#         if i % 1000 == 0:
#             print(i)
#     # print(wins)
#     result *= wins
# print(result)
