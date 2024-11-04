# Tutlokit v.1.0
# Developed by: Tutlo
# License: MIT

import time
import urllib.request

def loading():
	"""Show progress bar while loading"""
	print('[', end="")
	for i in range(50): 
		time.sleep(0.04)
		print('#', end="", flush=True)
	print(']')

def bootstrap():
	"""Application bootstrap"""
	print('\n[Initializing] ', end="", flush=True)
	loading()
	print('[Booting up] ', end="", flush=True)
	loading()
	# print header
	print_header()
	# call menu
	print_menu()

def info():
	"""Print software information"""
	print('\n---------------------------------------------')
	print('Tutlokit v.1.0 | Professional Hacking Equipment')
	print('Author: Tutlo')
	print('Made in Tutlograd, Republic of Tutlia')
	print('---------------------------------------------\n')
	input('Press ENTER to continue...')
	print_menu()

def scan():
	"""Scanner utility"""
	print('\n\n[Starting scanner]', end="", flush=True)
	loading()
	print('\n')
	print('====================================================================================')
	print('######## ##     ## ######## ##        #######   ######   ######     ###    ##    ## ')
	print('   ##    ##     ##    ##    ##       ##     ## ##    ## ##    ##   ## ##   ###   ## ')
	print('   ##    ##     ##    ##    ##       ##     ## ##       ##        ##   ##  ####  ## ')
	print('   ##    ##     ##    ##    ##       ##     ##  ######  ##       ##     ## ## ## ## ')
	print('   ##    ##     ##    ##    ##       ##     ##       ## ##       ######### ##  #### ')
	print('   ##    ##     ##    ##    ##       ##     ## ##    ## ##    ## ##     ## ##   ### ')
	print('   ##     #######     ##    ########  #######   ######   ######  ##     ## ##    ## ')
	print('====================================================================================')
	print('\n')

	# get URL
	target = input('Type in URL to scan and hit enter: ')
	
	try: 
		print('[SCANNING]: ' + target)
		print('[PROGRESS] ', end="", flush=True)
		loading()
		with urllib.request.urlopen(target) as url:
			print('\n')
			print(url.info())
	except:
		print('\n[ERROR] Error while trying to scan the URL.')
		print('\n[ERROR] Please check if URL is valid and try again.')


	# call menu again
	input('\nPress ENTER to continue...')
	print_menu()

def print_header():
	"""Print header ascii image"""
	print('\n')
	print('======================================================================')
	print('######## ##     ## ######## ##        #######  ##    ## #### ######## ')
	print('   ##    ##     ##    ##    ##       ##     ## ##   ##   ##     ##    ')
	print('   ##    ##     ##    ##    ##       ##     ## ##  ##    ##     ##    ')
	print('   ##    ##     ##    ##    ##       ##     ## #####     ##     ##    ')
	print('   ##    ##     ##    ##    ##       ##     ## ##  ##    ##     ##    ')
	print('   ##    ##     ##    ##    ##       ##     ## ##   ##   ##     ##    ')
	print('   ##     #######     ##    ########  #######  ##    ## ####    ##    ')
	print('======================================================================')
	print('\n')

def print_menu():
	"""Print menu with choices"""
	print('\n')
	print('==================================================')
	print('---------------------- Menu ----------------------')
	print('==================================================')
	print('Choose one of the provided options and hit enter')
	print('1. Info')
	print('2. Tutloscan')
	print('3. Exit')
	print(': ', end="")
	choice = input()

	if choice == '1':
		info()
	elif choice == '2':
		scan()
	elif choice == '3':
		print('\nExiting Tutlokit...')
		print('As far as I know, your computer science skill is very low!')
		print('Thanks for hacking with us!')
		print('See you again!\n')
		exit()
	else:
		print('\nUnknown option chosen.')
		print_menu()

def main():
	"""Main function"""
	bootstrap()

# Bootstrap
main()
