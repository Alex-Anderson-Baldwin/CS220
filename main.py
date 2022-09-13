import sys


def mergeSort(input_array):
    if len(input_array) < 2:
        return input_array
    mid = len(input_array) // 2
    left = input_array[:mid]
    right = input_array[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)


def merge(input1, input2):
    output = []
    while len(input1) > 0 or len(input2) > 0:
        if input1 == []:
            output = output + input2
            return output
        if input2 == []:
            output = output + input1
            return output
        if input1[0] < input2[0]:
            output.append(input1[0])
            input1 = input1[1:]
        elif input2[0] < input1[0]:
            output.append(input2[0])
            input2 = input2[1:]
    return output

def routerSort(network_traffic, router_count, routers):
    total = 0
    for x in range(len(network_traffic)):
        for y in range(len(network_traffic[x])):
            total += abs(float(network_traffic[x][y]))
            print(network_traffic[x][y])
            print(float((network_traffic[x][y])))
            print(abs(float((network_traffic[x][y]))))
            print("Total: " + str(total))
        router_traffic.append((x, total))
        total = 0
    print(router_traffic)
    sorted_keys = []
    for pair in router_traffic:
        sorted_keys.append(pair[1])

    sorted_keys = mergeSort(sorted_keys)
    sorted_keys = sorted_keys[::-1]
    sorted_router_traffic = []
    lcv = 0

    for key in sorted_keys:
        for pair in router_traffic:
            if key == pair[1]:
                sorted_router_traffic.append(pair)
                router_traffic.remove(pair)
                break

    output_list = {}
    output_string = ""
    lcv = 0
    print(sorted_keys)
    for router in sorted_router_traffic:
        output_list.update({router[0]:routers[lcv]})
        lcv += 1

    for x in range(int(router_count)):
        output_string = output_string + str(x+1) + "-" + str(output_list[x]) + " "
    print(output_list)
    return output_string

lists = []
for a in sys.stdin.readlines():
    lists.append(a.rstrip())
    print("hello")
print(lists)
router_count = lists[0]
network_traffic = []

for x in range(1, int(router_count)+1):
    network_traffic.append(lists[x].split(" "))

lists = lists[len(network_traffic)+1:]

routers = lists[0].split(" ")
routers = mergeSort(routers)
routers = routers[::-1]
router_traffic = []

output = routerSort(network_traffic, router_count, routers)
print(output)
