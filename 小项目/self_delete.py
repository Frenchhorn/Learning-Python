print('code start')
#start
print "cheat code"
with open('self_delete.py','r') as fin:
    codes = [line for line in fin]
with open('self_delete.py','w') as fout:
    fout.writelines(codes[:1] + codes[8:])
#end
print("code end")