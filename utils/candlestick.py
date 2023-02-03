import pandas as pd
from datetime import datetime, timedelta
import plotly.figure_factory
from pandas.tseries.frequencies import to_offset

pd.options.mode.chained_assignment = None

class BreakoutDetection:

    '''
    A Class to get data from a pickle file and perform a candlestick plot 
    and to detect the related breakout for any given periods. It has the 
    following class methods:

    __init__(self)
    load_data(self)
    plot_candlestick(self, df: pd.DataFrame(), frequency: str)
    get_candlestick_chart(self, begin, end,  frequency: str = '3H')
    detect_breakout(self, begin, end, frequency: str, plot_chart=False)
    main(self)
    '''

    def __init__(self) -> None:

        self.path = '/Users/behzad/My_codings/Coding_Challenge_2/raw_data/'

    def load_data(self):

        '''
        Loads raw data and replace Venue A and B with Venue AB as they are the same product 
        trading in two different venues.

        RETURNS
        -------
        a data frame (DataFrame)
            It returens a pandas DataFrame
        '''
        return pd.read_pickle(self.path + "PriceData.pickle")

    def plot_candlestick(self, df: pd.DataFrame(), frequency: str):

        """
        A method to draw a cabdlestick plot.

        Parameters
        ----------
        df (DataFrame)
            A dataframe for candelstick plot
        contract (str)
            contract(s) of each product tradings
        """

        fig = plotly.figure_factory.create_candlestick(
                                    df.resample(frequency).first(), 
                                    df.resample(frequency).max(), 
                                    df.resample(frequency).min(), 
                                    df.resample(frequency).last(), 
                                    dates=df.resample(frequency).first().index.astype('str')
                                    )
        fig.show()

    def get_candlestick_chart(self, begin, end,  frequency: str = '3H'):

        '''
        Candlestick plot for each spesific contract provided

        Parameters
        ----------
        df (DataFrame)
            OHLC style dataframe for candelstick plot
        contract (str)
            contract(s) of each product tradings
        '''

        df = self.load_data()
        df_selected = df[(df.index >= begin) & (df.index <= end)]

        self.plot_candlestick(df_selected, frequency)

    def detect_breakout(self, begin, end, frequency: str, plot_chart=False):

        """
        
        """

        df = self.load_data()
        
        df_selected = df[(df.index >= begin) & (df.index <= end)]
        df_selected['Close'] = df.resample(frequency).last()
        last_close = df_selected[-1:]['Close'].values[0]

        if plot_chart == True:
            self.plot_candlestick(df_selected, frequency)

        return False

    def main(self):
        
        begin = datetime(2022, 1, 3, 0, 0)
        end = datetime(2022, 1, 3, 13, 59)
        freq = '10Min'

        result = self.get_candlestick_chart(begin,end,freq)
        print(result)  
        
if __name__ == '__main__':
    det = BreakoutDetection() 
    det.main()


    