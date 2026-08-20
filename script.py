import os
import sys

def main(file_name: str, txt: str):
    if not os.path.exists('./' + file_name):
        sys.exit()
    with open(file_name, 'r') as s:
        if txt in s.read():
            print(f'we found {txt}')
        else:
            sys.exit()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])