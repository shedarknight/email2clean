import argparse

def composeArguments():
     parser.add_argument('--extract', help="search for and extract email addresses from csv", type=str)
     parser.add_argument("sourceFile", help="source File name", type=str)
     return parser.parse_args()

parser = argparse.ArgumentParser(
   prog='email2clean'
   )
   
args=composeArguments()

parser.print_help()


