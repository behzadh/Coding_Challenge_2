class CoinChangeMachine:

    '''
    This Class will perform an algorithm to return the number of solutions for an exchange value
    (ex £2-30) with specific coins available in a new exchange machine.

    __init__(self, available_coins: list = [1, 2, 5, 10, 20, 50, 100, 200])
    value_to_exchange(self, exchange_value: str)
    number_of_coin_combinations(self, user_input: str):
    main(self)
    '''
    
    def __init__(self, available_coins: list = [1, 2, 5, 10, 20, 50, 100, 200]):

        '''
        Initialize the list of available coins and its length

        Parameters
        ----------
        available_coins (list)
            Represents the list of available coins. The default is [1p, 2p, 5p, 10p, 20p, 50p, £1, £2]
        '''

        self.available_coins_for_change = available_coins
        self.number_of_coins = len(self.available_coins_for_change)

    def value_to_exchange(self, exchange_value: str):

        '''
        In this method, first the format of input value will be checked which should be like 
        £{Pound}-{Pence}, for example, £2-30'. Then, fills the possible empty {Pound} or {Pence}
        values and convert the total value to the pence format, for example £2-30 is 230 pence.

        Parameters
        ----------
        exchange_value (str)
            Value of the exchange amount

        Returns
        -------
        exchange_value (int)
            Returns value of the exchange amount in pence
        '''
        
        if '£' not in exchange_value or '-' not in exchange_value:
            raise ValueError('Please check the format of your input. It should be in the format of £{Pound}-{Pence}, for example, £2-30')
        else:
            get_user_money = exchange_value[1:].split('-')
            if get_user_money[0] == '':
                get_user_money[0] = '0'
            if get_user_money[1] == '':
                get_user_money[1] = '00'
            if len(get_user_money[1]) != 2:
                raise ValueError('Please enter Pense in two digit format')
            print(f'\nYou have asked to exchange the amount of £{get_user_money[0]}-{get_user_money[1]}')

            exchange_value = int(get_user_money[0]+get_user_money[1])
            return exchange_value

    def number_of_coin_combinations(self, input_amount: str):
        
        '''
        This method computes solutions of coin combinations for a given amount.

        Logic: The idea is to create a "reference list" with length of (value+1) in which the first
        element always hold a base reference as 1 and the rest are 0 (in the length of "value"). For ex.
        for £0-05 (5 p) the reference list will be [1, 0, 0, 0, 0, 0].
        For each given value, all available coins will be selected one by one, and accordingly updates
        the "reference list".

        Parameters
        ----------
        input_amount (str)
            Value of the exchange amount

        Returns
        -------
        number_of_combinations (int)
            Returns number of solutions for coin combinations
        '''

        # Gets the exchange value in the format of pence
        value = self.value_to_exchange(input_amount)

        # Creates the 'reference list'
        reference_list_for_value = [0]*(value+1)

        # Setting the first element to 1 as a reference value. 
        reference_list_for_value[0] = 1
        
        # Loop over the number of exsiting available coins
        for i in range(0,self.number_of_coins):
            # Selecting coins one by one and update the reference list from the range of coin value
            # and the value+1
            for j in range(self.available_coins_for_change[i],value+1):
                # Updates the values of refernce list by using the base reference value
                reference_list_for_value[j] += reference_list_for_value[j-self.available_coins_for_change[i]]
                # Updates number of solutions up to the end
                number_of_combinations = reference_list_for_value[j]
        # In cases that the insert value is equal to amount of one of the coins, the algorithm computes
        # one more option with the same amount. For example, for 5p one of the options is to give the exchange
        # same as 5p. To avoid that, if the given amount is equal to one of the coins, number of solutions
        # will be subtracted by 1
        if value in self.available_coins_for_change:
            number_of_combinations = number_of_combinations - 1
        print('Number of solutions for exchange coin combinations are: ', number_of_combinations, '\n')
        
        return number_of_combinations

    def main(self):

        value = '£0-06'
        self.number_of_coin_combinations(value)

if __name__ == '__main__':
    con = CoinChangeMachine() 
    con.main()
