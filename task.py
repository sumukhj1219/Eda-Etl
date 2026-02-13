from datetime import datetime

students = {}

def addStudent(student_id, name):
  if student_id in students:
    print("Student already exists")
  students[student_id] = {
      "name": name,
      "attendance": []
  }
  print("Student added successfully! \n")

def markAttendance(student_id, date):
  if student_id not in students:
    print("Student does not exist")
    return
  
  today=datetime.now().strftime("%Y-%m-%d")
  record=(today, "Present")
  students[student_id]["attendance"].append(record)
  print("Attendance Marked\n")

def viewStudent(student_id):
  if student_id not in students:
    print("Student does not exist")
    return
  student = students[student_id]
  print(f"\nName: {student['name']}")
  print("Attendance Records")

  for record in student["attendance"]:
    print(f"Date: {record[0]} | Status: {record[1]}")
    
def viewAll():
  print("All Students")
  for sid, data in students.items():
    print(f"ID: {sid} | Name: {data['name']}")

def main():
  while True:
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Student")
    print("4. View All Students")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
          student_id = input("Enter student id")
          name = input("Enter student name")
          addStudent(student_id, name)
    elif choice == "2":
          markAttendance()
    elif choice == "3":
          viewStudent()
    elif choice == "4":
          viewAll()
    elif choice == "5":
          break
    else:
          print("Invalid choice!\n")

if __name__ == "__main__":
  main()
