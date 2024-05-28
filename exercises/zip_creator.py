import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
  dest_path = pathlib.Path(dest_dir, 'compressed.zip')
  with zipfile.ZipFile(dest_path, 'w') as archive:
    for file in filepaths:
      file = pathlib.Path(file)
      archive.write(file, arcname=file.name)


if __name__ == '__main__':
  make_archive(['exe-1.py', 'exe-2.py'], 'dest')