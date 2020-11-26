#!usr/bin/env python
#
#<sixie6e@paracosmoclast>
#
#pseudolayout
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ezodf

class grocery():
	
	def __init__(self, name, years, parent):
		self.name = name
		self.years = years
		self.parent = parent
		self.employees = employees
		self.revenue = revenue
		
	kelloggs = ["cheez-it", "eggo", "town house", "pringles", "austin", "carr's", "morningstar farms", "plantation", "gardenburger", "bear naked", "natural touch", "kashi", "club", "pop tarts", "rxbar", "fruit winders", "e.l. fudge", "sunshine biscuits", "vienna fingers", "wheatables"] #2017 revenue: $12.93 billion USD

	general mills = ["betty crocker", "gold medal", "jus-rol", "pillsbury", "knack&back", "yoki", "bisquick", "cascadian farm", "haagen-dazs", "annie's", "* helper", "old el paso", "green giant", "wanchai ferry", "v.pearl", "epic", "immaculate baking", "liberte", "muir glen", "food should taste good", "larabar", "mountain high", "latina fresh", "blue buffalo", "totino's", "parampara", "yoplait"] #2017 revenue: $15.62 billion USD

	kraft-heinz = [heinz ketchup, kraft mac & cheese, lunchables, maxwell] #2017 revenue: $18.22 billion
	
	mondelez = ["cadbury", "nabisco", etc] #2017 revenue: $25.9 billion
	
	mars = [m&ms, snickers, dove, uncle ben’s] #2017 revenue: $35 billion


	coca-cola = [coca-cola, minute maid, glaceau] #2017 revenue: $35.41 billion

	unilever = [ben & jerry’s, klondike, popsicle, degree, vaseline] #2017 revenue: $62.62 billion


	procter&gamble = [pampers, tide, downy, charmin, gillette, crest] #2017 revenue: $65.06 billion


	pepsico = [pepsi, frito-lay, quaker, tropicana] #2017 revenue: $65.53 billion


	johnson&johnson = [aveeno, clean & clear, band-aid, tylenol] #2017 revenue: $76.45 billion


	nestle = [toll house, gerber, poland spring, stouffer’s] #2017 revenue: $89.79 billion

	ferrero spa = ["keebler", "famous amos", "nutella", "ferrara candy company", "ferrero kusschen", "ferrero rocher","hanuta", "kinder bueno", "kinder chocolate", "kinder joy", "kinder surprise", "mon cheri", "mother's cookies", "pocket coffee", "raffaello", "royal dansk", "thorntons", "tic tac"] #2017 revenue: $12.46 billion
	
	bc partners = ["petsmart", "chewy", "american journey"]
	
	kroger = ["", ""]
	
class vehicle():
	volkswagen group = [audi, bentley, bugatti, lamborghini, porsche, seat, skoda, volkswagen] #2017 revenue $272.21 billion

	toyota = [toyota, daihatsu, lexus] #2017 revenue $256.65 billion
	
	ford motor company = [ford, lincoln, troller] #2017 revenue $41.3 billion
	
	general motors = [cadillac, gmc, chevrolet, holden] #2017 revenue $145.58 billion
	
	renault-nissan-mitsubishi alliance = [renault, nissan, infiniti, dacia, datsun, samsung renault, lada, mitsubishi] #2017 revenue: $181.64 billion
	
	hyundai motor group = [hyundai, kia] #2017 revenue: $90.87 billion
	
	daimler ag = [mercedes-benz, smart, amg] #2017 revenue: $195.01 billion
	
	fiat chrysler automobiles = [alfa romeo, dodge, lancia, maserati, chrysler, fiat, jeep, ram] #2017 revenue: $131.62 billion
	
	honda = [honda, acura] #2017 revenue: $134.68 billion
	
	bmw = [bmw, mini, rolls royce] #2017 revenue: $117.12 billion
	
	suzuki = [suzuki, maruti suzuki] #2017 revenue: $30.52 billion
	
	groupe psa = [peugeot, ds automobiles, opel, citroen, vauxhall] #2017 revenue: $77.38 billion
	
	tata motors = [tata, jaguar, land rover] #2017 revenue: $41 billion
	
	geely = [lotus, proton, volvo] #2017 revenue: $14.13 billion
	
	independent = [ferrari $4.05B, aston martin $1.16B, subaru $32.02B, mazda $30.9B, tesla $11.76B, mclaren $1.15B]


class media():
	
	comcast = ["nbc", "universal filmed entertainment group", "sky studios", "dwa television", "cozi tv", "telemundo", "telexitos", "nhl", "back lot music", "peacock", "xfinity", "fandango", "xumo". "now tv", "]
	
	disney = ["abc", "disney studios", "utv motion pictures", "it's a laugh", "fx", "freeform productions", "marvel tv", "lwn", "rtl", "rtl2", "a&e", "fox nets group", "natgeo net", "espn", "abc radio", "fox music", "radio disney", "national geographic", "lucasarts"]
	
	national_amusements = ["cbs", "viacom", "paramount", "nickelodeon", "cbs", "the cw(50%)", "decades", "viacom dmn", "comedy central", "nick records", "cbs records", "simon & schuster", "pluto", "bet", "noggin", "showtime"]
	
	charter communications = ["spectrum", "time warner cable"]
	
	at_t =  ["time warner", "warner bros", "new line cinema", "wb", "cartoon network", "chilevision", "the cw(50%)", "tbs", "tnt", "trutv", "hbo", "cnn", "turner sports". "mlb", "nba", "watertower", "dc comics", "mad magazine", "boomerang", "crunchyroll", "rooster teeth"]
	
	thomson reuters = ["", ""]
		  
	bertelsmann = ["penguin", "random house"]
		   
	viacomCBS = ["", ""]
		   
	hasbro = ["", ""]
		   
	access_industries = ["", ""]
		   
	discovery_inc = ["", ""]

class retail():
	
	lowes = ["", ""]
	
	walmart = ["", ""]
	
	costco = ["", ""]
	
	amazon = ["", ""]
	
	home_depot = ["", ""]
	
	target = ["", ""]
	
	tjx = ["", ""]
	
	best_buy = ["", ""]
	
	albertsons = ["", ""]
	
	publix = ["", ""]
	
	apple = ["", ""]
	
	microsoft = ["", ""]
	
	macys = ["", ""]
	
	heb = ["", ""]
	
	dollar_general = ["", ""]
	
	dollar_tree = ["", ""]
	
	family_dollar = ["", ""]
	
	kohls = ["", ""]
	
	sears = ["", ""]
	
	whole_foods = ["", ""]
	
	rite-aid = ["", ""]
	
	gap = ["", ""]
	
	nordstom = ["", ""]
	
	ross = ["", ""]
	
	bjs = ["", ""]
	
	l_brands= ["", ""]
	
	jc_penney = ["", ""]
	
	bed_bath_beyond = ["", ""]
	
	autozone = ["", ""]
	
	nike = ["", ""]
	
	qurate = ["", ""]
	
	dollar_tree = ["", ""]
	
	family_dollar = ["", ""]
	
	kohls = ["", ""]

class banks():
	banks = ezodf.opendoc("/home/sixie6e/Documents/corporate_mapping/banks.ods")
		   
#industry = {type:brand}

agriculture_forestry = {
	'extermination0':'orkin',
	'extermination1':'a1',
	'farming_lstock':'heartland',
	'farming_crop':'dekalb',
	'fishing_hunting':'state',
	'landscaping':'earthworks'}
	
business_information = {
	'consultant':'the pyramid group llc',
	'daylabor':'laborready',
	'marketing':'829studios',
	'media0':media.comcast,
	'media1':media.national_amusements,
	'nonprofit':'boystown',
	'notary':'nps',
	'onlinebusiness':'ebay',
	'publishing':'harper collins',
	'recordproduction':'interscope',
	'retail0':retail.jc_penney,
	'retail1':retail.dollar_tree,}
	 
