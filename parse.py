# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:53:44 2019

@author: Jason
@e-mail: jasoncoding13@gmail.com
"""

if __name__ == '__main__':
    import pandas as pd
    df_tt = pd.read_json('./timetables.json', orient='records')
    df_tt = df_tt.sort_values(['Semester', 'ClientOrUOS', 'Purpose', 'Day'])
    df_tt.to_excel('./timetables.xlsx', index=False)
    print('The file is parsed successfully.')
