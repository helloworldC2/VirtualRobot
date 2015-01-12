'''
Paths can be separated by forward slashes: `"/name/first"`, or with dot
notation: `"name.first"`. If a path starts with a `'/'`, Orchestrate will be
interpret it as a [JSON Pointer](http://tools.ietf.org/html/rfc6901), otherwise
Orchestrate interprets the path as dot notation.
'''
class Patch:
    def __init__(self):
        self.operations = []

    '''
    Depending on the specified path, creates a field with that value, replaces
    an existing field with the specified value, or adds the value to an array.
    '''
    def add(self, path, value):
        return self.__operation('add', path, value)

    '''
    Removes the field at a specified path
    '''
    def remove(self, path):
        return self.__operation('remove', path)

    '''
    Replaces an existing value with the given value at the specified path.
    '''
    def replace(self, path, value):
        return self.__operation('replace', path, value)

    '''
    Moves a value from one path to another, removing the original path.
    '''
    def move(self, old_path, new_path):
        return self.__operation('move', new_path, from_path=old_path)

    '''
    Copies the value at one path to another.
    '''
    def copy(self, original, copy):
        return self.__operation('copy', copy, from_path=original)

    '''
    Tests equality of the value at a particular path to a specified value, the
    entire request fails if the test fails.
    '''
    def test(self, path, value):
        return self.__operation('test', path, value)

    '''
    Increments the numeric value at a specified field by the given numeric
    value, decrements if given numeric value is negative. Default is `1`
    '''
    def increment(self, path, value=1):
        return self.__operation('inc', path, value)

    '''
    Decrements the numeric value at a specified field by given a numeric value.
    This method is sugar. It wraps the `increment` method and multiplies the
    value by -1. Passing in a negative value will increment the field. The
    default is `-1`
    '''
    def decrement(self, path, value=1):
        self.increment(path, value*-1)
        return self

    def __operation(self, op, path, value=None, from_path=None):
        op = {
            'op': op,
            'path': path
        }
        if value != None:
            op['value'] = value
        if from_path:
            op['from'] = from_path

        self.operations.append(op)
        return self
