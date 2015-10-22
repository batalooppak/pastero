# Pastero
It's a simple weechat script to upload your code to a service provider and
returns the URL automatically so that you can share your snippets, code, etc and
don't flood the channels.
Also it will do its best to recognize the file type based on the extension.

## Requirements
* curl
* OSX or Linux
* weechat >= 1.3

## Usage
To upload a file:
>/pastero \<wherever_your_file_is\>  
>\*\*\* eg: /pastero ~/Documents/Scripts/my\_script.py

To run a command through pipes and upload the output: *Be careful with this!*
>/pastero --cmd command  
>\*\*\* eg: /pastero --cmd tree \<some_directory\>  
>\*\*\* eg: /pastero --cmd echo 'Hello, world'

To upload the clipboard do:  
>/pastero --clip
