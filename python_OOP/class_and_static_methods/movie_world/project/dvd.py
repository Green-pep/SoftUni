import calendar


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        new_date = date.split(".")
        creation_year, creation_month = int(new_date[2]), int(new_date[1])
        creation_month = calendar.month_name[creation_month]
        return cls(name, id, creation_year, creation_month, age_restriction)

    def __repr__(self):
        if self.is_rented:
            dvd_is_rented = "rented"
        else:
            dvd_is_rented = "not rented"
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction "
                f"{self.age_restriction}. Status: {dvd_is_rented}")
