def attendance_report(names, attendance):
    eligible_names = []
    
    for name in names:
        count = attendance.get(name,0)
        print(f"{name}: {count}")
        
        if count >=3:
            eligible_names.append(name)
            
    return eligible_names
    
names = ["Abha","Bhavesh","Chetan","Dharmesh"]
attendance_data = {
    "Abha": 5,
    "Bhavesh": 1,
    "Chetan": 3,
}

result = attendance_report(names,attendance_data)

print("Eligible participants:", result)
    