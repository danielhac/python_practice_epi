def function(self, a1, a2):
    arr = []

    for i in range(len(a1)):
        dct = {}

        if len(a1[i]) != len(a2[i]):
            arr.append('false')
            continue
        
        for char in range(len(a1[i])):
            if a1[i][char] not in dct:
                dct[a1[i][char]] = 1
            else:
                dct[a1[i][char]] += 1

        # This is the tricky part
        # Now we subtract from the matching values in the dct
        for char in range(len(a2[i])):
            if a2[i][char] not in dct:
                dct[a2[i][char]] = -1
            else:
                dct[a2[i][char]] -= 1
        
        # Then we use the absolute value from the existing dct values
        count = 0
        for val in dct.values():
            count += abs(val)
        
        if count > 3:
            arr.append('false')
        else:
            arr.append('true')
    
    print(arr)


#       [true, true, false, true,   false, true,  false]
arr1 = ['abca','aa', 'c',  'aaabc', 'aaa', 'abc', 'aaa']
arr2 = ['bcaa','ab', 'cc', 'aaabc', 'bbb', 'zbc', 'abc']


function("", arr1, arr2)
