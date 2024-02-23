import argparse
from helper import Cleaner

def main():
    parser = argparse.ArgumentParser(prog= 'Whomis', 
    description='Whomis is a command-line version of whois.', 
    epilog='To run type: py whomis.py followed by a domain name.')
    parser.add_argument('Domain', help='This web tool is useful in gathering IP and domain info.')
    parser.add_argument('--version', action='version', version='%(prog)s 0.0.1')
    args = parser.parse_args()
    var = Cleaner(args)
    var.clean()




if __name__ == "__main__":
    main()