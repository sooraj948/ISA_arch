#registers(global)

ac=0#accumalator
mq=0
mbr=0#mem buffer register
mar=0# mem address reg
ibr=0 #mem buffer reg
ir=0 # instruction reg
mm=[0 for i in range(1000)]# instructions and data in hex. 
pc=0


def fetch():
    global ac,mq,mbr,mar,ibr,ir,pc

    mar=pc
    mbr=mm[mar]

    ibr=mbr%(16**5)
    temp=mbr//(16**5)
    ir=temp//(16**3)
    mar=temp%(16**3)


mm[0]=0x0123456789

fetch()

# print(mar,ir,ibr)






