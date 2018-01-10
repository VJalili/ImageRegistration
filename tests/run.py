import unittest
from Basic import arguments
from Basic import parser

if __name__ == '__main__':
    # Test arguments
    suite = unittest.TestLoader().loadTestsFromModule(arguments)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Test parser
    suite = unittest.TestLoader().loadTestsFromModule(parser)
    unittest.TextTestRunner(verbosity=2).run(suite)
