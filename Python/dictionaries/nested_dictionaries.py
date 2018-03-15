'''We can nest values and keys within values and keys just like in
lists and tuples, as follows:'''

nested_dict = {'key_a':{'key_a':'a1','key_b':'a2'},'key_b':'b'}

print nested_dict['key_a']['key_a'] #Returns 'a1'
