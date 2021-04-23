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

def left():

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

    elif ir==0x02:#load -m(x)

        ac=-mm[mar]

    elif ir==0x03:#load |m(x)|

        ac=abs(mm[mar])

    elif ir==0x04:#load -|m(x)|

        ac=-abs(mm[mar])

    elif ir==0x0D:#unconditional jump. take left instruction

        pc=mm[mar]

    elif ir==0x0F:#conditional jump

        if ac>=0:
            pc=mm[mar]

        


    elif ir==0x05:#add m(x)

        ac+=mm[mar]

    elif ir==0x07:

        ac+=abs(mm[mar])

def right():

    global ac,mq,mbr,mar,ibr,ir,pc

    #right insruction

    # temp=ibr//(16**5)
    ir=ibr//(16**3)
    mar=ibr%(16**3)

    # mbr = mm[mar]

    if ir==0x0A:
        ac=mq

    elif ir==0x09:
        mq=mm[mar]

    elif ir==0x21:#STOR
        mm[mar]=ac

    elif ir==0x01:#LOAD

        ac=mm[mar]

    elif ir==0x02:#load -m(x)

        ac=-mm[mar]

    elif ir==0x03:#load |m(x)|

        ac=abs(mm[mar])

    elif ir==0x04:#load -|m(x)|

        ac=-abs(mm[mar])

    elif ir==0x0D:#unconditional jump. take left instruction

        pc=mm[mar]

    elif ir==0x0F:#conditional jump

        if ac>=0:
            pc=mm[mar]

        


    elif ir==0x05:#add m(x)

        ac+=mm[mar]

    elif ir==0x07:

        ac+=abs(mm[mar])

    






    

    


##################testing###################

mm[0]=0x0110005101

mm[0x100]=25
mm[0x101]=25


fetch()
left()
print(mar,ir,ibr,ac)
right()
print(mar,ir,ibr,ac)







