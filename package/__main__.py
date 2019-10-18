import sys
from package.app import app

if __name__ == '__main__':
    try:
        validAccountsListFile = sys.argv[1]
        transactionSummaryFile = sys.argv[2]
        a = app.App(validAccountsListFile, transactionSummaryFile)
    except IndexError:
        print("Front-end must have to arguments")
        exit(1)
