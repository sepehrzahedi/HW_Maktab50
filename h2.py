mypic = open("pic.png","rb")
my_newpic = open("new_mypic.png", "wb")
for i in mypic :
    my_newpic.write(i)
mypic.close()
my_newpic.close()