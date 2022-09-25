# x V y 
# V - or дизъюнкция
# /\ - and конъюнкция
# -x - not(x)

print('x y z Res')
for x in range(2):
    for y in range(2):
        for z in range(2):
            Res = x or y or z
        print(x, y, z, bool(Res))