NUM_NODES = 4
INF = 10_000

# Define the nodes
nodes = []


# Define the routing packet class
class rkpkt:
    def __init__(self, source_id, dest_id, min_cost_table):
        self.source_id = source_id
        self.dest_id = dest_id
        self.min_cost_table = min_cost_table


# Define the node class
class Node:
    def __init__(self, _id):
        self.id = _id
        self.distance_table = [INF, INF, INF, INF]
        self.distance_table[self.id] = 0

    def rt_init(self, dist_table):
        for i in range(len(self.distance_table)):
            self.distance_table[i] = min(self.distance_table[i], dist_table[i])
        self.distance_table[self.id] = 0
        self.rt_send()

    def rt_send(self):
        global nodes
        for i in range(NUM_NODES):
            if i != self.id:
                pkt = rkpkt(self.id, i, self.distance_table)
                nodes[i].rt_update(pkt)
        return

    def rt_update(self, pkt: rkpkt):
        global nodes
        source = pkt.source_id
        min_cost_table = pkt.min_cost_table
        updated = False
        for i in range(NUM_NODES):
            # If you have a better distance deal than the one I have, I'll accept it
            if self.distance_table[source] > self.distance_table[i] + min_cost_table[i]:
                self.distance_table[source] = self.distance_table[i] + min_cost_table[i]
                updated = True
        if updated:
            self.rt_send()
        return


# Print the distance table
def print_distance_table():
    print("Distance Table:")
    print("   |  0    1    2    3  ")
    print("---|--------------------")
    for i in range(NUM_NODES):
        print(f" {i} | ", end="")
        for j in nodes[i].distance_table:
            print(" ", end="")
            if j == INF:
                print("-", end="")
            else:
                print(j, end="")
            print("   ", end="")
        print()


# Main function
def main():
    for i in range(NUM_NODES):
        nodes.append(Node(i))  # Initialize the nodes
    nodes[0].rt_init([0, 1, 3, 7])  # Initialize the distance table for node 0
    nodes[1].rt_init([1, 0, 1, INF])  # Initialize the distance table for node 1
    nodes[2].rt_init([3, 1, 0, 2])  # Initialize the distance table for node 2
    nodes[3].rt_init([7, INF, 2, 0])  # Initialize the distance table for node 3
    print_distance_table()


# Calling the main function
if __name__ == "__main__":
    main()
