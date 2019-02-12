Mario Kart - Changelog

```
Structure of changelog

#### Added

#### Changed

#### Fixed

```

### [NEXT_RELEASE]

#### Added
    - Method show_drivers_average_speed on race manager
    - Method show_best_lap_of_race on race manager
    - Method show_best_drivers_lap on race manager
    - Main file to show results
    - Manager Race
    - Expection manager file
    - Service Position
    - Method milliseconds_to_text on date utils
    - Model Position
    - Helpers with methods convert_text_to_lap and _create_driver
    - Expection helper file
    - Utils with methods text_hour_to_milliseconds and text_minutes_to_milliseconds
    - Service File
    - Expection service file
    - Model Lap
    - Model Driver
    - Coveralls integration
    - CircleCI integration
    - Folders mkart, docs and tests to start the project

#### Changed
    - Model Driver to to have the average_speed as an attribute
    - Main file to show best lap of race
    - Main file to show best drivers lap
    - Refactor Service Position to create Service Lap
    - Service File to check file on instace of class
    - Separating requirements dev from test
    - Docs to show how run the project
    - Model Driver
    - README file to show badge of docs

#### Fixed
    - Typo on __main__ file