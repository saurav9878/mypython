inches = 10
feets = 5

centimeters = inches * 2.5 + 12 * 2.5 * feets
metres = centimeters / 12
centimeters = centimeters % 12

print metres
# round function rounds floating point numbers to 0 after floating point. 
print round(metres, 4)
print centimeters
