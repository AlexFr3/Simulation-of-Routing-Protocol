class Node:
    def __init__(self, name):
        self.name = name
        self.routing_table = {}  # Destinazione: (Costo, Next Hop)
        self.neighbors = {}      # Vicini: Costo

    def update_table(self, neighbor_name, neighbor_table):
        updated = False
        for dest, (cost_to_dest, next_hop) in neighbor_table.items():
            new_cost = self.neighbors[neighbor_name] + cost_to_dest
            if dest not in self.routing_table or new_cost < self.routing_table[dest][0]:
                self.routing_table[dest] = (new_cost, neighbor_name)
                updated = True
        return updated

    def __str__(self):
        return f"Node {self.name} Routing Table: {self.routing_table}"


class Network:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        self.nodes[name] = Node(name)

    def add_link(self, node1, node2, cost):
        self.nodes[node1].neighbors[node2] = cost
        self.nodes[node2].neighbors[node1] = cost

    def simulate_routing(self):
        converged = False
        iteration = 0
        while not converged:
            print(f"Iteration {iteration}")
            converged = True
            for node_name, node in self.nodes.items():
                for neighbor_name in node.neighbors:
                    if node.update_table(neighbor_name, self.nodes[neighbor_name].routing_table):
                        converged = False
            for node in self.nodes.values():
                print(node)
            iteration += 1
            print("-" * 50)


# Definizione della rete
network = Network()
network.add_node("A")
network.add_node("B")
network.add_node("C")
network.add_node("D")

network.add_link("A", "B", 1)
network.add_link("A", "C", 5)
network.add_link("B", "C", 2)
network.add_link("B", "D", 4)
network.add_link("C", "D", 1)

# Inizializza le tabelle di routing
for node in network.nodes.values():
    for neighbor, cost in node.neighbors.items():
        node.routing_table[neighbor] = (cost, neighbor)
    node.routing_table[node.name] = (0, node.name)

# Simula il protocollo
network.simulate_routing()
