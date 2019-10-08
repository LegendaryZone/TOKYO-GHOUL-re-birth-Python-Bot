from main import API
import sys
import time
from multiprocessing import Pool

def check(l):
	l=l.split(',')
	try:
		a=API()
		a.setuserId(l[2])
		a.setuuid(l[1])
		a.setconsumeId(l[0])
		a.login()
		a.getAllGifts()
		a.finishTutorial()
		a.getPlayer()
		if a.playerdata['player']['jewel']==97:
			a.gacha(10,10,597,171,2)
			a.gacha(10,10,434,133,2)
			a.gacha(10,10,598,171,2)
			a.freeunits(5)
		a.getPlayer()
		a.exportPlayer('selling.csv')
	except:
		pass

if __name__ == "__main__":
	with open(sys.argv[1]) as f:
		content = f.readlines()
		content = [x.strip() for x in content]
	print 'have %s accounts'%len(content)
	p= Pool(100)
	try:
		list(p.imap_unordered(check, content))
	except Exception:
		print("a worker failed, aborting...")
		p.close()
		p.terminate()
	else:
		p.close()
		p.join()
	print "job done"