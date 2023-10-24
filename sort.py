import argparse
import shutil
from pathlib import Path
from shutil import copyfile
from normalize import normalize

parser = argparse.ArgumentParser(description='Sorting directory')
parser.add_argument('--source', '-s', required=True, help='Source folser')

args = vars(parser.parse_args())
source = args.get('source')


def sort_folder(path: Path):
    for element in path.iterdir():
        if element.is_dir():
            sort_folder(element)
        else:
            extension = element.suffix
            new_name = normalize(element.stem)+extension
            if extension == '.jpeg' or extension == '.png' or extension == '.jpg' or extension == '.sng':
                new_path = output_folder / 'images'
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(element, new_path / new_name)
            elif extension == extension == '.avi' or extension == '.mp4' or extension == '.mov' or extension == '.mkv':
                new_path = output_folder / 'video'
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(element, new_path / new_name)
            elif extension == '.DOC' or extension == '.docx' or extension == '.txt' or extension == '.pdf' or extension == '.xlsx' or extension == '.pptx':
                new_path = output_folder / 'documents'
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(element, new_path / new_name)
            elif extension == '.MP3' or extension == '.ogg' or extension == '.wav' or extension == '.amr':
                new_path = output_folder / 'audio'
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(element, new_path / new_name)
            elif extension == extension == '.zip' or extension == '.gz' or extension == '.tar':
                new_path = output_folder / 'archives' / new_name
                shutil.unpack_archive(element, new_path)
            else:
                new_path = output_folder / 'others'
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(element, new_path / new_name)


output_folder = Path(source)
sort_folder(Path(source))
