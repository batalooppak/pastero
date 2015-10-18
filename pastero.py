# -*- coding: utf-8 -*-

# Copyright © 2015 Lucas Jiménez
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

# History:
# 2015-10-05, Lucas Jiménez
#     Version 0.3: Change paste provider
# 2015-10-05, Lucas Jiménez
#     Version 0.2: Code complety rewritten :)
# 2015-09-25, Lucas Jiménez
#     Version 0.1: Initial release

# TODO:
# - Add a feature to recognize variabel path "~"

SCRIPT_NAME    = "pastero"
SCRIPT_AUTHOR  = "Lucas Jiménez"
SCRIPT_VERSION = "0.3"
SCRIPT_LICENSE = "MIT"
SCRIPT_DESC    = "Upload snippets, text files, etc and return the URL"

PREFIX = "[pastero]"

SCRIPT_HELP = """Help:
This script will do its best to automatically identify
its filetype by the file extension. If the file doesn't have a file extension,
then plain text is used and no syntax highlighting is activated.\n
For the moment pastero doesn't accepts "~" as a path so you have
to use /home/<user>/ instead of "~".\n
Usage:
/pastero <full_path_to_file>/<file_name>\n
Example:
Let's suppose you have a file called my_script.py somewhere in  your
home folder, then you would do:
/pastero /home/<user_name>/Documents/Scripts/my_script.py
* This would upload my_script.py and return the URL."""


try:
    import weechat as w
    WEECHAT_RC_OK = w.WEECHAT_RC_OK
    import_ok = True

except ImportError:
    print "This script must be run under WeeChat."
    print "Get WeeChat now at: http://www.weechat.org/"
    import_ok = False


def pastero_cmd_cb(data, buffer, args):
    global Ext
    url = "https://ptpb.pw/"
    paster = "curl -sSF c=@%s %s" % (args, url)

    if args.count(".") > 0:
        Ext = args.split(".")
        Ext.reverse()
    else:
        Ext = " " # Ugly hack so Ext[0] doesn't complain in case is empty :>

    if args != "":
        w.hook_process(paster, 5 * 1000, "upload_cb", "")
    else:
        w.prnt(w.current_buffer(),
                     "%s\tPlease, specify a file to upload." % PREFIX)

    return WEECHAT_RC_OK


def upload_cb(data, command, return_code, out, err):
    if return_code == w.WEECHAT_HOOK_PROCESS_ERROR:
        w.prnt("", "Error with command %s" % command)
        return WEECHAT_RC_OK

    if out != "":
        url = out.splitlines()
        string = "Here is the " + url[4].rstrip() + "/" + Ext[0]
        w.command(w.current_buffer(), string)

    if err != "":
        w.prnt("", "stderr: %s" % err)

    return WEECHAT_RC_OK


if __name__ == "__main__" and import_ok:
    if w.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE,
                  SCRIPT_DESC, "", ""):
        
        w.hook_command(SCRIPT_NAME, SCRIPT_DESC, "",SCRIPT_HELP,
                             "", "pastero_cmd_cb", "")
