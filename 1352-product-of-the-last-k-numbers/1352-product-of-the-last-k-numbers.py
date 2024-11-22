class ProductOfNumbers:

    def __init__(self):
        self.list_of_prod = [1]  

    def add(self, num: int) -> None:
        if num == 0:
            self.list_of_prod = [1] 
        else:
            self.list_of_prod.append(self.list_of_prod[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.list_of_prod):  
            return 0
        return self.list_of_prod[-1] // self.list_of_prod[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)