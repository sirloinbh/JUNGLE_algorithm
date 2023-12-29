now = input()
start = input()

now_time = now.split(":")
start_time = start.split(":")
now_sec = int(now_time[0])*60*60 + int(now_time[1])*60 + int(now_time[2])
start_sec = int(start_time[0])*60*60 + int(start_time[1])*60 + int(start_time[2])

if now_sec <= start_sec :
    left_sec = start_sec - now_sec
else :
    left_sec = start_sec - now_sec +24*60*60
    
left_time = [left_sec//(60*60), (left_sec%(60*60))//60, left_sec%60]
left = []
for e in left_time :
    if e//10 == 0 :
        left.append("0"+str(e))
    else :
        left.append(str(e))
print(":".join(left))