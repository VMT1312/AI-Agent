import os

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    target_dir = os.path.abspath(os.path.join(target_dir, file_path))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.'
    if not os.path.isfile(target_dir):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target_dir, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > 10000:
                file_content_string = file_content_string[:10000] + f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f'Error: "{e}"'
    
