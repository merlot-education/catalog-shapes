import os
import rdflib

shape_base_folder = os.path.join(os.path.dirname(__file__), "shacl/shapes/")
shape_output_path = os.path.join(shape_base_folder, "mergedShapes.ttl")

graph = rdflib.Graph()

for root, _, files in os.walk(shape_base_folder, topdown=False):
    for name in files:
        file_path = os.path.join(root, name)
        if file_path == shape_output_path:
            continue
        print(file_path)
        with open(file_path, "r") as f:
            try:
                graph.parse(file_path, format='ttl')
            except Exception as e:
                raise Exception("An error occurred while parsing " + str(file_path) + ": " + str(e))

graph.serialize(shape_output_path, format='ttl')