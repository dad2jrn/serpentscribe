# SerpentScribe

`serpentscribe` is a simple, yet powerful Python logging library designed to make function call logging effortless. It provides a decorator to automatically log the details of function calls, including arguments and return values, to a JSON file.

## Features

- Easy to use: Simply decorate your functions to start logging.
- Logs function name, arguments, return values, and timestamp.
- Customizable log file path.

## Installation

Install `SerpentScribe` using pip:

```bash
pip install serpentscribe
```
## Usage

To use SerpentScribe, import the log_output decorator and apply it to any function:

```python
from serpentscribe.logger import log_output

@log_output
def my_function(arg1, arg2):
    # Function logic here
    return "Result"
```

By default, logs are written to function_log.json in the current directory. You can change the log file path by modifying the Logger class instantiation inside the decorator.

## Running Tests

To run tests, navigate to the root directory of the project and execute:

```bash
python -m unittest discover -s tests
```
Ensure you have a test suite available in the tests directory.

## Contribution

Contributions to SerpentScribe are welcome! Please read the contributing guidelines [CONTRIBUTION](/CONTRIBUTION.md) to get started.

## License

SerpentScribe is licensed under the MIT License. See the [LICENSE](/LICENSE) file for more details.

## Contact

For any queries or suggestions, feel free to contact the maintainer using Github