from Population import population
class Algorithm:
    def __init__(self,size,population):
        self.size=size
        self.popl=population
    def run(self):
        """
        evaluate and select the population until a solution is found
        :return: solution or best individual, list of best individuals during evolution,number of iterations
        """
        fit=[]
        iters=0
        while self.popl.evaluate()==None:
            fit.append(self.popl.selection(1.3))
            iters+=1
        return (self.popl.evaluate(),fit,iters)
