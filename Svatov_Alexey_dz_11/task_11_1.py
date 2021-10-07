class Date(object):
    def __init__(self, new_date):
        self.new_date = new_date

    def __str__(self):
        return '.'.join(self.new_date)

    @classmethod
    def extractor(cls, input_date):
        new_date = tuple(input_date.split('-'))
        date1 = cls(new_date)
        return date1

    @staticmethod
    def validator(input_date):
        day, month, year = map(int, input_date.split('.'))
        return day <= 31 and month <= 12 and year <= 2050


date = Date.extractor('02-10-1991')
print(Date.validator(str(date)))
print(date)
