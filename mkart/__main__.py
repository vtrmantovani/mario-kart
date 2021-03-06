import getopt
import sys

from mkart.exceptions.manager import ManagerException
from mkart.manager.race import RaceManager


def show_available_commands():
    print("Available Commands:")
    print(" * mkart -f <file.log> Process race result from a log file")


def show_text_line_break():
    print("===============================")


def show_text_result():
    print("\n")
    print("======RESULT OF KART RACE======")
    print("POSITION - DRIVER - FINISHED LAPS - DURATION")


def show_test_best_driver_lap():
    print("\n")
    print("=======BEST DRIVERS LAP=======")
    print("DRIVER - LAP - DURATION")


def show_test_best_lap_of_race_lap():
    print("\n")
    print("=======BEST LAP OF RACE=======")
    print("DRIVER - DURATION")


def show_test_drivers_average_speed():
    print("\n")
    print("=====DRIVERS AVERAGE SPEED=====")
    print("DRIVER - AVERAGE SPEED")


def show_text_time_drivers_after_winner():
    print("\n")
    print("====TIME DRIVERS AFTER WINER====")
    print("DRIVER - FINISHED LAPS - TIME")


def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:f:", ["file="])
    except getopt.GetoptError:
        show_available_commands()
        sys.exit()

    for opt, arg in opts:
        if opt == '-h':
            print('mkart -f <file.log>')
            sys.exit()
        elif opt in ("-f", "--file"):
            try:
                race_manager = RaceManager(arg)

                show_text_result()
                race_manager.show_result()
                show_text_line_break()

                show_test_best_driver_lap()
                race_manager.show_best_drivers_lap()
                show_text_line_break()

                show_test_best_lap_of_race_lap()
                race_manager.show_best_lap_of_race()
                show_text_line_break()

                show_test_drivers_average_speed()
                race_manager.show_drivers_average_speed()
                show_text_line_break()

                show_text_time_drivers_after_winner()
                race_manager.show_time_drivers_after_winner()
                show_text_line_break()

            except ManagerException as e:
                print(e)
            sys.exit()

    show_available_commands()
    sys.exit()


if __name__ == "__main__":
    main()
