class Fibonacci(object):

    """Iterator that yields numbers in the Fibonacci sequence"""

    def __init__(self, num1, num2, length):
        self.num1 = num1
        self.num2 = num2
        self.length = length
        self.count = 1

    def __iter__(self):
        self.a = self.num1
        self.b = self.num2
        return self

    def __next__(self):
        fib = self.a
        if self.count > self.length:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return fib


class Program(object):

    @staticmethod
    def run():
        while 1:
            command = input("\nPlease enter seed 1: ")
            a = int(command)
            command = input("Please enter seed 2: ")
            b = int(command)
            command = input("Please enter length of sequence: ")
            length = int(command)

            fibonacci = Fibonacci(a, b, length)
            for number in fibonacci:
                print(number)


Program.run()

"""
In this project, I chose to programmatically generate my sequence of numbers. This method has the advantage
of being infinite, any length is supported, and any seed number can be inputted. The downside of this method is that 
it is rather slow, as the algorithm has to calculate each number in the sequence individually. There is an alternative 
to this method though, by pre-calculating much of the sequence in advance, the program becomes much faster and able
to process a larger number of numbers in a shorter amount of time. This method might involve a large database
of numbers. Of course, the disadvantage is that this database would be finite, and unable to process certain numbers
past a certain point. A combination of these methods might be an option, pre-calculating the numbers up to a certain
point, and then generating the rest.
"""
