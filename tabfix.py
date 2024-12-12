#!/usr/bin/python

from sys import argv

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

def main():
    argv.pop(0)
    if len(argv) == 0:
        print("""\
Usage:  tabfix [file_name]
OR      tabfix [file_name] [tab_length]
(default tab length is 4)\
""")
        return

    file_name = argv.pop(0)
    if len(argv):
        tab_length = argv.pop(0)
    else:
        tab_length = 4
    
    output_file_name = ".tabfixed."+file_name
    convert_spaces_to_tabs(file_name, output_file_name, tab_length)

if __name__ == "__main__":
    main()
