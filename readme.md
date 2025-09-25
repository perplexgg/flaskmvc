# CLI Command Reference – Student Incentive System

This app is a simple CLI system for recording and managing student community service hours, built with the Flask MVC template.  
Commands are grouped by area. Run them with `flask <command>`.

---

## App-Level Commands

### `flask init-data`
- **Args:** none  
- **Role:** anyone  
- **Does:** Seeds the system with sample students and staff for quick testing.

### `flask leaderboard`
- **Args:** none  
- **Role:** anyone  
- **Does:** Displays a ranked list of students by total hours.

---

## Student Commands

### `flask create-student`
- **Args:** prompts for ID, name, and username.  
- **Does:** Creates a new student user.  

### `flask accolades`
- **Args:** prompts for student username.  
- **Does:** Shows a student’s accolades when they reach 10, 25, or 50 hours.  

---

## Staff Commands

### `flask create-staff`
- **Args:** prompts for ID, name, username, and department.  
- **Does:** Creates a new staff member.  

### `flask log-hours`
- **Args:** prompts for student username, hours, activity, and date.  
- **Does:** Logs service hours for a student (status = pending).  

### `flask approve-hours`
- **Args:** shows a list of pending entries, prompts to select one.  
- **Does:** Approves the selected entry, adds hours to the student’s total, and checks for accolades.  

---

## Example Flow
```bash
flask init-data
flask create-student
flask create-staff
flask log-hours
flask approve-hours
flask leaderboard
flask accolades
