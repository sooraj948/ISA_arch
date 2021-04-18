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

def execute():

    global ac,mq,mbr,mar,ibr,ir,pc

    #left insruction

    # mbr = mm[mar]

    if ir==0x0A:
        ac=mq

    elif ir==0x09:
        mq=mm[mar]

    elif ir==0x21:#STOR
        mm[mar]=ac

    elif ir==0x01:#LOAD

        ac=mm[mar]

    

    




mm[0]=0x0123456789

fetch()

# print(mar,ir,ibr)






