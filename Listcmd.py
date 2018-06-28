samp_list = list()
act_list = list()
n = int(input())

while n != 0:
 command = input()
 samp_list.append(command)
 n = n-1
for cmd in samp_list:
    if cmd == 'print':
        print (act_list)
    else:
        chk = cmd.split()
        cmd = chk[0]
        parm = chk[1:]
        cmd+="("+ ",".join(parm) +")"
        eval("act_list."+cmd)
