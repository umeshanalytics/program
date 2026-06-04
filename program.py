import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# - - - - MODULE 1: Student Registration & Grade Evaluation - - - -
def student_registration():
print('\n=== MODULE 1: Student Registration & Grade Evaluation ===')
student_name = input('Enter student name: ')
score = float(input('Enter exam score (0- 100): '))
if score > = 90 and score < = 100:
grade = 'A'; remark = 'Excellent'
elif score > = 75:
grade = 'B'; remark = 'Very Good'
elif score > = 60:
grade = 'C'; remark = 'Good'
elif score > = 40:
grade = 'D'; remark = 'Average'
else:
grade = 'F'; remark = 'Needs Improvement'
print('\n- - - Student Report - - - ')
print('Name :', student_name)
print('Score :', score)
print('Grade :', grade)
print('Remark:', remark)
# - - - - MODULE 2: Course Enrollment Management - - - -
def course_enrollment():
print('\n=== MODULE 2: Course Enrollment Management ===')
courses = []
max_courses = 5
while True:
if len(courses) > = max_courses:
print('Maximum course limit reached!'); break
course_name = input('Enter course name (or done to finish): ')
if course_name.lower() == 'done': break
credits = input('Enter credit value: ')
if not credits.isdigit():
print('Invalid credit! Skipping...'); continue
credits = int(credits)
if credits < = 0:
print('Credit must be positive! Skipping...'); continue
courses.append((course_name, credits))
print(f'Course {course_name} with {credits} credits added.')
print('\n- - - Enrollment Report - - - ')
for course, credit in courses:
print(f'Course: {course}, Credits: {credit}')
print('Total courses enrolled:', len(courses))
# - - - - MODULE 3: Student Record Data Management - - - -
def student_records():
print('\n=== MODULE 3: Student Record Data Management ===')
students = []
students.append({'name': 'Priya', 'age': 20, 'grades': [85, 90, 78]})
students.append({'name': 'Rahul', 'age': 21, 'grades': [72, 88, 91]})
students.append({'name': 'Anita', 'age': 19, 'grades': [95, 89, 92]})
print('=== Student Records ===')
for student in students:
print('Name:', student['name'])
print('Age:', student['age'])
print('Grades:', student['grades'])
print('- ' * 23)
event_A = {'Priya', 'Rahul', 'Anita', 'Kiran'}
event_B = {'Rahul', 'Anita', 'Sneha'}
print('\n=== Event Participation Analysis ===')
print('Common Participants:', event_A & event_B)
print('All Participants:', event_A | event_B)
print('Only Event A Participants:', event_A - event_B)
# - - - - MODULE 4: Sorting and Searching - - - -
def search_sort_students():
print('\n=== MODULE 4: Sorting and Searching ===')
student_ids = [105, 102, 110, 108, 101, 115]
print('Original IDs:', student_ids)
ids_bubble = student_ids[:]
n = len(ids_bubble)
for i in range(n):
for j in range(0, n- i- 1):
if ids_bubble[ j] > ids_bubble[ j+1]:
    ids_bubble[ j], ids_bubble[ j+1] = ids_bubble[ j+1], ids_bubble[ j]
print('Sorted IDs (Bubble Sort):', ids_bubble)
ids_sel = student_ids[:]
for i in range(len(ids_sel)):
min_idx = i
for j in range(i+1, len(ids_sel)):
if ids_sel[ j] < ids_sel[min_idx]: min_idx = j
ids_sel[i], ids_sel[min_idx] = ids_sel[min_idx], ids_sel[i]
print('Sorted IDs (Selection Sort):', ids_sel)
target = int(input('Enter Student ID to search: '))
found = - 1
for i in range(len(ids_bubble)):
if ids_bubble[i] == target: found = i; break
print('Linear Search: ID', target, 'found at index', found if found != - 1else 'not found')
low, high, found = 0, len(ids_bubble)- 1, - 1
while low < = high:
mid = (low+high)//2
if ids_bubble[mid] == target: found = mid; break
elif ids_bubble[mid] < target: low = mid+1
else: high = mid- 1
print('Binary Search: ID', target, 'found at index', found if found != - 1else 'not found')
# - - - - MODULE 5: Fee Calculation - - - -
def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
return tuition_fee + hostel_fee + transportation_fee
def fee_calculation():
print('\n=== MODULE 5: Fee Calculation ===')
tuition = float(input('Enter Tuition Fee: '))
h = input('Enter Hostel Fee (Enter to skip): ')
t = input('Enter Transportation Fee (Enter to skip): ')
hostel = float(h) if h.strip() else 0
transport = float(t) if t.strip() else 0
total = calculate_fee(tuition, hostel_fee=hostel, transportation_fee=transport)
print(f'Tuition: Rs.{tuition} Hostel: Rs.{hostel} Transport: Rs.{transport}')
print(f'Total Fee: Rs.{total}')
# - - - - MODULE 6: File Handling - - - -
def file_management():
print('\n=== MODULE 6: File Handling ===')
with open('student_records.txt', 'w') as file:
file.write('ID,Name,Marks\n')
file.write('101,Arjun,85\n')
file.write('102,Meera,92\n')
file.write('103,Ravi,76\n')
file.write('104,Anita,89\n')
print('Records written successfully.')
with open('student_records.txt', 'r') as file:
records = file.readlines()
print('\nReading stored records:')
for record in records: print(record.strip())
total, marks_sum, highest, top = 0, 0, - 1, ''
for record in records[1:]:
parts = record.strip().split(',')
marks = int(parts[2])
total += 1; marks_sum += marks
if marks > highest: highest = marks; top = parts[1]
print(f'\nAverage Marks: {marks_sum/total} Top Student: {top} with {highest} marks')
# - - - - MODULE 7: Directory Scanner - - - -
class MissingFileOrFolderError(Exception): pass
def scan_directory(path):
try:
if not os.path.exists(path):
raise FileNotFoundError(f'Invalid path: {path}')
for root, dirs, files in os.walk(path):
level = root.replace(path, '').count(os.sep)
indent = ' ' * 4 * level
print(f'{indent}{os.path.basename(root)}/')
for f in files: print(f'{indent} {f}')
if not files and not dirs:
raise MissingFileOrFolderError(f'Empty folder: {root}')
except FileNotFoundError as e: print(f'Error: {e}')
except MissingFileOrFolderError as e: print(f'Custom Error: {e}')
except Exception as e: print(f'Unexpected Error: {e}')
def directory_scanner():
print('\n=== MODULE 7: Directory Scanner ===')
path = input('Enter directory path to scan: ')
scan_directory(path)
# - - - - MODULE 8: Performance Analytics - - - -
def performance_analytics():
print('\n=== MODULE 8: Performance Analytics ===')
csv_file = 'student_performance.csv'
if not os.path.exists(csv_file):
with open(csv_file, 'w') as f:
f.write('Name,Math,Science,English\n')
f.write('Priya,88,92,85\n')
f.write('Rahul,75,80,70\n')
f.write('Anita,95,89,91\n')
f.write('Kiran,60,72,68\n')
print(f'Sample CSV created.')
try:
df = pd.read_csv(csv_file)
print('\n- - - Raw Data - - - '); print(df.to_string(index=False))
print('\n- - - Statistical Summary - - - '); print(df.describe().round(2))
scores = df[['Math','Science','English']].to_numpy()
print('Mean:', np.mean(scores, axis=0))
print('Median:', np.median(scores, axis=0))
print('Std Dev:', np.std(scores, axis=0).round(2))
print('Top Math:', df.loc[df['Math'].idxmax(), 'Name'])
print('Top Science:', df.loc[df['Science'].idxmax(), 'Name'])
print('Top English:', df.loc[df['English'].idxmax(), 'Name'])
subjects = ['Math', 'Science', 'English']
plt.bar(subjects, np.mean(scores, axis=0), color=['blue','green','orange'])
plt.title('Average Scores per Subject')
plt.xlabel('Subjects'); plt.ylabel('Average Score')
plt.tight_layout(); plt.savefig('avg_scores.png'); plt.show()
df.plot(x='Name', y=['Math','Science','English'], kind='bar', figsize=(10,6))
plt.title('Student Performance Comparison')
plt.tight_layout(); plt.savefig('student_performance.png'); plt.show()
except Exception as e: print(f'Error: {e}')
# - - - - MAIN DASHBOARD - - - -
def main_dashboard():
print('*' * 52)
print('* SMART CAMPUS INFORMATION SYSTEM - DASHBOARD *')
print('* Dayananda Sagar College of Engineering *')
print('*' * 52)
menu = {
'1': ('Student Registration & Grade Evaluation', student_registration),
'2': ('Course Enrollment Management', course_enrollment),
'3': ('Student Record Data Management', student_records),
'4': ('Search & Sort Student Data', search_sort_students),
'5': ('Fee Calculation', fee_calculation),
'6': ('File Management (Academic Records)', file_management),
'7': ('Directory Scanner', directory_scanner),
'8': ('Performance Analytics', performance_analytics),
'9': ('Exit', None),
}
while True:
print('\n- - - Main Menu - - - ')
for key, (label, _) in menu.items():
print(f' {key}. {label}')
choice = input('\nEnter your choice (1- 9): ').strip()
if choice == '9':
print('Goodbye!'); break
elif choice in menu:
_, func = menu[choice]
func()
else:
print('Invalid choice! Enter 1- 9.')
if __name__ == '__main__':
main_dashboard()