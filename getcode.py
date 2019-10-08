from main import API

logins='''2841C7DF-B399-4980-B320-EDBB3FCD406B,ecbedae6-75ef-41ab-9da4-bbae58a5d132,231352606796,ios,user: 231352606796 code: ed4abnaee9mcpl5e,0,,'''

for l in logins.split('\n'):
	l=l.split(',')
	a=API()
	a.setuserId(l[2])
	a.setuuid(l[1])
	a.setconsumeId(l[0])
	a.login()
	a.getAllGifts()
	a.finishTutorial()
	a.getPlayer()
	#a.freeunits(10)
	a.getPlayer()
	a.exportPlayer('selling.csv')