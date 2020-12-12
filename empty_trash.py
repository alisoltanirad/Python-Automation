import os

def empty_trash():
    os.system('cd ~\nrm -Rf .Trash')

if __name__ == '__main__':
    empty_trash()