f=open("01_basic_write.txt","w+")
for i in range(1):
    f.write("1,Almasud Abdullah Al Masud\n2,rimon,Rimol Ali\n3,niloy,Niloy Roy\n4,sourov,Sourov Deb Sharma\n5,sathi,Sathi Rani Roy%d"%(i+1))
    print(f)
f.close()
