#!/usr/bin/python
"""
    Pass a json mapping file with the file mapping:
        { "alib.js": ["lib/a.js", "lib/a1.js"], "blib.js": ["lib/b.js", "lib/b1.js"] }
"""
import os
import json
import argparse


def merge(file_list):
    merged = u""
    for f in file_list:
        with open(f, 'r') as f_h:
            merged += "\n" + f_h.read()
    return merged


parser = argparse.ArgumentParser(description='Concat JS files per mapping.')
parser.add_argument('mapping', metavar='m', type=unicode, nargs='+',
                   help='Mapping file')

args = parser.parse_args()

for mapping_file in args.mapping:
    if os.path.isfile(mapping_file):
        f = open(mapping_file, 'r')
        print u"Processing mapping file: {}".format(mapping_file,)
        mapping_json = json.load(f)
        for concat_file in mapping_json:
            with open(concat_file, 'w') as concat_file_h:
                concat_file_h.write(merge(mapping_json[concat_file]))
    else:
        print u"mapping file {} does not exits.".format(mapping_file,)
