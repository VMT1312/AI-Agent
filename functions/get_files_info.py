import os

def get_files_info(working_directory, directory=None):
    cwd_path = os.path.abspath(working_directory)
    directory_path = cwd_path
    if directory:
        directory_path = os.path.abspath(os.path.join(cwd_path, directory))
    if not directory_path.startswith(cwd_path):
        raise FileNotFoundError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory.')

    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f'Error: "{directory}" is not a directory')

    try:
        files_info = []

        for file in os.listdir(directory_path):
            path = os.path.join(directory_path, file)
            is_dir =  os.path.isfile(path)

            file_size = os.path.getsize(path)
            files_info.append(f'- {file}: file_size={file_size} bytes, is_dir={is_dir}')

        return "\n".join(files_info)
    except Exception as e:
        return f'Error: "{e}'
