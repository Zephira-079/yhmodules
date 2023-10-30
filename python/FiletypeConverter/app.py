import subprocess
import os

awake_path = input("path >> ") or "./"
output_extension = input("output_extension >> ")
output_path = input("output_path >> ") or "./"


def convert(initial_path, produced_ext, produced_path):
    multi_ext = initial_path.split(".")[:-1]
    produce_file = f'{"".join(multi_ext) if len(multi_ext) == 1 else ".".join(multi_ext)}.{produced_ext}'
    file_basename = os.path.basename(produce_file)
    command = [
        "ffmpeg",
        "-i", initial_path,
        f'{produced_path}/{file_basename}',
        "-n"
    ]
    subprocess.run(command)

def scanpath(initial_path, produced_ext, produced_path):
    if not os.path.exists(produced_path):
        os.mkdir(produced_path)

    if os.path.isfile(initial_path):
        convert(initial_path, produced_ext, produced_path)

    elif os.path.isdir(initial_path):
        directories = os.listdir(initial_path)
        for descendants_path in directories:
            scanpath(f'{initial_path}/{descendants_path}', produced_ext, produced_path)

        
scanpath(awake_path, output_extension, output_path)

