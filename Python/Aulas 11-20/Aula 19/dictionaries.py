#dictionary =  A changeable, unordered collection of unique key:value pairs
#                      Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlim'})
capitals.update({'USA':'New York'})
capitals.pop('China')
#capitals.clear()

#print(capitals['India'])       #prints the value related to the inserted key
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():  # prints the whole dictionary
    print(key, value)