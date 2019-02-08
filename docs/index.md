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

3. Install the Python dependencies:

    ```
    make requirements-dev
    ```


## Run the tests

1. Run the command:

    ```
    make test
    ```
