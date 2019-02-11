import getopt
import sys

from mkart.exceptions.manager import ManagerException
from mkart.manager.race import RaceManager


def show_avalibe_commands():
    print("Available Commands:")
    print(" * mkart -f <file.log> Process race result from a log file")


def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:f:", ["file="])
    except getopt.GetoptError:
        show_avalibe_commands()
        sys.exit()

    for opt, arg in opts:
        if opt == '-h':
            print('mkart -f <file.log>')
            sys.exit()
        elif opt in ("-f", "--file"):
            try:
                race_manager = RaceManager(arg)
                race_manager.show_result()

            except ManagerException as e:
                print(e)
            sys.exit()

    show_avalibe_commands()
    sys.exit()


if __name__ == "__main__":
    main()
