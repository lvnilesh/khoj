#!/usr/bin/env python3
import pathlib
import argparse
import os
import stat


def get_absolute(path):
    return path.expanduser().absolute()


def create_script(filepath, content):
    # Create Program Script File
    with open(get_absolute(filepath, 'w') as run_script:
        run_script.write(run_script_content)

    # Make Script Executable
    absolute_install_path = str(get_absolute(filepath))
    st = os.stat(absolute_install_path)
    os.chmod(absolute_install_path, st.st_mode | stat.S_IEXEC)


if __name__ == '__main__':
    # Setup Argument Parser
    parser = argparse.ArgumentParser(description="Setup the semantic search program")
    parser.add_argument('--script-dir', '-s', default="./", type=pathlib.Path, help="The project directory. Default: Current Directory")
    parser.add_argument('--install-dir', '-i', default="/usr/bin/", type=pathlib.Path, help="The directory to install the script. Default: ./embeddings.pt")
    parser.add_argument('--model-dir', '-m', default="./", type=pathlib.Path, help="The directory to store the model in. Default: Current Directory")
    args = parser.parse_args()

    run_server_content = f'''#!/bin/bash

# Arrange
eval "$(conda shell.bash hook)"
conda activate semantic-search
cd {get_absolute(args.script_dir)}

# Act
python3 search_types/asymmetric.py -j {get_absolute(args.model_dir)}/notes.jsonl.gz -e {get_absolute(args.model_dir)}/notes_embeddings.pt  -n 5 --interactive
'''

    search_cmd_content = f'''#!/bin/bash

# Arrange
eval "$(conda shell.bash hook)"
conda activate semantic-search
cd {get_absolute(args.script_dir)}

# Act
python3 main.py -j {get_absolute(args.model_dir)}/notes.jsonl.gz -e {get_absolute(args.model_dir)}/notes_embeddings.pt
'''

    # Create single command to start API server exposing HTTP interface
    create_script(f"{args.install_path}run_server"), run_server_content)

    # Create single command for interactive queries over commandline
    create_script(f"{args.install_path}semantic-search"), search_cmd_content)