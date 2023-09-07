import os
import warnings

shape_base_folder = "shacl/shapes/"
shape_output_path = os.path.join(shape_base_folder, "mergedShapes.ttl")

prefixes = set()
shape_dict = {}
shape_defs = []

for root, dirs, files in os.walk(shape_base_folder, topdown=False):
    for name in files:
        file_path = os.path.join(root, name)
        if file_path == shape_output_path:
            continue
        print(file_path)
        with open(os.path.join(root, name), "r") as f:

            blocks = []
            block_start = 0
            block_end = 0
            idx = 0
            tmp_list = []
            lines = f.readlines()
            for s in lines:
                if s.startswith("@prefix"):
                    prefixes.add(s)
                elif s.startswith("gax-validation:") and s.endswith("a sh:NodeShape ;\n"):
                    block_start = idx
                elif s.endswith(".\n"):
                    block_end = idx
                    blocks.append(lines[block_start:block_end+1])
                idx += 1

            if not blocks:
                continue

            for shape_list in blocks:
                shape_header = shape_list[0]
                shape_content = "".join(shape_list[1:])
                target_shape = shape_list[-1].strip()
                if (shape_header in shape_dict.keys()) \
                        and (shape_dict[shape_header]["content"] != shape_content)\
                        and (shape_dict[shape_header]["target_shape"] == target_shape):
                    warnings.warn(
                        "WARNING: Redifining " + shape_header + " with different content, this might cause issues if it is not just order related")
                    #print(file_path, shape_dict[shape_header]["file_path"], target_shape, shape_dict[shape_header]["target_shape"])
                shape_dict[shape_header] = {
                    "content": shape_content,
                    "file_path": file_path,
                    "target_shape": target_shape
                }


with open(shape_output_path, "w") as f:
    f.writelines(prefixes)
    f.write("\n")
    for shape_header in shape_dict.keys():
        f.write(shape_header)
        f.write(shape_dict[shape_header]["content"])
        f.write("\n")
