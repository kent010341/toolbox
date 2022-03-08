import os
import sys

folder_path = None
output_path = './output.txt'
base_ident = '    '

def args_parse(args):
    global folder_path, output_path

    iterator = iter(args)
    next(iterator)

    while True:
        try:
            arg = next(iterator)

            if arg == '--path' or arg == '-p':
                folder_path = next(iterator)
            elif arg == '--output' or arg == '-o':
                output_path = next(iterator)
            elif arg == '--help' or arg == '-h':
                print('Usage: python show_folder_tree.py [options]')
                print('    --path <folder path>, -p <folder path>')
                print('        path of the folder')
                print('    --output <file path>, -o <file path>')
                print('        output file name')
            else:
                print('unknown argument', arg)
                print('Use --help (or -h) to get the usage information.')
        except StopIteration:
            break

def write(s):
    with open(output_path, 'a') as f:
        f.write(s + '\n')

def list_files(ident, path, subfolder):
    sep = '' if path[-1] == '/' else '/'
    full_path = path + sep + subfolder
    
    dirs = sorted(os.listdir(full_path))
    str_indent = base_ident * ident

    for d in dirs:
        if d[-5:] != '.json':
            # not end with json => folder
            write(str_indent + d)
            list_files(ident+1, full_path, d)
        elif d[:-5] != subfolder:
            write(str_indent + d[:-5])

def main(args):
    args_parse(args)
    if folder_path == None:
        print('Folder name isn\'t specified, the option --path (-p) is reuqired.')
    else:
        list_files(0, folder_path, '')

if __name__ == '__main__':
    main(sys.argv)
