import unittest 
from coin_exchange import CoinChangeMachine

class TestCoinChangeMachine(unittest.TestCase):

    def test__init__(self):
        
        '''
        Tests if a given list and method for the init function
        '''
        
        obj = CoinChangeMachine([1, 2, 5])
        super(TestCoinChangeMachine, self).__init__()
        self.assertEqual(obj.available_coins_for_change, [1, 2, 5])  
        self.assertEqual(obj.number_of_coins, 3)    

    def test_value_to_exchange(self):

        '''
        Tests if the conversion of the given value to pence format
        '''
        
        obj = CoinChangeMachine()
        value = obj.value_to_exchange('£3-50')
        self.assertEqual(value, 350)

    def test_value_to_exchange_raiseError(self):

        '''
        Tests if the value errors are rasied
        '''
        
        obj = CoinChangeMachine()  
        with self.assertRaises(ValueError):
            value_err = obj.value_to_exchange('3-50')

    def test_number_of_coin_combinations(self):
        obj = CoinChangeMachine()
        n_comb = obj.number_of_coin_combinations('£0-05')
        self.assertEqual(n_comb, 3)
        n_comb2 = obj.number_of_coin_combinations('£0-06')
        self.assertEqual(n_comb2, 5)

if __name__ == "__main__":
    unittest.main(verbosity=3, exit=True)