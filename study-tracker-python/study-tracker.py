# ==========================
# Study Tracker CLI Application
# ==========================

# Tracks total study hours and identifies most studied subject

def get_input():
    sessions = []

    while True:
        subject = input("Subject: ").lower().strip()

        while True:
            try:
                hour = float(input("Hours: "))
                break
            except ValueError:
                print("Invalid Input")

        sessions.append([subject, hour])

        x = input("Do you want to continue? (yes/no): ").lower().strip()
        if x == 'no':
            break

    return sessions


sessions = get_input()

# Total Time Spent
total = sum(session[1] for session in sessions)
print("Total Study Time:", total)

# Most Studied Subject
subjects_hours = {}

for subject, hours in sessions:
    subjects_hours[subject] = subjects_hours.get(subject, 0) + hours

most_studied_subject = max(subjects_hours, key=subjects_hours.get)

print("Most Studied Subject:", most_studied_subject)