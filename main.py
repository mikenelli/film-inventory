#!/usr/bin/python
from time import strftime
import base64

def write():
	clear()
	print('How many days do you plan to check out '+ cc + '?')
	length = raw_input('Please type a number: ').strip()
	length = length if length.isdigit() else write() #loops write() if number of days is not a number
	clear()
	if noid == False:
		print('ID number of ' + cc + ' being checked out?')
		id = raw_input('ID number: ').strip()
		clear()
	if noid == True:
		id = '1'
	print('Reason for checking '+ cc + ' out?' )
	reason = raw_input('Please type a reason: ').strip()
	clear()
	log = (time+': '+name+' checked out '+cc+' #'+id+' for '+length+' day(s)'+' reason: '+reason)
	logenc = base64.b64encode(log)
	f = open('log.txt', 'a')
	f.write(logenc + '\n')
	f.close()
	print(name + ' sucessfully checked out ' + cc + ' #'+id+'\n')
	print('would you like to check out anything else?')
	anotherone = raw_input('y/n: ')
	clear()
	if anotherone == ('y'):
		return checkout()
	if anotherone == ('n'):
		return main()
	else:
		return main()

def checkout():
	global time, cc, noid
	noid = False
	time = strftime("%b %d %Y %I:%M")
	print('What are you checking out?\n\n1. Camera\n2. Audio\n3. Grip\n4. Lens\n5. Other')
	equip = raw_input('Make a selection: ')
	clear()
	if equip == '1':
		print('Cameras\n1. Varicam\n2. Panasonic 200\n3. Canon 60D')
		camchose = raw_input('Make a selection: ')
		clear()
		if camchose == '1':
			camcheck = ('Varicam')
			noid = True
			cc = camcheck
			write()
		if camchose == '2':
			camcheck = ('200')
			cc = camcheck
			write()
		if camchose == '3':
			camcheck = ('60D')
			cc = camcheck
			write()
		else:
			print('invalid selection')
			return checkout()

	if equip == '2':
		print('Audio Devices\n1. H6N\n2. H4N\n3. Rodemic\n4. Boom')
		audchose = raw_input('Make a selection: ')
		if audchose == '1':
			audcheck = ('H6N')
			cc = audcheck
			write()
		if audchose == '2':
			audcheck = ('H4N')
			cc = audcheck
			write()
		if audchose == '3':
			audcheck = ('Rodemic')
			cc = audcheck
			write()
		if audchose == '4':
			audcheck = ('Boom')
			cc = audcheck
			write()

	if equip == '3':
		print('Grip\n1. Tripod\n2. Steadicam\n3. XLR cable\n4. C-Stand')
		gripchose = raw_input('Make a selection: ')
		if gripchose == '1':
			gripcheck = ('Tripod')
			cc = gripcheck
			write()
		if gripchose == '2':
			gripcheck = ('Steadicam')
			noid = True
			cc = gripcheck
			write()
		if gripchose == '3':
			gripcheck = ('XLR cable')
			cc = gripcheck
			write()
		if gripchose == '4':
			gripcheck = ('C-Stand')
			cc = gripcheck
			write()		
			
	if equip == '4':
		print('Lenses\n1. Cine Kit (entire case)\n2. Canon 23-135mm\n3. Canon 50mm\n4. Cine 50')
		lenschose = raw_input('Make a selection: ')
		if lenschose == '1':
			lenschose = "CineKit"
			noid = True
			cc = lenschose
			write()
		if lenschose == '2':
			lenschose = "C23-135"
			cc = lenschose
			write()
		if lenschose == '3':
			lenschose = "C50"
			cc = lenschose
			write()
		if lenschose == '4':
			lenschose = "Cine50"
			cc = lenschose
			write()
	if equip == '5':
		print('Nothing here yet')
		clear()
		return checkout()


def main():
	print('Main Menu\n\n1: Checkout equipment\n2. Check who has equipment')
	var = raw_input('Make a selection: ')
	clear()
	if var == '1':
		global name
		print('Please enter your name')
		name = raw_input('Name: ').strip()
		clear()
		checkout()
	if var == '2':
		clear()
		for line in (open("log.txt").readlines()):
			dec = line.rstrip()
			print base64.b64decode(dec)
		print(' ')
		raw_input('Press enter to continue')
		clear()
		main()
	if var == 'exit':
		raw_input()
		
def clear():
	print(chr(27) + "[2J")
			
main()
	
