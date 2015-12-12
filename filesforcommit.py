#!/usr/bin/python
"""
  lists all files modified for commits with given commit message
"""

import subprocess
import argparse

parser = argparse.ArgumentParser(description='Files changed for commit message')
parser.add_argument('message', metavar='message', type=unicode, nargs=1,
                   help='Commit message')

args = parser.parse_args()
message = args.message[0]
sha_command = "git log -i --grep=\""+message+"\" --format=format:%H"
shas = subprocess.check_output(sha_command)
print message
print sha_command

file_names = []
if shas:
	for sha in shas.split("\n"):
		file_names.extend(subprocess.check_output("git show "+sha+" --name-only --format=format:").split("\n"))
	print "\n".join(list(set(file_names) - set([""])))
else:
	print "No commits found for message:"+message
