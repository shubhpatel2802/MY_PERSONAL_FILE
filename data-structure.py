"""
Python data structures are essentially containers for different kinds of data. The four main types are lists, sets, tuples and dictionaries.

1] list - ordered, mutable, dublicat-items allowed
syntax :
list_name = []
list_name = list()

# define empty list
# product = []
# product = list()
# print(len(product))
# print(type(product))

# random_data = [10, 10.4, 'demo', 3+9j ]
# print(random_data)

products = ['milk', 'butter-milk', 'pen']

veg = ['tomato', 'potato', 'onion']

# # merge two or more list
# print(veg + products)

# print(veg * 2)

# list methods
# total = veg * 2
# total.sort()
# total.sort()
# print(total)

fruit = ['apple', 'guava', 'orange']

# add data
# veg.append(fruit)
# veg.extend(fruit)
# veg.insert(0, "brinjal")
# print(veg)


# count, index, copy

# update data
# veg[0] = "cabbage"
# print(veg)

# delete data
# veg.pop() # remove element from the last
# veg.remove("tomato")
# veg.clear()
# veg.reverse()
# print(dir(veg))

2] tuple - ordered, immutable, duplicate value allowed
syntax :
tuple_name = ()
tuple_name = tuple()

L = [1,1,1,1,2,3,4,5]
# you can update list
tuple_data = tuple(L)
print(tuple_data)
# print(dir(tuple_data))
# print(tuple_data.count(1))
# print(tuple_data.index(3))

3] set - unordered, mutable, duplicate value are not allowed
print(set(tuple_data))

4] frozenset - unordered, immutable, duplicate value are not allowed

5] Dictionary 
contacts = {
    'A':{
        'aman':{
            'mobile':['000', '111']
        },
        'ajay':{
            'mobile':['222']
        }
    },
    'B':{
        'babbn':{
            'mobile':['333']
        }
    },
    'C':{
        'chintu':{
            'mobile':['444', '555', '666']
        }
    },
    'C':{
        'chintu':{
            'mobile':['444', '555', '777']
        }
    },
}


# print(contacts)
# print(contacts['A']['ajay']['mobile'][0])
# print(contacts['C'])
# print(len(contacts))
# print(dir(contacts))

#  'clear', 'copy', 'get', 'items', 'keys', 'values', 


# contacts.clear()
# p2 = contacts.copy()
# print(p2)

# print(contacts.get('A'))

# print(contacts.keys())
# print(contacts.values())
# print(contacts.items())


# 'pop', 'popitem', 'setdefault', 'update', 'fromkeys'

# contacts.pop('C')
# contacts.popitem()

new_contacts = {
    'D':{
        'dhimen':{
            'mobile': ['555-666']
        }
    },
    'E':{
        'eric':{
            'mobile':['666-777']
        }
    }
} 

contacts.update(new_contacts)
# print(contacts)

veg_dict = {}
veg = ['tomato', 'potato', 'onion']
price = 50


newDict = veg_dict.fromkeys(veg, price)

newDict.setdefault("cabbage", 150)
print(newDict)





"""

contacts = {
    'A':{
        'aman':{
            'mobile':['000', '111']
        },
        'ajay':{
            'mobile':['222']
        }
    },
    'B':{
        'babbn':{
            'mobile':['333']
        }
    },
    'C':{
        'chintu':{
            'mobile':['444', '555', '666']
        }
    },
    'C':{
        'chintu':{
            'mobile':['444', '555', '777']
        }
    },
}