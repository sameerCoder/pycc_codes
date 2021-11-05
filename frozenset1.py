#FrozenSet

fset1=frozenset({3,344,23})
print("frozen set 1 :", fset1)
fset2=frozenset({12,3,33,2132,232})

print("Intersection :",fset1.intersection(fset2))
print("fset1 Difference:",fset1.difference(fset2))
print("fset2 Difference:",fset2.difference(fset1))
print("Union of set:",fset1.union(fset2))
print(fset1.add(9))

