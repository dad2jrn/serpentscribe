# SerpentScribe

`serpentscribe` is a simple, yet powerful Python logging library designed to make function call logging effortless. No longer do you have to instantiate logging multiple times within a function or class.  This module provides a simple decorator to automatically log the details of function calls, including arguments and return values to stdout and optionally to a JSON file specified.

## Features

- Easy to use: Simply decorate your functions to start logging.
- Logs *function name*, *arguments* passed, return *values*, and *timestamp*.
- Customizable log file path when exporting to a file.

## Installation

Install `SerpentScribe` using `pipenv`:

```bash
pipenv install serpentscribe
```

or if you haven't graduated to `PIPENV` yet, (you probably should) you can install using `PIP`:

```bash
pip install serpentscribe
```

## Usage

To use SerpentScribe, import the log_output decorator and apply it to any function.  All inputs and outputs are logged to stdout and if specified, to a JSON file:

```python
from serpentscribe.logger import log_output

# Specify logger level (required) and file path (optional)
@log_output(logger_level="DEBUG", file_path="/path/to/log/file")
def my_function(arg1, arg2):
    # Function logic here
    return "Result"
```

## Logging Level

A logging level is a required argument when setting the decorator. The following are supported:

| LEVEL       | Description     |
| :------------- | -----------: |
| DEBUG   | Detailed information, typically only of interest to a developer trying to diagnose a problem. |
| INFO   | Confirmation that things are working as expected. |
| WARNING   | An indication that something unexpected happened, or that a problem might occur in the near future (e.g. ‘disk space low’). The software is still working as expected. |
| ERROR   | Due to a more serious problem, the software has not been able to perform some function. |
| CRITICAL   | A serious error, indicating that the program itself may be unable to continue running. |


## Logging to a File

SerpentScribe will always output to stdout.  If a file is specified, then logging will be sent to `stdout` as well as the specified file.
The log file will have the logs written in JSON format, which is both human-readable and easy to process programmatically. If a path for the log file is not specified, the logs will instead be written to `stdout`.

## Running Tests

To run tests, navigate to the root directory of the project and execute:

```bash
python -m unittest discover -s tests
```


## Contribution

Contributions to SerpentScribe are welcome! Please read the contributing guidelines [CONTRIBUTION](/CONTRIBUTION.md) to get started.

## License

SerpentScribe is licensed under the MIT License. See the [LICENSE](/LICENSE) file for more details.

## Contact

For any queries or suggestions, feel free to contact the maintainer using Github