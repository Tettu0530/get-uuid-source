import subprocess

command = "wmic csproduct get uuid"

res = subprocess.check_output(command).decode("utf-8")

res = res.replace("UUID", "")
hwid = res.strip()
print(hwid)

with open("hwid.txt", "w", encoding = "utf-8") as f:
    f.write(hwid)