
t0 = 0
t1 = 0

def estimatePrice(mileage):
	return(t0  + (t1 * mileage))


i = 0;
y = 0;
while(i <= 5):
	y += i * i + i
	i += 1

print y