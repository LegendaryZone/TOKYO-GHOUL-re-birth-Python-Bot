import requests
from tools import Crypter
import json
import random
import zlib
import socket
import struct
import time
import io
from collections import OrderedDict

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class API(object):
	def __init__(self):
		self.s=requests
		#self.s.verify=False
		self.crypter=Crypter()
		self.deviceType='ios'
		self.deviceModel='iPad5,4'
		self.osVersion='iOS 10.2'
		self.hackStatus='0'
		self.userId=str(0)
		self.uuid=''
		self.appVersion='2.2.7'
		self.advertiseId='00000000-0000-0000-0000-000000000000'
		self.consumeId=self.rndDeviceId()#'2841C7DF-B399-4980-B320-EDBB3FCD406B'#
		self.appKey='u8VT1aaEQbqtYlsR'
		self.step=0
		self.ssr={6:'Ken Kaneki (Dark)',10:'Toka Kirishima (Speed)',11:'Toka Kirishima (Light)',15:'Nishiki Nishio (Strength)',19:'Shu Tsukiyama (Dark)',25:'Ryoko Fueguchi (Wizdom)',42:'Ayato Kirishima (Speed)',46:'Yamori (Strength)',61:'Rize Kamishiro (Wizdom)',66:'Kohtaro Amon (Strength)',101:'Shu Tsukiyama (Strength)',102:'Hinami Fueguchi (Light)',105:'Renji Yomo (Speed)',106:'Uta (Dark)',107:'Uta (Wizdom)',110:'Tatara (Strength)',113:'Noro (Dark)',116:'Naki (Strength)',122:'Kurona Yasuhisa (Dark)',125:'Nashiro Yasuhisa (Light)',127:'Akira Mado (Speed)',128:'Kureo Mado (Wizdom)',129:'Kureo Mado (Dark)',130:'Juzo Suzuya (Speed)',131:'Kisho Arima (Dark)',133:'Yukinori Shinohara (Speed)',138:'Ken Kaneki (Light)',139:'Toka Kirishima (Dark)',140:'Kohtaro Amon (Wizdom)',141:'Kisho Arima (Light)',143:'Nishiki Nishio (Wizdom)',144:'Nishiki Nishio (Speed)',200:'Kohtaro Amon (Wizdom)',201:'Ken Kaneki (Dark)',202:'Hinami Fueguchi (Wizdom)',203:'Akira Mado (Light)',204:'Hinami Fueguchi (Speed)',205:'Juzo Suzuya (Strength)',206:'Toka Kirishima (Wizdom)',207:'Ayato Kirishima (Wizdom)',208:'Renji Yomo (Strength)',209:'Rize Kamishiro (Dark)',210:'Nishiki Nishio (Strength)',212:'Toka Kirishima (Wizdom)',214:'Juzo Suzuya (Wizdom)',215:'Kohri Ui (Strength)',216:'Toka Kirishima (Strength)',217:'Kohsuke Hoji (Light)',218:'Tatara (Wizdom)',220:'Kohtaro Amon (Light)',221:'Juzo Suzuya (Dark)',222:'Hinami Fueguchi (Light)',223:'Yamori (Dark)',224:'Ken Kaneki (Strength)',225:'Kohtaro Amon (Speed)',226:'Eto (Light)',228:'Renji Yomo (Speed)',232:'Ken Kaneki (Wizdom)',233:'Kohtaro Amon (Dark)',234:'Akira Mado (Wizdom)',236:'Shachi (Strength)',238:'Ken Kaneki (Wizdom)',239:'Iwao Kuroiwa (Light)',242:'Ayato Kirishima (Light)',245:'Renji Yomo (Wizdom)',246:'Akira Mado (Wizdom)',247:'Toka Kirishima (Strength)',250:'Ken Kaneki (Strength)',251:'Yukinori Shinohara (Wizdom)',253:'Taishi Fura (Strength)',255:'Kisho Arima (Speed)',256:'Lantern (Dark)',258:'Uruka Minami (Dark)',259:'Taishi Fura (Strength)',261:'Uta (Speed)',262:'Shu Tsukiyama (Wizdom)',263:'Toka Kirishima (Light)',264:'Lantern (Strength)',267:'Naki (Wizdom)',268:'Juzo Suzuya (Strength)',269:'Kurona Yasuhisa (Speed)',270:'Nashiro Yasuhisa (Speed)',273:'Uta (Light)',274:'Akira Mado (Speed)',276:'Akira Mado (Light)',277:'Hinami Fueguchi (Light)',278:'Kohsuke Hoji (Wizdom)',279:'Kisho Arima (Strength)',280:'Rize Kamishiro (Strength)',281:'Kohtaro Amon (Strength)',284:'Ken Kaneki (Speed)',285:'Toka Kirishima (Speed)',286:' (Wizdom)',288:'Yukinori Shinohara (Speed)',289:'Kaya Irimi (Wizdom)',292:'Yamori (Dark)',296:'Iwao Kuroiwa (Speed)',300:'Haise Sasaki (Light)',309:'Kuki Urie (Strength)',310:'Ginshi Shirazu (Speed)',314:'Shu Tsukiyama (Light)',315:'Juzo Suzuya (Light)',318:'Hinami Fueguchi (Wizdom)',320:'Akira Mado (Strength)',325:'Saiko Yonebayashi (Dark)',328:'Toru Mutsuki (Wizdom)',330:'Ken Kaneki (Dark)',331:'Rize Kamishiro (Light)',334:'Toka Kirishima (Speed)',335:'Haise Sasaki (Dark)',336:'Nishiki Nishio (Speed)',337:'Juzo Suzuya (Speed)',338:'Ginshi Shirazu (Strength)',346:'Ken Kaneki (Dark)',349:'Ayato Kirishima (Wizdom)',350:'Nutcracker (Dark)',351:'Akira Mado (Light)',355:'Iwao Kuroiwa (Wizdom)',356:'Yukinori Shinohara (Speed)',358:'Non-Killing Owl (Strength)',362:'Saiko Yonebayashi (Strength)',364:'Haise Sasaki (Wizdom)',10011:'Toka Kirishima (Light)',10042:'Ayato Kirishima (Speed)',10102:'Hinami Fueguchi (Light)',10141:'Kisho Arima (Light)',10201:'Ken Kaneki (Dark)',10204:'Hinami Fueguchi (Speed)',10209:'Rize Kamishiro (Dark)',10210:'Nishiki Nishio (Strength)',10224:'Ken Kaneki (Strength)',10225:'Kohtaro Amon (Speed)',10234:'Akira Mado (Wizdom)',10238:'Ken Kaneki (Wizdom)',10338:'Ginshi Shirazu (Strength)',5032:'Noro (Dark)',5033:'Shachi (Light)',5034:'Kisho Arima (Wizdom)',5037:'Non-Killing Owl (Strength)',5060:'Toru Mutsuki (Wizdom)',5061:'Saiko Yonebayashi (Strength)',5063:'Akira Mado (Wizdom)',5064:'Hinami Fueguchi (Light)',5065:'Kuki Urie (Strength)',5066:'Ayato Kirishima (Speed)',5067:'Ginshi Shirazu (Speed)',5068:'Torso (Dark)',5069:'Toka Kirishima (Wizdom)',5070:'Haise Sasaki (Wizdom)',5071:'Donato Porpora (Strength)',5072:'Haise Sasaki (Wizdom)',5073:'Roma (Speed)',5074:'Toru Mutsuki (Light)',5075:'Take Hirako (Light)',5076:'Nico (Dark)',5080:'Eto (Speed)',5083:'Kimi Nishino (Wizdom)',5084:'Nishiki Nishio (Speed)',5086:'Ken Kaneki (Dark)',5092:'Hinami Fueguchi (Light)',5093:'Toka Kirishima (Strength)',5094:'Ken Kaneki (Wizdom)',5095:'Shu Tsukiyama (Wizdom)',5096:'Nishiki Nishio (Strength)',5097:'Ken Kaneki (Dark)',5098:'Toka Kirishima (Light)',601012:'Ken Kaneki (Dark)',601011:'Ken Kaneki (Dark)',601022:'Ken Kaneki (Dark)',601021:'Ken Kaneki (Dark)',601032:'Ken Kaneki (Dark)',601031:'Ken Kaneki (Dark)',602011:'Rize Kamishiro (Light)',602021:'Rize Kamishiro (Light)',602031:'Rize Kamishiro (Light)',603011:'Haise Sasaki (Light)',603012:'Haise Sasaki (Dark)',603021:'Haise Sasaki (Light)',603022:'Haise Sasaki (Dark)',603031:'Haise Sasaki (Light)',603032:'Haise Sasaki (Dark)',604012:'Ginshi Shirazu (Speed)',604011:'Ginshi Shirazu (Strength)',604022:'Ginshi Shirazu (Speed)',604021:'Ginshi Shirazu (Strength)',604032:'Ginshi Shirazu (Speed)',604031:'Ginshi Shirazu (Strength)',604013:'Ginshi Shirazu (Strength)',605011:'Akira Mado (Light)',605021:'Akira Mado (Light)',605031:'Akira Mado (Light)',606011:'Haise Sasaki (Wizdom)',606021:'Haise Sasaki (Wizdom)',606031:'Haise Sasaki (Wizdom)',702011:'Nishiki Nishio (Speed)',702012:'Toka Kirishima (Dark)',702021:'Nishiki Nishio (Speed)',702022:'Toka Kirishima (Dark)',702031:'Nishiki Nishio (Speed)',702032:'Toka Kirishima (Dark)',703011:'Nishiki Nishio (Strength)',703012:'Ken Kaneki (Light)',703021:'Nishiki Nishio (Strength)',703022:'Ken Kaneki (Light)',703031:'Nishiki Nishio (Strength)',703032:'Ken Kaneki (Light)',704011:'Uta (Dark)',704021:'Uta (Dark)',704031:'Uta (Dark)',705011:'Shu Tsukiyama (Dark)',705021:'Shu Tsukiyama (Dark)',705031:'Shu Tsukiyama (Dark)',711011:'Hinami Fueguchi (Wizdom)',711021:'Hinami Fueguchi (Wizdom)',711031:'Hinami Fueguchi (Wizdom)',712011:'Toka Kirishima (Wizdom)',712021:'Toka Kirishima (Wizdom)',712031:'Toka Kirishima (Wizdom)',713011:'Juzo Suzuya (Wizdom)',713021:'Juzo Suzuya (Wizdom)',713031:'Juzo Suzuya (Wizdom)',714011:'Tatara (Wizdom)',714021:'Tatara (Wizdom)',714031:'Tatara (Wizdom)',715012:'Itsuki Marude (Light)',715011:'Kohtaro Amon (Light)',715022:'Itsuki Marude (Light)',715021:'Kohtaro Amon (Light)',715032:'Itsuki Marude (Light)',715031:'Kohtaro Amon (Light)',716011:'Yamori (Dark)',716021:'Yamori (Dark)',716031:'Yamori (Dark)',305701:'Non-Killing Owl (Dark)',305801:'Non-Killing Owl (Dark)',305901:'Non-Killing Owl (Dark)',306101:'Kisho Arima (Light)',306201:'Kisho Arima (Light)',306301:'Kisho Arima (Light)',300501:'Yukinori Shinohara (Wizdom)',300601:'Yukinori Shinohara (Wizdom)',300701:'Yukinori Shinohara (Wizdom)',310501:'Yukinori Shinohara (Wizdom)',300901:'Iwao Kuroiwa (Strength)',301001:'Iwao Kuroiwa (Strength)',301101:'Iwao Kuroiwa (Strength)',310901:'Iwao Kuroiwa (Strength)',300101:'Yamori (Strength)',300201:'Yamori (Strength)',300301:'Yamori (Strength)',310101:'Yamori (Strength)',306501:'Naki (Speed)',306601:'Naki (Speed)',306701:'Naki (Speed)',316501:'Naki (Speed)',306901:'Tatara (Light)',307001:'Tatara (Light)',307101:'Tatara (Light)',307301:'Noro (Dark)',307401:'Noro (Dark)',307501:'Noro (Dark)',307701:'Kohsuke Hoji (Light)',307801:'Kohsuke Hoji (Light)',307901:'Kohsuke Hoji (Light)',308501:'Ken Kaneki (Wizdom)',308601:'Ken Kaneki (Wizdom)',308701:'Ken Kaneki (Wizdom)',308901:'Rize Kamishiro (Speed)',309001:'Rize Kamishiro (Speed)',309101:'Rize Kamishiro (Speed)',309301:'Kohtaro Amon (Strength)',309401:'Kohtaro Amon (Strength)',309501:'Kohtaro Amon (Strength)',309701:'Akira Mado (Speed)',309801:'Akira Mado (Speed)',309901:'Akira Mado (Speed)',311001:'Ayato Kirishima (Strength)',311101:'Ayato Kirishima (Strength)',311201:'Ayato Kirishima (Strength)',311011:'Ayato Kirishima (Strength)',311401:'Eto (Dark)',311501:'Eto (Dark)',311601:'Eto (Dark)',311801:'Juzo Suzuya (Strength)',311901:'Juzo Suzuya (Strength)',312001:'Juzo Suzuya (Strength)',311811:'Juzo Suzuya (Strength)',312201:'Kureo Mado (Light)',312301:'Kureo Mado (Light)',312401:'Kureo Mado (Light)',312601:'Nishiki Nishio (Dark)',312701:'Nishiki Nishio (Dark)',312801:'Nishiki Nishio (Dark)',313001:'Nutcracker (Light)',313101:'Nutcracker (Light)',313201:'Nutcracker (Light)',313401:'Haise Sasaki (Dark)',313501:'Haise Sasaki (Dark)',313601:'Haise Sasaki (Dark)',313801:'Ginshi Shirazu (Light)',313901:'Ginshi Shirazu (Light)',314001:'Ginshi Shirazu (Light)',314201:'Non-Killing Owl (Wizdom)',314301:'Non-Killing Owl (Wizdom)',314401:'Non-Killing Owl (Wizdom)',314601:'Kisho Arima (Wizdom)',314701:'Kisho Arima (Wizdom)',314801:'Kisho Arima (Wizdom)',943031:'Nishiki Nishio (Speed)',944041:'Ayato Kirishima (Wizdom)',945041:'Toru Mutsuki (Wizdom)',945042:'Ginshi Shirazu (Speed)',945043:'Saiko Yonebayashi (Dark)'}
		self.havesssr={}
		#if 'Admin' in socket.gethostname():
		#	self.s.proxies.update({'http': 'http://127.0.0.1:8888','https': 'https://127.0.0.1:8888',})
		
	def genRandomIP(self):
		return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
		
	def rndHex(self,n):
		return ''.join([random.choice('0123456789ABCDEF') for x in range(n)])
	
	def rndDeviceId(self):
		s='%s-%s-%s-%s-%s'%(self.rndHex(8),self.rndHex(4),self.rndHex(4),self.rndHex(4),self.rndHex(12))
		return s

	def setDevice(self,device):
		self.deviceType=device

	def setuserId(self,userId):
		self.userId=str(userId)

	def setconsumeId(self,id):
		self.consumeId=str(id)

	def setuuid(self,id):
		self.uuid=str(id)

	def log(self,msg):
		print '[%s]%s'%(time.strftime('%H:%M:%S'),msg.encode('utf-8'))
		
	def checkSSR(self,id):
		if id in self.ssr:
			if id in self.havesssr:
				self.havesssr[id]+=1
			else:
				self.havesssr[id]=1
			#self.log('have ssr: %s'%(self.ssr[id]))
		
	def getPlayer(self):
		playerdata=self.callAPI('/tkr/player/getdata',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.playerdata=playerdata
		self.log('hello %s gems:%s rank:%s coin:%s'%(playerdata['player']['name'],playerdata['player']['jewel'],playerdata['player']['rank'],playerdata['player']['coin']))
		self.havesssr={}
		if len(self.havesssr)==0:
			for u in playerdata['units']:
				self.checkSSR(u['unitId'])

	def login(self):
		self.callAPI('/tkr/login/startup',['advertiseId=%s'%self.advertiseId,'appKey=%s'%self.appKey,'appVersion=%s'%self.appVersion,'consumeId=%s'%self.consumeId,'deviceType=%s'%self.deviceType,'userId=%s'%self.userId])
		self.callAPI('/tkr/login/auth',['advertiseId=%s'%self.advertiseId,'appKey=%s'%self.appKey,'consumeId=%s'%self.consumeId,'deviceModel=%s'%self.deviceModel,'deviceType=%s'%self.deviceType,'hackStatus=%s'%self.hackStatus,'osVersion=%s'%self.osVersion,'uuid=%s'%self.uuid])
		if not hasattr(self,'accessKey'):	exit(1)
		self.callAPI('/tkr/tutorial',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/login/loginbonus/get',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.getPlayer()
		
	def callAPI(self,url,data):
		#self.log('doing %s step'%(self.step))
		crypted_data=[]
		for i in data:
			if 'postHash' in i:	continue
			i=i.split('=')
			crypted_data.append('%s=%s'%(i[0],self.encode(i[1]).replace('=','%3d').replace('+','%2b').replace('/','%2f')))
		crypted_data.append('postHash=%s'%(self.calcpostHash(''.join(data))).replace('==','%3d%3d').replace('+','%2b').replace('/','%2f'))
		rdata=self.s.post('https://tkr-i18n-prd.channel.or.jp'+url,data='&'.join(crypted_data),headers=OrderedDict([('deviceType','ios'),('X-Unity-Version','5.6.4p4'),('userId',str(self.userId)),('Accept-Language','en-gb'),('Content-Type','application/x-www-form-urlencoded; charset=utf-8'),('language','en'),('User-Agent','BNEI0345/188 CFNetwork/808.2.16 Darwin/16.3.0'),('timezone','CET 02:00:00'),('X-App-Version',self.appVersion),('country','DE'),('currency','EUR')]),verify=False)
		plaindata= json.loads(self.decode(rdata.content))
		#if 'invasionInfo' in plaindata:
			#self.log(str(plaindata['invasionInfo']['user']['userId']))
		if 'accessKey' in plaindata and not hasattr(self,'accessKey'):
			self.log('found accessKey')
			self.accessKey=plaindata['accessKey']
		if 'uuid' in plaindata and self.uuid=='':
			self.log('found uuid')
			self.uuid=plaindata['uuid']
		if 'userId' in plaindata and self.userId=='0':
			self.log('found userId')
			self.userId=str(plaindata['userId'])
		if 'questToken' in plaindata:
			self.log('found questToken')
			self.questToken=str(plaindata['questToken'])
		if 'gachaDrawToken' in plaindata:
			self.log('found gachaDrawToken')
			self.gachaDrawToken=str(plaindata['gachaDrawToken'])
		if plaindata['res']=='00001':
			self.log('bad res..')
			#exit(1)
		#self.log('%s = %s,%s'%(plaindata['res'],self.step+1,url))
		self.step+=1
		time.sleep(1)
		return plaindata

	def gacha(self,category,drawNum,gachaDrawId,gachaNo,mode):
		self.callAPI('/tkr/gacha/gacha',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'category=%s'%str(category),'consumeId=%s'%self.consumeId,'drawNum=%s'%str(drawNum),'gachaDrawId=%s'%str(gachaDrawId),'gachaDrawToken=%s'%self.gachaDrawToken,'gachaNo=%s'%str(gachaNo),'mode=%s'%str(mode),'userId=%s'%self.userId,'uuid=%s'%self.uuid])
		
	def getAllGifts(self):
		mypresents=self.callAPI('/tkr/player/presentbox/list',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'userId=%s'%self.userId,'uuid=%s'%self.uuid])
		presents=[]
		if 'presents' in mypresents and len(mypresents['presents'])==0:	return
		for p in mypresents['presents']:
			presents.append(p['id'])
		presents.sort()
		presentIdMax=presents[-1]
		presentIdMin=presents[0]
		self.callAPI('/tkr/player/presentbox/receiveall',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'presentCount=%s'%str(len(presents)),'presentFilterDec=%s'%'131123','presentIdMax=%s'%str(presentIdMax),'presentIdMin=%s'%str(presentIdMin),'userId=%s'%self.userId,'uuid=%s'%self.uuid])
		
	def freeunits(self,howmany=1):
		i=0
		while(i<howmany):
			self.gacha(6,10,431,2,2)
			i += 1
		
	def reroll(self):
		self.callAPI('/tkr/login/startup',['advertiseId=%s'%self.advertiseId,'appKey=%s'%self.appKey,'appVersion=%s'%self.appVersion,'consumeId=%s'%self.consumeId,'deviceType=%s'%self.deviceType,'userId=%s'%self.userId])
		#self.callAPI('/tkr/login/readgdpragreement',['advertiseId=%s'%self.advertiseId,'appKey=%s'%self.appKey,'appVersion=%s'%self.appVersion,'consumeId=%s'%self.consumeId,'deviceType=%s'%self.deviceType,'readGdprAgreementsJson=%s'%'[{"category":1,"agreementNo":2},{"category":2,"agreementNo":3}]'])
		self.callAPI('/tkr/login/auth',['advertiseId=%s'%self.advertiseId,'appKey=%s'%self.appKey,'consumeId=%s'%self.consumeId,'deviceModel=%s'%self.deviceModel,'deviceType=%s'%self.deviceType,'hackStatus=%s'%self.hackStatus,'osVersion=%s'%self.osVersion,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/login/signup/namecheck',['advertiseId=%s'%self.advertiseId,'appKey=%s'%self.appKey,'consumeId=%s'%self.consumeId,'name=%s'%'Haise'])
		signUpToken=self.callAPI('/tkr/login/signup/createtoken',['advertiseId=%s'%self.advertiseId,'appKey=%s'%self.appKey,'consumeId=%s'%self.consumeId])['signUpToken']
		self.callAPI('/tkr/login/signup',['advertiseId=%s'%self.advertiseId,'appKey=%s'%self.appKey,'consumeId=%s'%self.consumeId,'deviceModel=%s'%self.deviceModel,'deviceType=%s'%self.deviceType,'name=%s'%'Haise','osVersion=%s'%self.osVersion,'signUpToken=%s'%signUpToken])
		self.callAPI('/tkr/login/auth',['advertiseId=%s'%self.advertiseId,'appKey=%s'%self.appKey,'consumeId=%s'%self.consumeId,'deviceModel=%s'%self.deviceModel,'deviceType=%s'%self.deviceType,'hackStatus=%s'%self.hackStatus,'osVersion=%s'%self.osVersion,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/tutorial',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/inherit/getcode',['advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'playerInfoJson=%s'%'{}','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/tutorial',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/login/loginbonus/get',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/player/getdata',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/invasion/tutorial/getFinish',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/invasion/info/get',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'invasionId=%s'%'8','requestUtcTime=%s'%'0','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/quest/token/create',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'tokenType=%s'%'0','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		hash=self.callAPI('/tkr/quest/sneak',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'areaNumber=%s'%'0','consumeId=%s'%self.consumeId,'difficulty=%s'%'1','invasionId=%s'%'0','questCategory=%s'%'1','questGroupId=%s'%'3001','questId=%s'%'1011','questToken=%s'%self.questToken,'userId=%s'%self.userId,'uuid=%s'%self.uuid])['hash']
		time.sleep(20)
		self.callAPI('/tkr/quest/token/create',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'hash=%s'%hash,'tokenType=%s'%'3','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/tutorial/updatestep/2',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'clearTrophyList=%s'%'[{"trophyId":1},{"trophyId":15},{"trophyId":34}]','consumeId=%s'%self.consumeId,'dropResult=%s'%'[{"sessionType":0,"order":0,"pos":3,"dropKind":0,"partsEnemyId":0},{"sessionType":0,"order":0,"pos":1,"dropKind":0,"partsEnemyId":0},{"sessionType":0,"order":1,"pos":1,"dropKind":0,"partsEnemyId":0}]','hash=%s'%hash,'questToken=%s'%self.questToken,'updateAchieveList=%s'%'[{"achieveId":210001,"progress":2},{"achieveId":210002,"progress":2},{"achieveId":210003,"progress":2},{"achieveId":210004,"progress":2},{"achieveId":210005,"progress":2},{"achieveId":210006,"progress":2},{"achieveId":210007,"progress":2},{"achieveId":210008,"progress":2},{"achieveId":210009,"progress":2},{"achieveId":213001,"progress":3},{"achieveId":213002,"progress":3},{"achieveId":213003,"progress":3},{"achieveId":213004,"progress":3},{"achieveId":213005,"progress":3},{"achieveId":213006,"progress":3},{"achieveId":213007,"progress":3},{"achieveId":213008,"progress":3},{"achieveId":213009,"progress":3},{"achieveId":215001,"progress":1},{"achieveId":215002,"progress":1},{"achieveId":215003,"progress":1},{"achieveId":413001,"progress":3}]','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/invasion/info/get',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'invasionId=%s'%'8','requestUtcTime=%s'%'0','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/quest/token/create',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'tokenType=%s'%'0','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		hash=self.callAPI('/tkr/quest/sneak',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'areaNumber=%s'%'0','consumeId=%s'%self.consumeId,'difficulty=%s'%'1','invasionId=%s'%'0','questCategory=%s'%'1','questGroupId=%s'%'3001','questId=%s'%'1012','questToken=%s'%self.questToken,'userId=%s'%self.userId,'uuid=%s'%self.uuid])['hash']
		time.sleep(10)
		self.callAPI('/tkr/quest/token/create',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'hash=%s'%hash,'tokenType=%s'%'3','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		time.sleep(10)
		self.callAPI('/tkr/tutorial/updatestep/3',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'clearTrophyList=%s'%'[{"trophyId":1},{"trophyId":15},{"trophyId":34}]','consumeId=%s'%self.consumeId,'dropResult=%s'%'[{"sessionType":0,"order":0,"pos":1,"dropKind":0,"partsEnemyId":0},{"sessionType":0,"order":0,"pos":3,"dropKind":0,"partsEnemyId":0},{"sessionType":0,"order":1,"pos":1,"dropKind":0,"partsEnemyId":0}]','hash=%s'%hash,'questToken=%s'%self.questToken,'updateAchieveList=%s'%'[{"achieveId":210001,"progress":1},{"achieveId":210002,"progress":1},{"achieveId":210003,"progress":1},{"achieveId":210004,"progress":1},{"achieveId":210005,"progress":1},{"achieveId":210006,"progress":1},{"achieveId":210007,"progress":1},{"achieveId":210008,"progress":1},{"achieveId":210009,"progress":1},{"achieveId":211001,"progress":3},{"achieveId":211002,"progress":3},{"achieveId":211003,"progress":3},{"achieveId":211004,"progress":3},{"achieveId":211005,"progress":3},{"achieveId":211006,"progress":3},{"achieveId":211007,"progress":3},{"achieveId":211008,"progress":3},{"achieveId":211009,"progress":3},{"achieveId":213001,"progress":2},{"achieveId":213002,"progress":2},{"achieveId":213003,"progress":2},{"achieveId":213004,"progress":2},{"achieveId":213005,"progress":2},{"achieveId":213006,"progress":2},{"achieveId":213007,"progress":2},{"achieveId":213008,"progress":2},{"achieveId":213009,"progress":2},{"achieveId":214001,"progress":3},{"achieveId":214002,"progress":3},{"achieveId":214003,"progress":3},{"achieveId":214004,"progress":3},{"achieveId":214005,"progress":3},{"achieveId":214006,"progress":3},{"achieveId":214007,"progress":3},{"achieveId":214008,"progress":3},{"achieveId":214009,"progress":3},{"achieveId":413001,"progress":2}]','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/invasion/info/get',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'invasionId=%s'%'8','requestUtcTime=%s'%'0','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/tutorial/updatestep/4',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'category=%s'%'6','consumeId=%s'%self.consumeId,'drawNum=%s'%'10','gachaDrawId=%s'%'431','gachaDrawToken=%s'%self.gachaDrawToken,'gachaNo=%s'%'2','mode=%s'%'2','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		
	def finishTutorial(self):
		self.callAPI('/tkr/invasion/tutorial/getFinish',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/invasion/info/get',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'invasionId=%s'%'6','requestUtcTime=%s'%'0','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/invasion/tutorial/finish',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'descriptionIdsJson=%s'%'[73]','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/invasion/tutorial/finish',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'descriptionIdsJson=%s'%'[73,74,75]','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/invasion/tutorial/finish',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'descriptionIdsJson=%s'%'[73,74,75,76]','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/invasion/tutorial/finish',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'descriptionIdsJson=%s'%'[73,74,75,76,77]','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/invasion/tutorial/finish',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'descriptionIdsJson=%s'%'[73,74,75,76,77,78]','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/invasion/tutorial/finish',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'descriptionIdsJson=%s'%'[73,74,75,76,77,78,79]','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		self.callAPI('/tkr/invasion/tutorial/finish',['accessKey=%s'%self.accessKey,'advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'descriptionIdsJson=%s'%'[73,74,75,76,77,78,79,80]','userId=%s'%self.userId,'uuid=%s'%self.uuid])
		
	def exportCode(self):
		code=self.callAPI('/tkr/inherit/getcode',['advertiseId=%s'%self.advertiseId,'consumeId=%s'%self.consumeId,'playerInfoJson=%s'%'{}','userId=%s'%self.userId,'uuid=%s'%self.uuid])['code']
		_str='user: %s code: %s'%(self.userId,code)
		self.log(_str)
		return _str

	def exportPlayer(self,export_file=None):
		character=[]
		dispatch=[]
		for x in self.havesssr:
			if x>1000:
				dispatch.append('%s x%s'%(self.ssr[x],self.havesssr[x]))
			else:
				character.append('%s x%s'%(self.ssr[x],self.havesssr[x]))
		#self.log('character:%s'%(character))
		#self.log('dispatch:%s'%(dispatch))
		self.save(','.join([self.consumeId,self.uuid,self.userId,self.deviceType,self.exportCode(),str(len(self.havesssr)),';'.join(character),';'.join(dispatch)])+'\n',export_file if export_file else 'users.csv')
	
	def ensure_unicode(self,v):
		if isinstance(v, str):
			v = v.decode('utf8')
		return unicode(v)

	def save(self,d,f):
		with io.open(f, 'a', encoding='utf8') as json_file:
			json_file.write('%s'%unicode(self.ensure_unicode(d)))
		
	def calcpostHash(self,data):
		data=data#.replace('[','').replace(']','').replace('{','').replace('}','').replace('"','').replace(':','')
		crc32=hex(zlib.crc32(data)& 0xffffffff).upper()
		crc32=crc32[2:-1].rstrip()
		return self.encode(crc32)

	def decode(self,data):
		return self.crypter.decode(data.replace('\'',''))
		
	def encode(self,data):
		return self.crypter.encode(data)
		
if __name__ == "__main__":
	a=API()
	a.reroll()