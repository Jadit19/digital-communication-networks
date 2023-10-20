NUM_NODES = 4
INF = float("inf")

# Define the distance table for each node
distance_table = [[INF for _ in range(NUM_NODES)] for _ in range(NUM_NODES)]

# Define the nodes
nodes = []


# Initialize the distance table for node 0
def rtinit0():
    global distance_table
    distance_table[0] = [INF, 1, 3, 7]


# Iniitialize the distance table for node 1
def rtinit1():
    global distance_table
    distance_table[1] = [1, INF, 1, INF]


# Initialize the distance table for node 2
def rtinit2():
    global distance_table
    distance_table[2] = [3, 1, INF, 2]


# Initialize the distance table for node 3
def rtinit3():
    global distance_table
    distance_table[3] = [7, INF, 2, INF]


# Define the routing packet class
class rkpkt:
    def __init__(self, source_id, dest_id, min_cost):
        self.source_id = source_id
        self.dest_id = dest_id
        self.min_cost = min_cost


# Define the node class
class Node:
    def __init__(self, id):
        self.id = id


# Initialize the nodes
for i in range(NUM_NODES):
    nodes.append(Node(i))


# Print the distance table
def print_distance_table():
    global distance_table
    print("Distance Table:")
    print("   |  0  |  1  |  2  |  3  |")
    print("---|-----|-----|-----|-----|")
    for i in range(NUM_NODES):
        print(f" {i} | ", end="")
        for j in range(NUM_NODES):
            print("", end=" ")
            if distance_table[i][j] == INF:
                print("-", end=" ")
            else:
                print(distance_table[i][j], end=" ")
            print(" |", end=" ")
        print()


# Main function
def main():
    rtinit0()  # Initialize node 0
    rtinit1()  # Initialize node 1
    rtinit2()  # Initialize node 2
    rtinit3()  # Initialize node 3
    print_distance_table()


if __name__ == "__main__":
    main()
