
# Merge 2 Dictionary

dic1 = {'c':3,'d':4,'e':'Hello'}

dic2 = {'a':1,'b':2}

merger_dict = dic1.copy()
merger_dict.update(dic2)
print(merger_dict)
print(type(dic2))

# Swaping Dictionary key & Values

def swap_dict(dict_):
        min_val = min(dict_.values())
        max_val = max(dict_.values())

        for key, value in dict_.items():
                if value == min_val:
                        dict_[key] = max_val
                elif value == max_val:
                        dict_[key] = min_val
        return dict_

dict_ = {'a':1,'b':2,'c':3}
print('Before Swap Dictionary = ',dict_)

result = swap_dict(dict_)

print('After Swap Dictionary = ',result)
