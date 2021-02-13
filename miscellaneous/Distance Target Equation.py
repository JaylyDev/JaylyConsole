import math
print("Aircraft Flying Object Distance Target Attitude Calculation")
print("Input distance to target (Nautical Miles / RNG):")
RNG = float(input())
print("Input Camera elevation angle:")
Degrees = int(input())
print("Input the height of Aircraft Altitude (Feet):")
height = int(input())
sin = math.sin(math.radians(-Degrees))
NMI = RNG**sin
FT = NMI*6076.11549
Resultfeet = height-FT
TargetAltitude = Resultfeet//3.281
printnmi = math.trunc(NMI)
printft = math.trunc(FT)
printResultfeet = math.trunc(Resultfeet)
printTargetAltitude = math.trunc(TargetAltitude)
print("")
print(str(RNG) + " * SIN(" + str(Degrees) + " degree) = " + str(printnmi))
print(str(printnmi) + " NMI = " + str(printft) + " FT")
print(str(height) + " - " + str(printft) + " = " + str(printResultfeet) + " Feet")
print("")
print("Target Altitude:")
print(str(printResultfeet) + " Feet = " + str(printTargetAltitude) + " Metre ")
exit = input()