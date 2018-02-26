import random

def GenerateDictionary(length, minval, maxval):
    return {"name%d"%(i+1):random.randint(minval,maxval) for i in range(length)}

def mean(dic):
    arr = list(dic.values())
    return sum(arr)/len(arr)

def var(dic):
    arr = list(dic.values())
    m =mean(dic)
    return sum([(arr[i] - m)**2 for i in range(len(arr))])/len(arr)

def findmin(dic):
    arr = list(dic.values())
    minval = min(arr)
    return {"value":minval, "names":[ key for key in dic.keys() if dic[key]==minval]}

def findmax(dic):
    arr = list(dic.values())
    maxval = max(arr)
    return {"value":maxval, "names": [ key for key in dic.keys() if dic[key]==maxval]}

def findavgclosest(dic):
    m = mean(dic)
    avgclosest=min([abs(dic[key]-m) for key in dic.keys()])
    names = [ key for key in dic.keys() if abs(dic[key]-m)==avgclosest]
    return {"value":dic[names[0]], "names":names}

X =GenerateDictionary(10, 1, 5)
print("Сгенерированный словарь:\n",X, sep="")
print("Среднее = %.3f"%mean(X))
print("Абс. сумма = %d"%sum(list(X.values())))
print("Дисперсия = %.3f"%var(X))
min_dic=findmin(X); avg_dic = findavgclosest(X); max_dic=findmax(X)
print("Человек с наименьшим долгом(%dруб):"%min_dic['value'],', '.join(min_dic['names']))
print("Человек с долгом, который ближе всего к среднему(%dруб):"%avg_dic['value'],', '.join(avg_dic['names']))
print("Человек с наибольшим долгом(%dруб):"%max_dic['value'],', '.join(max_dic['names']))



    
