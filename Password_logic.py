print ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"
print ",       ESET Crackme 2015 Password Logic       ,"
print ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"
i= 0
while (i < 1):
    print " "
    a= raw_input("Enter password: ")
    if (len(a) != 10):
        print "length of password should be equal to 10 characters"
        i=0
        continue
    if (int(a[4].encode("hex"),16)+ int(a[5].encode("hex"),16) != 162):
        print "The hexadecimal sum of character 4 and 5 should be equal to A2"
        i=0
        continue
    if (int(a[0].encode("hex"),16)+ int(a[8].encode("hex"),16) != 185):
        print "The hexadecimal sum of character 0 and 8 should be equal to B9"
        i=0
        continue
    if (int(a[4].encode("hex"),16)+ int(a[5].encode("hex"),16) + int(a[9].encode("hex"),16) != 273):
        print "The hexadecimal sum of character 4,5 and 9 should be equal to 111"
        i=0
        continue
    if (int(a[7].encode("hex"),16)+ int(a[3].encode("hex"),16)+ int(a[0].encode("hex"),16)+ int(a[8].encode("hex"),16) != 300):
        print "The hexadecimal sum of character 7,3,0 and 8 should be equal to 12C"
        i=0
        continue
    if (int(a[2].encode("hex"),16)+ int(a[6].encode("hex"),16) != 132):
        print "The hexadecimal sum of character 2 and 6 should be equal to 84"
        i=0
        continue
    if (int(a[0].encode("hex"),16)+ int(a[1].encode("hex"),16) +
        int(a[2].encode("hex"),16)+ int(a[3].encode("hex"),16) +
        int(a[4].encode("hex"),16)+ int(a[5].encode("hex"),16) +
        int(a[6].encode("hex"),16)+ int(a[7].encode("hex"),16) +
        int(a[8].encode("hex"),16)+ int(a[9].encode("hex"),16) != 813):
        print "The hexadecimal sum of all character should be equal to 32D"
        i=0
        continue
    if (int(a[0].encode("hex"),16) != 69):
        print ("Nice work little help, \n char[0] = 45 \n char[6] + char[1] = D0 \n char[3] - char[4] = E \n char[5] + char[7] = 9F")
        continue
    if (int(a[6].encode("hex"),16)+ int(a[1].encode("hex"),16) != 208):
        print ("Nice work little help, \n char[0] = 45 \n char[6] + char[1] = D0 \n char[3] - char[4] = E \n char[5] + char[7] = 9F")
        continue
    if (int(a[3].encode("hex"),16)- int(a[4].encode("hex"),16) != 14):
        print ("Nice work little help, \n char[0] = 45 \n char[6] + char[1] = D0 \n char[3] - char[4] = E \n char[5] + char[7] = 9F")
        continue
    if (int(a[5].encode("hex"),16)+ int(a[7].encode("hex"),16) != 159):
        print ("Nice work little help, \n char[0] = 45 \n char[6] + char[1] = D0 \n char[3] - char[4] = E \n char[5] + char[7] = 9F")
        continue
    i=i+1
print " "
print "You guessed the right password"
xa= raw_input("Press enter to exit....")
