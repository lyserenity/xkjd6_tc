#!/usr/bin/env python3
#coding:utf-8



import numpy as np
import json
import re
# import os
import io
#import copy


class Split_SSBB(object):
    def __init__(self, tosplit):
        self.tosplit = tosplit
    
    def avuio(self, bi_start,bi_end,bi_step = 1):
        try:
            get_split = re.search(r'[avuio]+',self.tosplit).group()
            get_bbbb = get_split[bi_start:bi_end:bi_step]
            return  get_bbbb
        except AttributeError:
            pass

    def woavuio(self,bi_start,bi_end,bi_step = 1):
        try:
            get_split = re.search(r'[^avuio]+' ,self.tosplit).group()
            get_ssss = get_split[bi_start:bi_end:bi_step]
            return  get_ssss
        except AttributeError:
            pass

def simp_code(toSimp,test_code,k = 3):
    i = k
    while i <= len(toSimp):       
        if (toSimp[0:i] in test_code) and (i != 6):
                i += 1
                continue
        else:
            test_code.append(toSimp[0:i])
            return str(toSimp[0:i])
            break

def wordIN (word_lstIN,w_start,w_end,w_step=1,num=0):
        wb = []
        wi = word_lstIN[w_start:w_end:w_step]
        for wi in word_lstIN:
            wb.append(data[wi]["BBBB"][num])
        wb = "".join(wb)
        return wb

# =============================================================================

origin_lst =[]

lookup_lst = []
freq_ls = []
lst_2 = []
test_code = []

new_lst = []

input_file = "test_2.txt"
with open(input_file, 'r', encoding = 'utf8') as lookup_file:
    lookup_word = pd.read_csv(lookup_file, delimiter='\t', header=None,index_col=False,dtype=np.str)    
    print(lookup_word.shape[1])
    if lookup_word.shape[1] == 1:
        lookup_word['sybbbb']="#N/A"
    for row in range(len(lookup_word)):
        try:
            if (len(lookup_word.iloc[row,0]) <= 2 and len(lookup_word.iloc[row,1]) == 3) or re.search(r'[A-Za-z0-9]',lookup_word.iloc[row,0]) is not None:
                try:
                    origin_lst.append([lookup_word.iloc[row,0],lookup_word.iloc[row,1]])
                    test_code.append(lookup_word.iloc[row,1])
                except AttributeError:
                    lookup_lst.append(lookup_word.iloc[row,0])
            else:
                lookup_lst.append(str(lookup_word.iloc[row,0]))
        except IndexError:
            lookup_lst.append(str(lookup_word.iloc[row,0]))
# with io.open(input_file, 'r', encoding = 'utf8') as lookup_file:
#     lookup_word = np.loadtxt(lookup_file, dtype = np.str, delimiter = '\t')
#     for row in range(1,lookup_word.shape[0]+1):
#             lookup_lst.append([lookup_word[row-1,0],lookup_word[row-1,1]])

write_file = "test_2_result.txt"
output_file = io.open(write_file, 'w', encoding = 'utf8')


with io.open('xkjd6.json', 'r', encoding = 'utf8') as infile:
    data = json.load(infile) # danzi for dict


#lookup_lstCP = copy.deepcopy(lookup_lst)
i = 0
while i <= len(lookup_lst):
    try:
        if (len(lookup_lst[i][0]) <= 2 and len(lookup_lst[i][1]) == 3) or re.search(r'[A-Za-z0-9]',lookup_lst[i][0]) is not None:
             try:            
                origin_lst.append([lookup_lst[i][0],lookup_lst[i][1]])
                test_code.append(lookup_lst[i][1])
                lookup_lst.pop(lookup_lst.index(lookup_lst[i]))
                i = i - 1
             except IndexError:
                 pass
      
        else:
            word_hasKey = lookup_lst[i][0]
            for i_hasKey in range(len(word_hasKey)):
                while re.match(r'(。|？|，|、|：|“)', word_hasKey[i_hasKey]) is not None:               
                    break
                else:
                    try:
                        data[str(word_hasKey[i_hasKey])]
                    except KeyError:                                     
                        origin_lst.append([lookup_lst[i][0],lookup_lst[i][1]])
                        test_code.append(lookup_lst[i][1])
                        lookup_lst.pop(lookup_lst.index(lookup_lst[i]))                       
                        i = i -1
                        break
    except IndexError:
            pass
    i = i+1



for i in range(len(lookup_lst)):
    phr = lookup_lst[i][0]
    get_phr = re.sub(r'^(.+)(。|？|，|、|：|“)+$', r'\1', str(phr))
    
    for word in get_phr:
        word = str(word)
        while re.match(r'(。|？|，|、|：|“)', word) is not None:
            break # break if punctuation
        else:
            lst_2.append(word)
                
    check_lst = "".join(lst_2)
           
    pronun = str(lookup_lst[i][1])
    if len(phr) <= 2:
        v = pronun + wordIN(check_lst,0,2)
        vs = simp_code(v,test_code)
    elif len(get_phr) == 3:
        v = pronun + wordIN(check_lst,0,2)
        vs = simp_code(v,test_code)
    else:
        v = pronun + wordIN(check_lst,0,2)
        vs = simp_code(v,test_code)

    new_lst.append([str(phr),str(vs)])

    
    lst_2.clear()


new_lst.extend(origin_lst)
new_sort_lst = sorted(new_lst,key=lambda phrCode:phrCode[1])

for k in new_sort_lst:
    output_file.write(k[0]+"\t"+k[1]+"\n")

output_file.close()
