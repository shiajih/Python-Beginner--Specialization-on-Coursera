# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pos = line.find('0')
    total = total + float(line[pos:])
    
print("Average spam confidence:", total / count)
