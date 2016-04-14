__author__ = 'lyndsay.beaver'
n=['Lyndsay',' Beaver']

def join_strings(words):
    result=''
    for i in range(len(words)):
        result += words[i]
    return result
print (join_strings(n))