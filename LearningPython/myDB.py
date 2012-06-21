class MyDB:
    def __init__(self):
        self._id2name_map = {}
        self._name2id_map = {}

    def add(self, identifier, name):
        self._name2id_map[name] = identifier
        self._id2name_map[identifier] = name

    def by_name(self, name):
        return self._name2id_map[name]
    #some comment
