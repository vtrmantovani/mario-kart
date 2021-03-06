# Mario Kart

Shows the race result from a log file with pattern:  

```
Hora (Hour),
Piloto (Driver),
Nº Volta (Lap number),
Tempo Volta (Lap duration),
Velocidade média da volta (Average lap speed)
```

[File Example](example.log)


## Dependencies

- [Python 3.6](https://www.python.org/downloads/)


## Set up

1.  Create a virtualenv with python 3.6:

    ```
    virtualenv -p python3 .venv
    ```

2.  Active the virtualenv:

    ```
    source .venv/bin/activate
    ```

3. Install the project:

    ```
    pip install .
    ```


## Usage Example

### Run the comand with example.log file:
``` 
    mario-kart -f example.log 
```

### Example Return Success

```
======RESULT OF KART RACE======
POSITION - DRIVER - FINISHED LAPS - DURATION
1 038-F.MASS 4 4:11.578
2 002-K.RAIKKONEN 4 4:15.153
3 033-R.BARRICHELLO 4 4:16.080
4 023-M.WEBBER 4 4:17.722
5 015-F.ALONSO 4 4:54.221
6 011-S.VETTEL 3 6:27.276
===============================


=======BEST DRIVERS LAP=======
DRIVER - LAP - DURATION
038-F.MASSA 3 1:02.769
002-K.RAIKKONEN 4 1:03.076
033-R.BARRICHELLO 3 1:03.716
023-M.WEBBER 4 1:04.216
015-F.ALONSO 2 1:07.011
011-S.VETTEL 3 1:18.097
===============================


=======BEST LAP OF RACE=======
DRIVER - DURATION
038-F.MASSA 1:02.769
===============================


=====DRIVERS AVERAGE SPEED=====
DRIVER - AVERAGE SPEED
038-F.MASSA 44.246
002-K.RAIKKONEN 43.627
033-R.BARRICHELLO 43.468
023-M.WEBBER 43.191
015-F.ALONSO 38.066
011-S.VETTEL 25.746
===============================


====TIME DRIVERS AFTER WINER====
DRIVER - FINISHED LAPS - TIME
002-K.RAIKKONEN 4 0:03.575
033-R.BARRICHELLO 4 0:04.502
023-M.WEBBER 4 0:06.144
015-F.ALONSO 4 0:42.643
011-S.VETTEL 3 6:27.276
===============================
```

### Example Return Erros

```
* File is empty
* File not found
* File not match with pattern
* Line '{x}' not match with pattern

{x} = Line of file with don't match with pattern
```
 

## Run the tests

1.  Create a virtualenv with python 3.6:

    ```
    virtualenv -p python3 .venv
    ```

2.  Active the virtualenv:

    ```
    source .venv/bin/activate
    ```

3. Install the Python dependencies:

    ```
    make requirements-test
    ```

4. Run the command:

    ```
    make test
    ```
