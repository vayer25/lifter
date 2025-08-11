import csv

def export_to_csv(students, filename="students.csv"):
    if not students:
        print("⚠️ No data to export.")
        return
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=students[0].keys())
            writer.writeheader()
            writer.writerows(students)
        print(f"✅ Data exported successfully to '{filename}'.")
    except Exception as e:
        print(f"👎 Error exporting data: {e}")

def import_from_csv(filename="students.csv"):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            students = []
            for row in reader:
                students.append({
                    "name": row["name"],
                    "section": row["section"],
                    "spanish": int(row["spanish"]),
                    "english": int(row["english"]),
                    "social": int(row["social"]),
                    "science": int(row["science"]),
                    "average": float(row["average"])
                })
            print(f"✅ Data imported successfully from '{filename}'.")
            return students
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"❌ Error importing data: {e}")
        return []
import csv

def export_to_csv(students, filename="students.csv"):
    if not students:
        print("⚠️ No data to export.")
        return
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=students[0].keys())
            writer.writeheader()
            writer.writerows(students)
        print(f"✅ Data exported successfully to '{filename}'.")
    except Exception as e:
        print(f"👎 Error exporting data: {e}")

def import_from_csv(filename="students.csv"):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            students = []
            for row in reader:
                students.append({
                    "name": row["name"],
                    "section": row["section"],
                    "spanish": int(row["spanish"]),
                    "english": int(row["english"]),
                    "social": int(row["social"]),
                    "science": int(row["science"]),
                    "average": float(row["average"])
                })
            print(f"✅ Data imported successfully from '{filename}'.")
            return students
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"❌ Error importing data: {e}")
        return []
