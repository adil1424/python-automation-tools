# backup_report.py
# Backup verification report generator

import os
from datetime import datetime

backup_dir = "/backup/data/"
report_file = f"backup_report_{datetime.today().date()}.txt"

files = os.listdir(backup_dir)

with open(report_file, "w") as report:
    report.write("Backup Verification Report\n")
    report.write("--------------------------\n")

    for f in files:
        full_path = os.path.join(backup_dir, f)
        size = os.path.getsize(full_path)

        report.write(f"{f} - {size} bytes\n")

print("Backup report created:", report_file)
