from main import API
import sys
from multiprocessing import Pool

def check(l):
	l=l.split(',')
	try:
		a=API()
		a.setuserId(l[2])
		a.setuuid(l[1])
		a.setconsumeId(l[0])
		a.login()
		a.exportCode()
		a.getAllGifts()
		a.freeunits(10)
		#a.gacha(4,10,434,133,2)
		#a.gacha(2,10,565,141,2)
		a.getPlayer()
		a.exportPlayer()
	except:
		pass

if __name__ == "__main__":
	with open(sys.argv[1]) as f:
		content = f.readlines()
		content = [x.strip() for x in content]
	print 'have %s accounts'%len(content)
	p= Pool(25)
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