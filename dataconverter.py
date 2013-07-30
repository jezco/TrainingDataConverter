import sys
import xml.etree.ElementTree as ET

class Exercise:
    hello = ""
    def __init__(self, helloStr):
        self.hello = helloStr
        
    def sayHi(self):
        print self.hello
        
def main():
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    
    if len(sys.argv) > 1:

    
main()