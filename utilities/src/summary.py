import pandas as pd

'''
Function to calculate average value of each column in the dataframe and return as a dictionary

:param dataframe: dataframe to consider
:param columns_list: list of columns to calculate mean for
'''

class summary_of_dataframe():

    def __init__(self, input_dataframe, columns_list):
        self.dataframe = input_dataframe
        self.columns_list = columns_list

    def get_average(self):

        average_dict = {}
        columns = []

        if len(columns) == 0:
            columns = self.columns_list
        else:
            columns = self.dataframe.columns

        for i in columns:
            average_dict[i] = self.dataframe[i].mean()

        return average_dict


    '''
    Function to calculate median value of each column in the dataframe and return as a dictionary
    
    :param dataframe: dataframe to consider
    :param columns_list: list of columns to calculate median for
    '''


    def get_median(self):

        median_dict = {}
        columns = []

        if len(columns) == 0:
            columns = self.columns_list
        else:
            columns = self.dataframe.columns

        for i in columns:
            median_dict[i] = self.dataframe[i].median()

        return median_dict

    '''
    Function to calculate mode value of each column in the dataframe and return as a dictionary
    
    :param dataframe: dataframe to consider
    :param columns_list: list of columns to calculate mode for
    '''

    def get_mode(self):

        mode_dict = {}
        columns = []

        if len(columns) == 0:
            columns = self.columns_list
        else:
            columns = self.dataframe.columns

        for i in columns:
            mode_dict[i] = self.dataframe[i].mode()

        return mode_dict

    '''
    Function to calculate variance of each column in the dataframe and return as a dictionary
    
    :param dataframe: dataframe to consider
    :param columns_list: list of columns to calculate range for
    '''

    def get_variance(self):

        range_dict = {}
        columns = []

        if len(columns) == 0:
            columns = self.columns_list
        else:
            columns = self.dataframe.columns

        for i in columns:
            range_dict[i] = self.dataframe[i].var()

        return range_dict

    '''
    Function to calculate range value of each column in the dataframe and return as a dictionary
    
    :param dataframe: dataframe to consider
    :param columns_list: list of columns to calculate range for
    '''

    def get_range(self):

        range_dict = {}
        columns = []

        if len(columns) == 0:
            columns = self.columns_list
        else:
            columns = self.dataframe.columns

        for i in columns:
            range_dict[i] = self.dataframe[i].max() - self.dataframe[i].min()

        return range_dict