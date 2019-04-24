class ODict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._order = []

    def __setitem__(self, key, value):
        self._order.append(key)
        super().__setitem__(key, value)

    def __delitem__(self, key):
        self._order.remove(key)
        super().__delitem__(key)

    def __iter__(self):
        for item in self._order:
            yield item

    def items(self):
        for item in self._order:
            yield item, self[item]

    def __repr__(self):
        return '{' + ', '.join(['%s: %s' % (repr(key), repr(value))
                                for key, value in self.items()]) + '}'
