import os

def main(file_name: str, txt: str):
    if not os.path.exists('./' + file_name):
        raise FileNotFoundError
    with open(file_name, 'r') as s:
        if txt in s.read():
            print(f'we found {txt}')

if __name__ == '__main__':
    main('test.txt', 'wow')