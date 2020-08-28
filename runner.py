#!/usr/bin/env python

import commands
import sys
from datetime import date, timedelta

today = date.today()
today_f = today.strftime("%Y-%m-%d")
report = "Report Date: " + today_f
print(report)
yesterday = today - timedelta(days=1)
yesterday_f = yesterday.strftime("%Y-%m-%d")

if len(sys.argv) == 3:
    start = sys.argv[1]
    end = sys.argv[2]
else:
    start = yesterday_f
    end = today_f

records = "From: " + start + " To: " +  end 
print(records)
batcmd = "source  /home/stack/overcloudrc; openstack usage list --start " + start + " --end " + end +  " -f yaml"

result = commands.getoutput(batcmd)
for res in result.split("- CPU Hours"):
    res = res.strip()
    project = ""
    ram = ""
    for line in res.splitlines():
        line = line.strip()
        if line.startswith("Project:"):
            project = line
        elif line.startswith("RAM MB-Hours:"):
            ram = line
        if project and ram:
            ram_f = ram.split("RAM MB-Hours: ")[1]
            project_f = project.split("Project: ")[1]
            outp = project_f + ", " + ram_f
            print(outp)
            break
