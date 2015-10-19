# Pastero
It's a simple weechat script to upload your code to a service provider and
returns the URL automatically so that you can share your snippets, code, etc and
don't flood the channels.
Also it will do its best to recognize the file type based on the extension.

## Requirements
For the moment it requires curl to upload the data.

## Usage
/pastero <wherever_your_file_is>
*** eg: /pastero ~/Documents/Scripts/my_script.py
/pastero --cmd command
*** eg: /pastero --cmd echo 'Hello, world' # Please be careful with this option.
