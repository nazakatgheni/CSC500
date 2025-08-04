# Ask for current time and wait time
current_time = int(input("What is the current time (0-23)? "))
hours_to_wait = int(input("How many hours to wait for the alarm? "))

# Calculate alarm time
alarm_time = (current_time + hours_to_wait) % 24

# Output the result
print(f"The alarm will go off at {alarm_time}:00.")
