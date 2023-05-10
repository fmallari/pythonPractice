"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    """Create new generator at start"""

def __init__(self, start=0):
    self.start = self.next = start

    """Show representation"""

def __repr__(self):
    return f"<SerialGenerator start={self.start} next={self.next}>"

def generate(self):
    """Return next sequential serial"""
    self.next +=1
    return self.next - 1

def reset(self):
    """Reset number to original start"""
    self.next = self.start
