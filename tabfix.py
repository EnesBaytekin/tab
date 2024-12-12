#!/usr/bin/python

from sys import argv
from shutil import copy2
from os.path import getmtime
from time import sleep

def convert_spaces_to_tabs(input_file_name, output_file_name, tab_length):
    input_file = open(input_file_name, "r")
    lines = input_file.readlines()
    input_file.close()
    output_file = open(output_file_name, "w")
    for line in lines:
        space_count = 0
        for index in range(len(line)):
            char = line[index]
            if char == " ":
                space_count += 1
            elif char == "\t":
                space_count += tab_length
            else:
                line_data = line[index:]
                break
        tabs = (space_count//tab_length)*"\t"
        spaces = (space_count%tab_length)*" "
        output_file.write(tabs+spaces+line_data)
    output_file.close()

def help():
    print("""\
Usage:
        tabfix [options] <file_name>
OR      tabfix [options] <file_name> <tab_length>

Options:
  -w, --watch       Watch the file and fix tabs on save.
  -h, --help        Show this help menu.

(default tab length is 4)\
""")
    exit(0)

def main():
    argv.pop(0)

    if len(argv) == 0 or "--help" in argv or "-h" in argv:
        help()

    watch_mode = False
    while "--watch" in argv:
        watch_mode = True
        argv.remove("--watch")
    while "-w" in argv:
        watch_mode = True
        argv.remove("-w")

    file_name = argv.pop(0)
    if len(argv):
        tab_length = argv.pop(0)
    else:
        tab_length = 4
    
    if watch_mode:
        output_file_name = ".tabbackup."+file_name
        copy2(file_name, output_file_name)
        last_modified_time = getmtime(file_name)
        while True:
            current_modified_time = getmtime(file_name)
            if current_modified_time != last_modified_time:
                last_modified_time = current_modified_time
                convert_spaces_to_tabs(file_name, file_name, tab_length)
            sleep(1)
    else:
        output_file_name = ".tabfixed."+file_name
        convert_spaces_to_tabs(file_name, output_file_name, tab_length)

if __name__ == "__main__":
    main()
