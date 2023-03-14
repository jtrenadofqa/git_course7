import datetime

class PhDStudent:

    def __init__(self, name, family_name, year):
        self._name=name
        self._family_name=family_name
        self._access_year=""
        self.set_access_year(year)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name=value

    @property
    def family_name(self):
        return self._family_name

    @family_name.setter
    def family_name(self, value):
        self._family_name=value

    @property
    def access_year(self):
        return self._access_year

    def set_access_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise SystemExit( "Student access year can not be set to be after current year" )
        elif current_year-value>6:
            print("Student should be in alumni database, access year set to {}".format(value))
        else:
            self._access_year=value

