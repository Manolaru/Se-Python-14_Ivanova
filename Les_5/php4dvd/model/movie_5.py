class Movie5(object):

    def __init__(self, name="", year="", duration=""):
        self.name = name
        self.year = year
        self.duration = duration

    @classmethod
    def Gatsby(cls):
        return cls(name="Gatsby", year="2000", duration="120")

    @classmethod
    def Kabaret(cls):
        return cls(name="Kabaret", year="1980", duration="90")

    @classmethod
    def Batman(cls):
        return cls(name="Batman", year="1993", duration="100")

    @classmethod
    def Mask(cls):
        return cls(name="Mask", year="2002", duration="60")

    @classmethod
    def Titanic(cls):
        return cls(name="Titanic", year="1999", duration="220")
