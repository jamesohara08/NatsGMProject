'''
This helper function takes a csv of player info and writes it into html buttons that can be used as player selectors in the code.
csv should have format
	Position (letter), Player (full name), 2019 Salary, 2019 Luxury Tax Value
'''
csv_in = "nats.csv"
html_out = "htmlelements.html"
with open(csv_in) as in_f:
	with open(html_out,"w") as out_f:
		header = True
		num = 0
		for line in in_f:
			if header:
				header = False
				continue
			row = line.strip("\n").split(",")
			out_f.write("<button class=\"btn btn-light\" id=\"p{0}\" onclick=\"addPlayer(p{0})\" data-name=\"{1}\" data-position=\"{2}\" data-salary=\"{3}\" data-luxury=\"{4}\">{2} | {1} | ${3:,} | ${4:,}</button>\n".format(num,row[1],row[0],int(float(row[2])*1000000),int(float(row[3])*1000000)))
			num += 1