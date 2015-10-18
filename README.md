# Pastero
It's a simple weechat script to upload your code to a service provider and
returns the URL automatically so that you can share your snippets, code, etc and
don't flood the channels.
Also it will do its best to recognize the file type based on the extension.

# Requirements
For the moment it requires curl to upload the data.

# Usage
Simply load the script in weechat and do this everytime you want to upload the
file.
/pastero /full/path/to/file/script.py

# TODO
* Add a feature so that when you're typing the route to your file it reconize
the '~' symbol as the $HOME path. For now you have to type the full path to
the file.

* Better error handling, like check if the site provider is down.
