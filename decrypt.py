'''' Crackme Decrypt
     hex input
''''
import sys
if ("idlelib" in sys.modules):
    print ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"
    print ", Enter the hexadecimal code of encrypted text ,"
    print ",               Without any space              ,"
    print ",            Like 04014C2344111246             ,"
    print ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"
    print " "
    print " "
    a= raw_input("Enter pass key [Default is El B4nd1to]: ") or "El B4nd1to"
    b= raw_input("Enter hex values of encoded string [Enter to decrypt default text]: ") or "04014C23441112461A1033074D2A4551466A1904670957214503035756052F0B02365F170E475601261D51335902021F5613321A02305E15465E1302340F4521160909465602220B022D45501141191F204028104409464719512B014D2F16160941560228034764431E14561014350B4C27531446571705264202305E1112131510294E4021161403500408371A472016040E5656022603476441111F131702671A4A2D455012560E0569"
    ans= ''
    n= 0
    i= 0
    while (i < len(b)-1):
        if n > len(a)-1:
            n=0
        c = "0x" + b[i] + b[i+1]
        c = int(c,16)
        d = int(a[n].encode("hex"),16) + 2
        e = c^d
        n = n+1
        i = i+2
        ans = ans+chr(e)
    print " "
    print "Decrypted text is"
    print " "
    print ans
else:
    print ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"
    print ", Please run the code in Idle ,"
    print ",            Not in           ,"
    print ",        Command Prompt       ,"
    print ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"
    print " "
    print " "
print " "
x=raw_input("Press enter to exit....")
