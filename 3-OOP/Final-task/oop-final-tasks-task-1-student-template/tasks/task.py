class Sun:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Sun, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def inst(cls):
        cls.__new__(cls)
