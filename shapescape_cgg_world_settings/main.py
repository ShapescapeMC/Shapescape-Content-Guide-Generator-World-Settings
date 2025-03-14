import sys
from pathlib import Path
import json
import better_json_tools as bjt
import os

# colors
color_white = '\033[0m'
color_red = '\033[31m'


class CGGWorldSettings(Exception):
    pass


def load_json_file(path: Path, file_name: str) -> dict:
    # check if file exist, if not raising an exception
    if path.exists():
        with open(path, 'r') as in_file:
            # try to load the file using bjt. If file is not valid json raising an exception
            try:
                json_file = json.load(in_file, cls=bjt.jsonc.JSONCDecoder)
            except:
                raise CGGWorldSettings(
                    f"[{color_red}ERROR{color_white}] "
                    f"{file_name} file is not valid json or is empty.")
    else:
        raise CGGWorldSettings(
            f'Could not file {file_name} at path {path}'
        )
    return json_file


def main():

    release_config_file = load_json_file(release_config_path, "release_config.json")
    # Writing Setting to file
    with open(world_settings_template_path, 'w', encoding='utf8') as file:
        file.write(f'- `Level Name`: {release_config_file["product_name"]}\n')
        file.write(f'- `Cheats`: {release_config_file["settings"]["cheats"]}\n')
        file.write(f'- `Difficulty`: {release_config_file["settings"]["difficulty"]}\n')
        file.write(f'- `Multiplayer`: {release_config_file["settings"]["multiplayer"]}\n')
        file.write(f'- `Gamerules`:\n')
        file.write(f'    - `sendCommandFeedback`: {release_config_file["settings"]["sendCommandFeedback"]}\n')
        file.write(f'    - `commandBlockOutput`: {release_config_file["settings"]["commandBlockOutput"]}\n')
        file.write(f'    - `doDayLightCycle`: {release_config_file["settings"]["doDayLightCycle"]}\n')
        file.write(f'    - `doMobSpawning`: {release_config_file["settings"]["doMobSpawning"]}\n')


if __name__ == "__main__":
    config = {}
    if len(sys.argv) > 1:
        config = json.loads(sys.argv[1])

    release_config_path = config.get(
        "release_config_path",
        "../pack/release_config.json")
    world_settings_template_path = config.get(
        "world_settings_template_path",
        "data/shapescape_content_guide_generator/templates/world_settings.md")
    path_relative_to_config_json = config.get(
        "path_relative_to_config_json",
        True
    )
    # #Update the paths if they are relative to the config.json file.
    if path_relative_to_config_json:
        try:
            root_dir = os.environ['ROOT_DIR']
        except KeyError:
            raise CGGWorldSettings(
                "Failed to load 'ROOT_DIR' from environment variables.")
        root_dir = Path(root_dir)
        release_config_path = root_dir / release_config_path

    main()

