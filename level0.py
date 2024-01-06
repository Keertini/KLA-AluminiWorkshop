import json

with open("Y:\\Student Handout\\Input data\\level0.json", "r") as file:
        file_content = file.read()
        data = json.loads(file_content)

neighbourhoods = data["neighbourhoods"]

n_indices = ["n0", "n1", "n2","n3","n4","n5","n6","n7","n8","n9","n10","n11","n12","n13","n14","n15","n16","n17","n18","n19"]
distances_2d_array = []

for index in n_indices:
    distances_2d_array.append(neighbourhoods[index]["distances"])

print('')

def nearest_neighbor_algorithm(distances_2d_array):
    n_neighbors = len(distances_2d_array)
    start_node = 0
    unvisited_nodes = set(range(1, n_neighbors))
    path = [start_node]

    while unvisited_nodes:
        current_node = path[-1]
        nearest_neighbor = min(unvisited_nodes, key=lambda node: distances_2d_array[current_node][node])
        path.append(nearest_neighbor)
        unvisited_nodes.remove(nearest_neighbor)

    path.append(start_node)  
    return path


result_path = nearest_neighbor_algorithm(distances_2d_array)
print(result_path)
print('')

vehicle_name = "v0"
start_point = data["vehicles"][vehicle_name]["start_point"]
path = [f"r{result_path[0]}"]

for node_index in result_path[1:]:
    node_name = f"n{node_index}"
    path.append(node_name)

path.append(start_point)

output_json = {vehicle_name: {"path": path}}

print(json.dumps(output_json, indent=2))
print('')

output_file_path = "level0_output.json"
with open(output_file_path, "w") as output_file:
    json.dump(output_json, output_file, indent=2)

print(f"Output written to {output_file_path}")