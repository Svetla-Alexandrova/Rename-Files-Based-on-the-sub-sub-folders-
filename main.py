

from pathlib import Path

root_dir = Path('files')

for path in root_dir.glob("**/*"):
  if path.is_file():
    parent_folder = path.parts
    # print(parent_folder)
    subfolders = path.parts[1:-1]
    # print(subfolders)

    new_filename = "-".join(subfolders) + '-' + path.name
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)