import json
from datetime import date
from pathlib import Path
DATA_FILE = Path("sample_applications.json")
REPORT_FILE = Path("tracker_report.txt")
STATUSES = ["Applied", "Interview", "Selected", "Rejected"]
def load_applications():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r") as file:
        return json.load(file)
def save_applications(applications):
    with DATA_FILE.open("w") as file:
        json.dump(applications, file, indent=4)
def add_application(applications, company, role, status, application_date):
    if status not in STATUSES:
        print("Invalid status!")
        return
    application = {
        "company": company,
        "role": role,
        "status": status,
        "application_date": application_date
    }
    applications.append(application)
    save_applications(applications)
    print("Application added successfully!")
def search_by_status(applications, status):
    return [
        app for app in applications
        if app["status"].lower() == status.lower()
    ]
def search_by_company(applications, company):
    return [
        app for app in applications
        if company.lower() in app["company"].lower()
    ]
def update_status(applications, company, role, new_status):
    if new_status not in STATUSES:
        print("Invalid status!")
        return
    for app in applications:
        if (app["company"].lower() == company.lower()
                and app["role"].lower() == role.lower()):
            app["status"] = new_status
            save_applications(applications)
            print("Status updated successfully!")
            return
    print("Application not found!")
def generate_summary(applications):
    counts = {status: 0 for status in STATUSES}
    for app in applications:
        if app["status"] in counts:
            counts[app["status"]] += 1
    interviews = [
        app for app in applications
        if app["status"] == "Interview"
    ]
    return counts, interviews
def display_applications(applications):
    if not applications:
        print("No applications found.")
        return
    for i, app in enumerate(applications, start=1):
        print(
            f'{i}. {app["company"]} | {app["role"]} | '
            f'{app["status"]} | {app["application_date"]}'
        )
def save_report(applications):
    counts, interviews = generate_summary(applications)
    with REPORT_FILE.open("w") as file:
        file.write("PERSONAL JOB APPLICATION TRACKER\n")
        file.write("=" * 40 + "\n\n")
        file.write("ALL APPLICATIONS\n")
        file.write("-" * 40 + "\n")
        for i, app in enumerate(applications, start=1):
            file.write(
                f'{i}. {app["company"]} | {app["role"]} | '
                f'{app["status"]} | {app["application_date"]}\n'
            )
        file.write("\nAPPLICATION SUMMARY\n")
        file.write("-" * 40 + "\n")
        for status, count in counts.items():
            file.write(f"{status}: {count}\n")
        file.write("\nCURRENT INTERVIEWS\n")
        file.write("-" * 40 + "\n")
        if interviews:
            for app in interviews:
                file.write(
                    f'{app["company"]} - {app["role"]}\n'
                )
        else:
            file.write("No current interviews.\n")
    print("Report saved successfully!")
def main():
    applications = load_applications()
    while True:
        print("\n===== JOB APPLICATION TRACKER =====")
        print("1. View all applications")
        print("2. Add application")
        print("3. Search by status")
        print("4. Search by company")
        print("5. Update application status")
        print("6. View summary")
        print("7. Save report")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_applications(applications)
        elif choice == "2":
            company = input("Company: ")
            role = input("Role: ")
            status = input("Status: ").strip().title()
            application_date = input("Application date (YYYY-MM-DD): ")
            try:
                date.fromisoformat(application_date)
                add_application(
                    applications,
                    company,
                    role,
                    status,
                    application_date
                )
            except ValueError:
                print("Invalid date format!")
        elif choice == "3":
            status = input("Enter status: ")
            result = search_by_status(applications, status)
            display_applications(result)
        elif choice == "4":
            company = input("Enter company name: ")
            result = search_by_company(applications, company)
            display_applications(result)
        elif choice == "5":
            company = input("Company: ")
            role = input("Role: ")
            new_status = input("New status: ").strip().title()
            update_status(
                applications,
                company,
                role,
                new_status
            )
        elif choice == "6":
            counts, interviews = generate_summary(applications)
            print("\nAPPLICATION SUMMARY")
            for status, count in counts.items():
                print(f"{status}: {count}")
            print("\nCURRENT INTERVIEWS:")
            display_applications(interviews)
        elif choice == "7":
            save_report(applications)
        elif choice == "8":
            save_applications(applications)
            print("Thank you for using the tracker!")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()