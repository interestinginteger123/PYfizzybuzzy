class LambdaInteractor(object):
    def __init__(self, dictthing):
        self._lambdadict = dictthing
        self._printout = ''
    
    def fizzbuzz(self, n, p):
        x= lambda a: a if n%p==0 else ''
        return x
    
    def output(self, n):
        for key, value in self._lambdadict.items():
            printfizzbuzz = self.fizzbuzz(n, value)
            self._printout +=printfizzbuzz(a=key)
        return self._printout

if __name__ == "__main__":

    dictthing={'Fizz':3,'Buzz':5}
    FIZZBUZZ = LambdaInteractor(dictthing)
    print(FIZZBUZZ.output(5))

