from datetime import datetime

datetime_str1 = "2025-01-01 "+input()
datetime_str2 = "2025-01-02 "+input()

delta = datetime.strptime(datetime_str2, "%Y-%m-%d %H:%M:%S") - datetime.strptime(datetime_str1, "%Y-%m-%d %H:%M:%S")

total_seconds = int(delta.total_seconds())

hours = total_seconds // 3600%24
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")
