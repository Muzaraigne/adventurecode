a ='mypyemv (1058) -> tdssotr, pebnvks, zaulju'
node = {
    'name' :'mypyemv',
    'taille' : 1058,
    'fils' : ['tdssotr','pebnvks','zaulju']
}

print(a.split(' '))
print(a.split(' ')[1].strip('()'))
if node.get('fils'):
    print(node.get('fils'))
    print(node)
    b = node.pop('fils')
    print(b)
    print(node.values()
          )
    