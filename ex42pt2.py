class A(object):
    def __init__(self):
        print("in here")
    # cat has-a name    
    def cat(self, name):
        print ("my cat ", name)

B = A()
print(B.cat((A(), "Tom")))
    
# https://softwareengineering.stackexchange.com/questions/245929/using-class-like-an-object-in-python    