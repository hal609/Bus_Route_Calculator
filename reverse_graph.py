import pickle
import rustworkx as rx

# Load graph
with open("transit_graph_.pkl", "rb") as f:
    G = pickle.load(f)

print(type(G))

# Reverse graph
G.reverse()

# Export reversed graph
with open("transit_graph_reversed.pkl", "wb") as f:
    pickle.dump(G, f)