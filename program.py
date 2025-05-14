import os
from models import ParkReport, Volunteer

class ParkCleanlinessProgram:
    def __init__(self, report_file='reports.txt', volunteer_file='volunteers.txt'):
        self.report_file = report_file
        self.volunteer_file = volunteer_file
        self.reports = []
        self.volunteers = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.report_file):
            with open(self.report_file, 'r') as f:
                for line in f:
                    report = ParkReport.from_line(line)
                    if report:
                        self.reports.append(report)

        if os.path.exists(self.volunteer_file):
            with open(self.volunteer_file, 'r') as f:
                for line in f:
                    volunteer = Volunteer.from_line(line)
                    if volunteer:
                        self.volunteers.append(volunteer)

    def save_reports(self):
        with open(self.report_file, 'w') as f:
            for report in self.reports:
                f.write(report.to_line() + '\n')

    def save_volunteers(self):
        with open(self.volunteer_file, 'w') as f:
            for volunteer in self.volunteers:
                f.write(volunteer.to_line() + '\n')

    def submit_report(self, resident_name, description):
        report = ParkReport(resident_name, description)
        self.reports.append(report)
        self.save_reports()
        print(f"✅ Thank you, {resident_name}, for reporting the issue.")

    def add_volunteer(self, resident_name, contact, available_dates=None):
        volunteer = Volunteer(resident_name, contact, available_dates)
        self.volunteers.append(volunteer)
        self.save_volunteers()
        print(f"✅ Thank you, {resident_name}, for volunteering!")

    def list_reports(self):
        if not self.reports:
            print("🚫 No cleanliness reports yet.")
        else:
            print("📋 Current cleanliness reports:")
            for idx, report in enumerate(self.reports, start=1):
                print(f" {idx}. {report}")

    def list_volunteers(self):
        if not self.volunteers:
            print("🚫 No volunteers registered yet.")
        else:
            print("🙋‍♂️ Registered volunteers:")
            for idx, volunteer in enumerate(self.volunteers, start=1):
                print(f" {idx}. {volunteer}")

    def summary(self):
        print("=== 🧹 Park Cleanliness Program Summary ===")
        print(f"📝 Total reports: {len(self.reports)}")
        print(f"🙋‍♀️ Total volunteers: {len(self.volunteers)}")
        print("---------------------------------------")
