mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':0}

# How to sort a dict by value Python 3>
{key:value for key, value in sorted(mydict.items(), key=lambda kv: (kv[1], kv[0]))}



# How to sort a dict by value Python 2>
{key:value for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k))}


# How to sort a dict by key Python 3>
{key:mydict[key] for key in sorted(mydict.keys())}



# How to sort a dict by key Python 2>
{key:mydict[key] for key in sorted(mydict.iterkeys())}
