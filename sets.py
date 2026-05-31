setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)
# Union
print("\nUnion of two sets:")
setz = setx.union(sety)

# Difference (elements in setx but not in sety)
print("\nDifference of setx - sety:")
setz = setx.difference(sety)
print(setz)

#Symmentric Difference
print("\nSymmetric Differnce of two sets:")
setz = setx.symmetric_difference(sety)
print(setz)