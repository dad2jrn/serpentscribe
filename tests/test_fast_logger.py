import unittest
import json
from fast_logger.fast_logger import log_output

# A sample function to be decorated
@log_output
def sample_function(a, b):
    return a + b

class TestFastLogger(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log_file = 'function_log.json'

    def test_sample_function(self):
        # Clear the log file before the test
        open(self.log_file, 'w').close()

        # Run the sample function
        result = sample_function(3, 4)
        self.assertEqual(result, 7)

        # Verify the log entry
        with open(self.log_file, 'r') as file:
            logs = file.readlines()
            self.assertEqual(len(logs), 1)

            log_entry = json.loads(logs[0])
            self.assertEqual(log_entry['function'], 'sample_function')
            self.assertEqual(log_entry['arguments']['args'], [3, 4])
            self.assertEqual(log_entry['arguments']['kwargs'], {})
            self.assertEqual(log_entry['result'], 7)

    @classmethod
    def tearDownClass(cls):
        # Clean up (optional)
        pass

if __name__ == '__main__':
    unittest.main()
