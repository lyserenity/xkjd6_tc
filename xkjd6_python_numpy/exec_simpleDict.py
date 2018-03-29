#!/usr/bin/env python
#coding:utf-8


import numpy as np
import json
import re
#import os
import io


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

# =============================================================================

origin_lst =[]

lookup_lst = []
freq_ls = []
lst_2 = []
lst_3 = []
new_code = []
test_code = []

new_lst = []

input_file = 'test.txt'
with io.open(input_file, 'r', encoding = 'utf8') as lookup_file:
    lookup_word = np.loadtxt(lookup_file, dtype = np.str, delimiter = '\t')
    for row in range(lookup_word.shape[0]):
        print(row)
        try:
            if (len(lookup_word[row-1,0]) <= 2 and len(lookup_word[row-1,1]) == 3) or re.search(r'[A-Za-z0-9]',lookup_word[row-1,0]) is not None:
                try:
                    origin_lst.append([lookup_word[row-1,0],lookup_word[row-1,1]])
                    test_code.append(lookup_word[row-1,1])
                except AttributeError:
                    lookup_lst.append(str(lookup_word[row-1,0]))
            else:
                lookup_lst.append(str(lookup_word[row-1,0]))
        except IndexError:
            lookup_lst.append(str(lookup_word[row,0]))
write_file = 'test_result.txt'
output_file = io.open(write_file, 'w', encoding = 'utf8')


with io.open('xkjd6.json', 'r', encoding = 'utf8') as infile:
    data = json.load(infile) # danzi for dict

for phr_hasKey in lookup_lst:
    get_phr = str(phr_hasKey)
    for word in get_phr:
        word = str(word)
        while re.match(r'(。|？|，|、|：|“)', word) is not None:
            break
        else:
            while word in data:
                break
            else:
                for i in range(1,lookup_word.shape[0]+1):
                    while phr_hasKey == lookup_word[i-1,0]:
                       origin_lst.append([lookup_word[i-1,0],lookup_word[i-1,1]])
                       test_code.append(lookup_word[row-1,1])
                       lookup_lst.pop(lookup_lst.index(get_phr))
                       break                
 #               lookup_lst.pop(lookup_lst.index(get_phr))
                

 
for phr in lookup_lst:
    get_phr = re.sub(r'^(.+)(。|？|，|、|：|“)+$', r'\1', str(phr))
    for word in get_phr:
        word = str(word)
        while re.match(r'(。|？|，|、|：|“)', word) is not None:
            break
        else:
            word_data = data[word]["DATA"]
            for multi in word_data:
                freq_ls.append(multi["freq"])
            word_freq = freq_ls.index(max(freq_ls))
            lst_2.append(word_data[word_freq]["pronun"])
            lst_3.append(data[word]["BBBB"][0])
            freq_ls.clear()
                
    phr_code = "".join(lst_2)+"".join(lst_3)


    if len(get_phr) <= 2:
        v = phr_code
        vs = simp_code(v,test_code)
    elif len(get_phr) == 3:
        v = Split_SSBB(phr_code).woavuio(0,6,2)+Split_SSBB(phr_code).woavuio(5,6,1)+Split_SSBB(phr_code).avuio(0,2)
        vs = simp_code(v,test_code)

    else:
        v = Split_SSBB(phr_code).woavuio(0,6,2)+Split_SSBB(phr_code).woavuio(-2,-1,1)+Split_SSBB(phr_code).avuio(0,2)
        vs = simp_code(v,test_code)

    new_lst.append([str(phr),str(vs)])

    
    lst_2.clear()
    lst_3.clear()

new_lst.extend(origin_lst)
new_sort_lst = sorted(new_lst,key=lambda phrCode:phrCode[1])

for k in new_sort_lst:
    output_file.write(k[0]+"\t"+k[1]+"\n")

output_file.close()

