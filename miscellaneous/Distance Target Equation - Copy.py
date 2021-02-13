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
print("")
print(str(RNG) + " * SIN(" + str(Degrees) + " degree) = " + str(NMI))
print(str(NMI) + " NMI = " + str(FT) + " FT")
print(str(height) + " - " + str(FT) + " = " + str(Resultfeet) + " Feet")
print("")
print("Target Altitude:")
print(str(Resultfeet) + " Feet = " + str(TargetAltitude) + " Metre ")
exit = input()