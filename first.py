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

        pc=mar
        return 1

    elif ir==0x0F:#conditional jump

        if ac>=0:
            pc=mar
            return 1

        


    elif ir==0x05:#add m(x)

        ac+=mm[mar]

    elif ir==0x07:

        ac+=abs(mm[mar])

    elif ir==0x06:
        ac-=mm[mar]
    
    elif ir==0x08:
        ac-=abs(mm[mar])

    elif ir==0x0B:
        mq=mm[mar]*mq//(16**5)
        mq=(mm[mar]*mq)%(16**5)

    elif ir==0x0C:
        mq=ac//mm[mar]
        ac=ac%mm[mar]
        
    elif ir==0x24:
        ac=ac*2

    elif ir==0x25:
        ac=ac//2

    elif ir==0x22:
        temp = mm

    return 0

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

        pc=mar
        return 2

    elif ir==0x0F:#conditional jump

        if ac>=0:
            pc=mar
            return 2

        


    elif ir==0x05:#add m(x)

        ac+=mm[mar]

    elif ir==0x07:

        ac+=abs(mm[mar])

    elif ir==0x06:
        ac-=mm[mar]
    
    elif ir==0x08:
        ac-=abs(mm[mar])

    elif ir==0x0B:
        mq=mm[mar]*mq//(16**5)
        mq=(mm[mar]*mq)%(16**5)

    elif ir==0x0C:
        mq=ac//mm[mar]
        ac=ac%mm[mar]
        
    elif ir==0x24:
        ac=ac*2

    elif ir==0x25:
        ac=ac//2

    elif ir==0x22:
        temp = mm

    elif ir==0x00:
        return 0
    
    return 1

def main():
    global pc
    fetch()
    l=left()
    print(mar,ac,pc)
    if l:#JUMP
        print("jumped in left")
        main()
    else:

        print("now onto right")

        r=right()   
        if(r):
            if (r==2):
                print("jump")
                print(mar,ac,pc)
                main()
            else:

                print(mar,ac,pc)
                pc+=1
                main()
        else:

            print(mar,ac,pc)







    

    


##################testing###################

mm[0]=0x0110005101
mm[1]=0x0D005
mm[5]=0x21102
mm[0x100]=25
mm[0x101]=25


main()
print(mm[0x102])
# fetch()
# left()
# print(mar,ir,ibr,ac)
# right()
# print(mar,ir,ibr,ac)







