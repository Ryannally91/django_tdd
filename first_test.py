import unittest
# Notice that we are now importing unittest
#From command line 'python -m unittst first_test.py

def sum_two(a,b):
    return a + b
    
def scale_list(l,y):
    if type(y) != int:
        return []
    for i in range(len(l)):
        l[i] *= y
    return l
# Below this line we are creating our first class that will hold all of our tests
class MainTest(unittest.TestCase):
    # We will create individual tests as methods within this class, and the system knows to run any method whose name begins with 'test'
    def test_hello(self):
        print("Hello from the tests")

    def test_sum_two(self):
        returned_value = sum_two(5,7)
        # Here we call on self, and utilizing the methods we inherited from TestCase we can call on the assertEqual method, providing our inputs
        self.assertEqual(returned_value, 12)
        self.assertEqual(sum_two(-5,5), 0) #better way of writting test, to avoid having many variables 


#         1. `import unittest` and create a class that inherits from `unittest.TestCase`
# 2. Define a method beginning with `test` so it will get run by TestCase
# 3. Determine which assert method is most appropriate for the function we are testing
# 4. Create a few different asserts in our test method so we can test different inputs in one go
# 5. Run the tests with `python -m unittest first_test.py` and see the result

    def test_scale_list(self):
        self.assertEqual(scale_list([1,2,3,4],5), [5,10,15,20])
        self.assertEqual(scale_list([-1,2,-3,4],-5), [5,-10,15,-20])
        self.assertIsNot(scale_list([0],0), []) #this one is tricky

    