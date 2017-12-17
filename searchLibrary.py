import os
import pandas as pd
import utilities
import numpy as np
from app import artworkSet

#filter1
class stats():
    def __init__(self,df1):
        self.df = df1
        self.temp = ''
    def topTen(self,cat):
        temp = pd.pivot_table(self.df,index = cat, aggfunc = 'count')
        temp = temp.to_records()
        temp = pd.DataFrame(temp)
        temp = temp[[cat,'ConstituentID_x']]
        self.temp = temp
        tsum = temp['ConstituentID_x'].sum()
        temp1 = temp.sort_values(['ConstituentID_x'], ascending=[False], inplace=True)
        temp1 = temp
        temp1['Percent'] = temp1['ConstituentID_x']/tsum * 100
        temp1 = temp1.rename(index = str, columns = {'ConstituentID_x':'Count'})
        temp1 = temp1.head(n=10)
        #print("\tThis thing is a(n): {}  which is a {} class!".format(type(temp1), temp1.__class__.__name__))
        #temp1.describe()
        return str(temp1)
    def des(self):
        return self.temp.describe()


def runSearch(someNationality, someDepartment, startDate, endDate):
    print('\tStarting the search')
    df = artworkSet
    df[['Ayear', 'Amonth', 'Aday']] = df['DateAcquired'].str.split('-', expand=True)
    df['Ayear'] = df['Ayear'].replace(np.nan, 0, regex=True)
    df[df['Ayear'] == 'Y'] = 0
    df['Ayear'] = df['Ayear'].astype(str).astype(int)
    Search2 = utilities.inSr(someNationality, someDepartment, startDate, endDate)
    #Search2.crieteria()
    searched = Search2.ret()
    print('\tSetting the filters')
    if searched['inyear'] != 0 and searched['outyear'] != 0:
        filter1 = df[(df['Ayear'] >= searched['inyear']) & (df['Ayear'] <= searched['inyear'])]
    else:
        filter1 = df

    if Search2.blank1() != True and Search2.blank2() != True:
        filter1 = df[(df['Nationality_y'] == searched['nation']) & (df['Department'] == searched['dep'])]
    elif Search2.blank1() != True:
        filter1 = df[(df['Nationality_y'] == searched['nation'])]
    elif Search2.blank2() != True:
        filter1 = df[(df['Department'] == searched['dep'])]
    else:
        filter1 = df
    print('\tperforming the search')
    results = []
    ncl = stats(filter1)
    results.append(ncl.topTen('Artist'))
    #results += str(ncl.des())
    if Search2.blank1() == True:
        results.append(ncl.topTen('Nationality_y'))
    if Search2.blank2() == True:
        results.append(ncl.topTen('Department'))
    with open('searchResults.txt', 'w') as outFile:
        outFile.write('Search Results\n\t{}\n\t{}\n\t{}\n'.format(results[0], results[1], results[2]))
    outFile.close
    return results
