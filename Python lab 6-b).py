def test(x):
    result =  map(sum, x)
    return list(result)

nums = [(1,2), (2,3), (3,4)]
print("\nSum of all the elements : " , test(nums))

nums = [(1,2,6), (2,3,-6), (3,4), (2,2,2,2)]
print("\nSum of all the elements : ", test(nums))
