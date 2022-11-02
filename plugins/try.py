f = open("SQL_injection_payloads.txt", "r")
for line in f:
    line = line.rstrip()
    print(line)