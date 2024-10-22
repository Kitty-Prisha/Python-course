studentdata={'id1':{
    'Name':['Sara'],
    'class':['V'],
    'subject':['Math','Science','English']
},
'id2':{
    'Name':['Jack'],
    'class':['V'],
    'subject':['Math','Science','English']
}
}
result={}
for key,value in studentdata.items():
    if value not in result.values():
        result[key]=value
print(result)

