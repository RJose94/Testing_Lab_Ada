import unittest
from datetime import datetime

class Greeter:
    def greet(self, name):
        name = name.strip().capitalize()
        hour = datetime.now().hour

        if 6 <= hour < 12:
            greeting = 'Buenos dias'
        elif 18 <= hour < 22:
            greeting = 'Buenas tardes'
        else:
            greeting = 'Buenas noches'

        print(f'{greeting} {name}')
        return f'{greeting} {name}'


class TestGreeter(unittest.TestCase):
    def test_greet(self):
        greeter = Greeter()
        hour = datetime.now().hour
        if 6 <= hour < 12:
            expected_greeting = 'Buenos dias Jose'
        elif 18 <= hour < 22:
            expected_greeting = 'Buenas tardes Jose'
        else:
            expected_greeting = 'Buenas noches Jose'
        self.assertEqual(greeter.greet(' Jose '), expected_greeting)

if __name__ == '__main__':
    unittest.main()
