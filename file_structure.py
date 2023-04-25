 
import os

# Define the path and folder names
pipeline_path = "/path/to/pipeline"
source_folder = "source"
transform_folder = "transform"
visualize_folder = "visualize"
output_folder = "output"

# Create the folders if they don't exist
if not os.path.exists(pipeline_path):
    os.mkdir(pipeline_path)
if not os.path.exists(os.path.join(pipeline_path, source_folder)):
    os.mkdir(os.path.join(pipeline_path, source_folder))
if not os.path.exists(os.path.join(pipeline_path, transform_folder)):
    os.mkdir(os.path.join(pipeline_path, transform_folder))
if not os.path.exists(os.path.join(pipeline_path, visualize_folder)):
    os.mkdir(os.path.join(pipeline_path, visualize_folder))
if not os.path.exists(os.path.join(pipeline_path, output_folder)):
    os.mkdir(os.path.join(pipeline_path, output_folder))

# Create empty files for each folder
source_files = ["file1.csv", "file2.csv", "file3.csv"]
transform_files = ["transform1.py", "transform2.py", "transform3.py"]
visualize_files = ["visualize1.py", "visualize2.py", "visualize3.py"]
output_files = ["processed_file1.csv", "processed_file2.csv", "processed_file3.csv"]

for file_name in source_files:
    open(os.path.join(pipeline_path, source_folder, file_name), 'a').close()

for file_name in transform_files:
    open(os.path.join(pipeline_path, transform_folder, file_name), 'a').close()

for file_name in visualize_files:
    open(os.path.join(pipeline_path, visualize_folder, file_name), 'a').close()

for file_name in output_files:
    open(os.path.join(pipeline_path, output_folder, file_name), 'a').close()
