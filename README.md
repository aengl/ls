# ls
A customised "ls" command for todo-txt.

## Installation

`cd` into your plugins folder (see [Installing Addons](https://github.com/ginatrapani/todo.txt-cli/wiki/Creating-and-Installing-Add-ons)), e.g.:

    cd ~/.todo.actions.d

Then clone this repository into the folder `ls`:

    git clone https://github.com/aengl/ls

## Prerequisites

`ls` requires python3 to be installed. To enable color support, the `colored` library is required:

    pip3 install colored

## Usage

    todo.sh ls

To view a shared `todo.txt`:

    todo.sh ls <path_to_todo_dir>

The path can be relative to `TODO_DIR`, or absolute.
