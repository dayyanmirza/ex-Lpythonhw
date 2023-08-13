# Override Explicitly
class Parent(object):

    def override(self):
        print("PARENT override()")


class Child(Parent):

    def override(self):
        print("CHILD override()") # Child overrides the function by defining its own version.


dad = Parent()
son = Child()

dad.override()
son.override()
