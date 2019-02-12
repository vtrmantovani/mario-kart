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

### Return

```
======RESULT OF KART RACE======
1 038 F.MASS 4 0:04:11.578000
2 002 K.RAIKKONEN 4 0:04:15.153000
3 033 R.BARRICHELLO 4 0:04:16.080000
4 023 M.WEBBER 4 0:04:17.722000
5 015 F.ALONSO 4 0:04:54.221000
6 011 S.VETTEL 3 0:06:27.276000
===============================


=======BEST DRIVERS LAP=======
038 F.MASSA 3 0:01:02.769000
002 K.RAIKKONEN 4 0:01:03.076000
033 R.BARRICHELLO 3 0:01:03.716000
023 M.WEBBER 4 0:01:04.216000
015 F.ALONSO 2 0:01:07.011000
011 S.VETTEL 3 0:01:18.097000
===============================


=======BEST LAP OF RACE=======
038 F.MASSA 0:01:02.769000
===============================
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
