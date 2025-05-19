# import os
# import re
# from collections import defaultdict

# def windows_to_unix_path(path):
#     # Converts Windows path to Unix path for Git Bash compatibility
#     return path.replace("\\", "/")

# def find_split_files(base_dir):
#     split_files = defaultdict(list)

#     # Look for files ending in pattern like _part_aa, _part_ab, etc.
#     pattern = re.compile(r"(.+)_part_[a-z]{2}$")

#     for root, _, files in os.walk(base_dir):
#         for file_name in files:
#             match = pattern.match(file_name)
#             if match:
#                 base_name = match.group(1)
#                 full_path = os.path.join(root, file_name)
#                 split_files[(root, base_name)].append(full_path)

#     return split_files

# def reconstruct_files(base_dir):
#     split_groups = find_split_files(base_dir)

#     for (root, base_name), parts in split_groups.items():
#         # Sort parts to ensure correct order (part_aa, part_ab, ...)
#         parts.sort()
#         output_file = os.path.join(root, base_name + ".raw")

#         print("\n")
#         print(f"Reconstructing {base_name} from {len(parts)} parts...")

#         try:
#             with open(output_file, 'wb') as out_f:
#                 for part in parts:
#                     with open(part, 'rb') as in_f:
#                         out_f.write(in_f.read())

#             print(f"Successfully reconstructed: {output_file}")

#             # Delete the part files after successful reconstruction
#             for part in parts:
#                 os.remove(part)
#                 print(f"Deleted part file: {part}")

#         except Exception as e:
#             print(f"Error reconstructing {base_name}: {e}")

# # ---- Entry point ----
# if __name__ == "__main__":
#     directory_to_scan = os.path.abspath(".")
#     reconstruct_files(directory_to_scan)





import os
import re
from collections import defaultdict

def windows_to_unix_path(path):
    # Converts Windows path to Unix path for Git Bash compatibility
    return path.replace("\\", "/")

def find_split_files(base_dir):
    split_files = defaultdict(list)

    # Look for files ending in pattern like _part_aa, _part_ab, etc.
    pattern = re.compile(r"(.+)_part_[a-z]{2}$")

    for root, _, files in os.walk(base_dir):
        # Skip the .git directory
        if ".git" in root.split(os.sep):
            continue

        for file_name in files:
            match = pattern.match(file_name)
            if match:
                base_name = match.group(1)
                full_path = os.path.join(root, file_name)
                split_files[(root, base_name)].append(full_path)

    return split_files

def reconstruct_files(base_dir):
    split_groups = find_split_files(base_dir)

    for (root, base_name), parts in split_groups.items():
        # Sort parts to ensure correct order (part_aa, part_ab, ...)
        parts.sort()
        output_file = os.path.join(root, base_name + ".raw")

        print("\n")
        print(f"Reconstructing {base_name} from {len(parts)} parts...")

        try:
            with open(output_file, 'wb') as out_f:
                for part in parts:
                    with open(part, 'rb') as in_f:
                        out_f.write(in_f.read())

            print(f"Successfully reconstructed: {output_file}")

            # Delete the part files after successful reconstruction
            for part in parts:
                os.remove(part)
                print(f"Deleted part file: {part}")

        except Exception as e:
            print(f"Error reconstructing {base_name}: {e}")

# ---- Entry point ----
if __name__ == "__main__":
    directory_to_scan = os.path.abspath(".")
    reconstruct_files(directory_to_scan)
