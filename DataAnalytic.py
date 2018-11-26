
import pandas as pd
import numpy as np
import scipy as sc
from collections import Counter

def frac(u):
    v = u -int(u)
    return v
def sort(x):
    if x == sorted(x):
        return True 
    if x[::-1] == sorted(x):
        return True
    return False 
def reverse(D):
    ans = {}
    for k in D:
        v = D[k]
        if v not in ans:
            ans[v] = k
        else:
            
            ans[v] = [ans[v]] + [k]
    return ans
def longestSequence(M):
    p = 0
    for i in range (len(M)):
        v = M.count(M[i])
        if v > p:
            p = v
            s = i
    return M[s]*p
def cirShift(L,n):
    while n > len(L):
        n = n - len(L)    
    new_L = L[-n:] + L[:-n]
    return new_L
def balance(fName):
    i = 0
    with open('fName','r') as f:
        logfile= f.read()  
#if type(logfile) == dict:
# is it possible to have dictionary file or string with integer values
    if type(logfile) == str:
        new_logfile = logfile.split('\n')
        listb = []
        for k in new_logfile:
            DOW = new_logfile[i][0]
            if DOW == 'D':
                new_k = float(new_logfile[i][2:])
            else:
                new_k = float(new_logfile[i][2:])*-1
            listb.append(new_k)
            i+=1
        balance = sum(listb)
        return balance
    return 'data can not be handeled'
def top(fName):
    with open('sales.txt') as f:
        content = f.read().splitlines()
        df_names = {}
        j = 0
        k = 2
        #create the first information
        for i in range(len(content)):
            df = content[i].split(',')
            if df[j] not in df_names:
                df_names[df[j]] = float(df[k])
            else:
                df_names[df[j]] = [df_names[df[j]]] + [float(df[k])]
        for key in df_names:
            if type(df_names[key]) == list:
                df_names[key] = sum(df_names[key])
            else:
                df_names[key] = df_names[key] 
        h_amount = 0
        for key in df_names:
            if h_amount < df_names[key]:
                h_amount = df_names[key]
                t_cus = key
        #create the second information
        new_list = []
        for i in range(len(content)):
            df2 = content[i].split(',')
            new_list = new_list + [df2[1]]
        new_list_dict = Counter(new_list)
        number_tran = 0
        for key in new_list_dict:
            if number_tran < new_list_dict[key]:
                number_tran = new_list_dict[key]
                t_prod = key

        print('The top customer is %s with total amount $%s' % (t_cus,int(h_amount)))
        print('The top product is %s as it appears in %s transactions' % (t_prod,number_tran))
def sum_row_col(filename):
    df = pd.read_csv(filename, sep=",", header=None, names=["a", "b", "c","d"])
    for i in range(len(df)):
        df.loc[i,'sum_row'] =sum(df.iloc[i,0:4])
    lis = []
    for j in df:
        lis = lis + [sum(df[j])]
    s = pd.Series(lis, index=["a", "b", "c","d","sum_row"])
    df2 =df.append(s,ignore_index = True)
    return df2
    