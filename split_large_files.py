# import os
# import subprocess

# # 100 MB in bytes
# SIZE_THRESHOLD = 100 * 1024 * 1024

# def windows_to_unix_path(path):
#     # Converts Windows path to Unix path for Git Bash compatibility
#     return path.replace("\\", "/")

# def split_large_files(base_dir):
#     for root, _, files in os.walk(base_dir):
#         for file_name in files:
#             full_path = os.path.join(root, file_name)

#             if not os.path.isfile(full_path):
#                 continue

#             file_size = os.path.getsize(full_path)
#             if file_size > SIZE_THRESHOLD:
#                 file_base = os.path.splitext(file_name)[0]

#                 # Output prefix format: originalfilename_part_
#                 output_prefix = os.path.join(root, f"{file_base}_part_")

#                 # Convert to Unix-style path for Git Bash
#                 unix_input_path = windows_to_unix_path(full_path)
#                 unix_output_prefix = windows_to_unix_path(output_prefix)

#                 print("\n")
#                 print(f"Splitting file: {unix_input_path} ({file_size / (1024*1024):.2f} MB)")

#                 command = [
#                     "split",
#                     "-b", "100M",
#                     unix_input_path,
#                     unix_output_prefix
#                 ]

#                 try:
#                     subprocess.run(command, check=True)
#                     print(f"Successfully split: {file_name}")

#                     # Delete the original file after successful split
#                     os.remove(full_path)
#                     print(f"Deleted original file: {file_name}")
#                 except subprocess.CalledProcessError as e:
#                     print(f"Error splitting {file_name}: {e}")

# # ---- Entry point ----
# if __name__ == "__main__":
#     # Use full absolute path to ensure os.walk works as expected
#     directory_to_scan = os.path.abspath(".")
#     split_large_files(directory_to_scan)

import os
import subprocess

# 100 MB in bytes
SIZE_THRESHOLD = 100 * 1024 * 1024

def windows_to_unix_path(path):
    # Converts Windows path to Unix path for Git Bash compatibility
    return path.replace("\\", "/")

def split_large_files(base_dir):
    for root, _, files in os.walk(base_dir):
        # Skip the .git directory
        if ".git" in root.split(os.sep):
            continue

        for file_name in files:
            full_path = os.path.join(root, file_name)

            if not os.path.isfile(full_path):
                continue

            file_size = os.path.getsize(full_path)
            if file_size > SIZE_THRESHOLD:
                file_base = os.path.splitext(file_name)[0]

                # Output prefix format: originalfilename_part_
                output_prefix = os.path.join(root, f"{file_base}_part_")

                # Convert to Unix-style path for Git Bash
                unix_input_path = windows_to_unix_path(full_path)
                unix_output_prefix = windows_to_unix_path(output_prefix)

                print("\n")
                print(f"Splitting file: {unix_input_path} ({file_size / (1024*1024):.2f} MB)")

                command = [
                    "split",
                    "-b", "100M",
                    unix_input_path,
                    unix_output_prefix
                ]

                try:
                    subprocess.run(command, check=True)
                    print(f"Successfully split: {file_name}")

                    # Delete the original file after successful split
                    os.remove(full_path)
                    print(f"Deleted original file: {file_name}")
                except subprocess.CalledProcessError as e:
                    print(f"Error splitting {file_name}: {e}")

# ---- Entry point ----
if __name__ == "__main__":
    # Use full absolute path to ensure os.walk works as expected
    directory_to_scan = os.path.abspath(".")
    split_large_files(directory_to_scan)
