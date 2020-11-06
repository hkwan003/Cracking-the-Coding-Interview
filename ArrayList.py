import ctypes

class OurOwnList(object):
    def __init__(self):
        #count actual elements (default is 0)
        self.n = 0

        #default capacity
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        #return number of elements sorted in array
        return self.n

    def __getitem__(self, k):
        #returns items at index k
        if not 0 <= k < self.n:
            return IndexError('k is out of bounds!')

        return self.A[k]

    def append(self, element):
        #add element to end of array
        if self.n == self.capacity:
            self._resize(2 * self.capacity)     #double capacity once overflow

        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_cap): #underscore in front of variable means private variable or function
        #resize internal array to capacity new_cap
        B = self.make_array(new_cap) #new bigger array

        for k in range(self.n): #reference all existing values
            B[k] = self.A[k]
        self.A = B #call A the fresh Array
        self.capacity = new_cap #reset the capacity
    def make_array(self, new_cap):
        #returns a new array with new_cap capacity
        return (new_cap * ctypes.py_object)()