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
        self.assertEqual(greeter.greet(' Jose '), 'Hola Jose')

if __name__ == '__main__':
    unittest.main()
