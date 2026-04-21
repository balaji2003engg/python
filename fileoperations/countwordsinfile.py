import re
#total number  of words
with open(r"D:\git\python\Dbconnect\dbqueries.txt") as f:
  data =f.read()
  print(len(data.split()))
#Count Specific Word ("ERROR")
with open(r"D:\git\python\app.log.txt")  as a:
   e= a.read()
   print("Error count", e.count("ERROR"))
   
# print line containing error
with open(r"D:\git\python\app.log.txt")  as l:
    
    for lines in l:
        if "ERROR" in lines:
            print(lines.strip())
            
#  identify ip address
with open(r"D:\git\python\app.log.txt") as ip:
    ipr= ip.read()
    p=re.findall("\d+\.\d+\.\d+\.\d+",ipr)
    print(p)
    re.findall()
           