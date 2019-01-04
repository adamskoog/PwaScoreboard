class UpperCaseList(list):
    # list subclass that uses upper() when testing for 'in'
    def __contains__(self, other):
        return super(UpperCaseList, self).__contains__(other.upper())