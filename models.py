import datetime

class ParkReport:
    def __init__(self, resident_name, description, date=None):
        self.resident_name = resident_name
        self.description = description
        self.date = date if date else datetime.date.today()

    def __str__(self):
        return f"[{self.date}] {self.resident_name} reported: {self.description}"

    def to_line(self):
        return f"{self.resident_name}|{self.description}|{self.date}"

    @staticmethod
    def from_line(line):
        try:
            parts = line.strip().split('|')
            name = parts[0]
            desc = parts[1]
            date = datetime.datetime.strptime(parts[2], "%Y-%m-%d").date()
            return ParkReport(name, desc, date)
        except (IndexError, ValueError):
            return None


class Volunteer:
    def __init__(self, resident_name, contact, available_dates=None):
        self.resident_name = resident_name
        self.contact = contact
        self.available_dates = available_dates if available_dates else []

    def add_availability(self, date):
        if date not in self.available_dates:
            self.available_dates.append(date)

    def __str__(self):
        dates = ', '.join(str(d) for d in self.available_dates) if self.available_dates else 'No availability set'
        return f"{self.resident_name} (Contact: {self.contact}) | Available: {dates}"

    def to_line(self):
        dates_str = ','.join(str(d) for d in self.available_dates)
        return f"{self.resident_name}|{self.contact}|{dates_str}"

    @staticmethod
    def from_line(line):
        try:
            parts = line.strip().split('|')
            name = parts[0]
            contact = parts[1]
            dates = []
            if len(parts) > 2 and parts[2]:
                for d in parts[2].split(','):
                    date_obj = datetime.datetime.strptime(d.strip(), "%Y-%m-%d").date()
                    dates.append(date_obj)
            return Volunteer(name, contact, dates)
        except (IndexError, ValueError):
            return None
