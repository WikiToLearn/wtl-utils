This bot takes care of uploading pages to WTL. It can be used for multiple purposes, a brief
description on oh to use it can be retrieved
[here](https://meta.wikitolearn.org/Texla/Import_page_from_converted_files).

Be careful: the bot looks for files in the ./input folder, which is
not tracked by git since it is pretty convinient to use a symlink
and link the directory that you wish to import to ./input.
This causes ./input to be a file that depends on the user
file hierarcacy, and is not a good idea to distribute it.

Hence, if you are willing to use this bot you have to:

    ln -s /absolute/path/of/the/dir/to/import/$directory_name .
    mv $directory_name input
    ./upload.sh

This bot uses a docker, so you must have a working docker engine
installed on your system.

