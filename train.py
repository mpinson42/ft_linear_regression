import sys

def get_file():
	try:
		text = open(sys.argv[1], "r")
		text = text.read()
		text = text.replace("\t","")
		text = text.split('\n')
	except:
		print 'error open'
		sys.exit()
	return (text)




def pars_name(string):
	var = string.split(',')
	if(len(var) != 2):
		print 'error'
		sys.exit()
	if(len(var[0]) == 0 or len(var[1]) == 0):
			print 'error'
			sys.exit()
	return(var)


def pars_var(tab, nb):
	tab_x = []
	for i in tab:
		data = i.split(',')
		if(len(data) != 2):
			print 'error'
			sys.exit()
		if(len(data[0]) == 0 or len(data[1]) == 0):
			print 'error'
			sys.exit()
		tab_x.append(int(data[nb]))
	return tab_x




def estimatePrice(mileage, t0, t1):
	return(t0  + (t1 * mileage))




def zeta_0(km, price, t0, t1):
	i = 0
	y = 0
	while(i <= len(km) - 1):
		y += estimatePrice(km[i], t0, t1) - price[i]
		i += 1
	return(y);



def zeta_1(km, price, t0, t1):
	i = 0
	y = 0
	while(i <= len(km) - 1):
		y += (estimatePrice(km[i], t0, t1) - price[i]) * km[i]
		i += 1
	return(y);




def get_residu(km, price):
	i = 0
	
	t0 = 0
	t1 = 0
	
	while(i < 5000):
		tmpt0 =   zeta_0(km, price, t0, t1)
		tmpt1 =   zeta_1(km, price, t0, t1)
		t1 = tmpt1
		t0 = tmpt0
		i += 1




	print t0
	print t1
	print t0 + t1 * 42000






if ( __name__ == "__main__"):
	string = get_file()
	name = pars_name(string[0])
	print name
	string.remove(string[0])

	while '' in string:
		string.remove('')
	var_x = pars_var(string, 0)
	var_y = pars_var(string, 1)

	get_residu(var_x, var_y)

	print string;