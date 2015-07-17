"""gludb.config

Provide gludb configuration. This consists mainly of a mapping from Storable
classes to a database configuration. It also includes a default mapping for
classes not specifically mapped to a database
"""

# TODO: really force config to be process-wide? But we're trying to make things
#       super simple (no DAO's lying around) and no database-specific coupling
#       where they defined their classes


class Database(object):
    def __init__(self, db_driver, **kwrds):
        # TODO: need to get a driver (and pass along the kwrds) - then
        #       we can rewrite our methods with types.MethodType
        pass

    def ensure_table(self):
        print("Table Ensured")  # TODO: Remove and replace with error thrown

    def find_one(self, id):
        return None  # TODO: Remove and replace with error thrown

    def find_all(self):
        return []  # TODO: Remove and replace with error thrown

    def save(self, obj):
        pass  # TODO: Remove and replace with error thrown


class _DatabaseMapping(object):
    def __init__(self):
        self.clear_mappings()

    def add_mapping(self, cls, db):
        self.mapping[cls] = db

    def get_mapping(self, cls):
        db = self.mapping.get(cls, self.default_database)
        if db is None:
            raise ValueError("There is no database mapping for %s" % repr(cls))
        return db

    def clear_mappings(self):
        self.default_database = None
        self.mapping = {}

_database_mapping = _DatabaseMapping()


def default_database(db):
    """Set the default database configuration used for classes without a
    specific mapping"""
    _database_mapping.default_database = db


def class_database(cls, db):
    """Map a class (for which we assume issubclass(cls, Storable)==True) to
    a database configuration"""
    _database_mapping.add_mapping(cls, db)


def clear_database_config():
    """Reset all mappings to default state. Note that any in-memory databases
    will be lost"""
    _database_mapping.clear_mappings()


def get_mapping(cls):
    """Return a database config object for the given class"""
    return _database_mapping.get_mapping(cls)
