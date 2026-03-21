
def encryption(txt):
	txt = txt.replace(" ", "")
	L = len(txt)
	rows = int(L**0.5)
	cols = rows if rows*rows >= L else rows + 1
	encriptedMsg = []
	for i in range(rows):
		encriptedMsg.append([])
		for j in range(cols):
			if j + i*cols < L:
				encriptedMsg[i].append(txt[j + (i)*cols])
			else:
				encriptedMsg[i].append("")
	columns =  [list(row) for row in zip(*encriptedMsg)]
	return " ".join("".join(col) for col in columns)


print(encryption("haveaniceday")== "hae and via ecy")
print(encryption("feedthedog")== "fto ehg ee dd")
print(encryption("chillout")== "clu hlt io")
print(encryption("A Fool and His Money Are Soon Parted.")== "Anoea FdnSr oHeot oiyoe lsAnd aMrP.")
print(encryption("One should not worry over things that have already happened and that cannot be changed.")== "Onvtlphb. noehreae etraentc swttaech hohhddaa oriayann urnvhnng lygeadoe dosapttd")
print(encryption("Back to Square One is a popular saying that means a person has to start over, similar to: back to the drawing board.")== "Brpgatroea aeutpo,:dr cOlhessbrd knaartiaa. tertsamcw oismoriki Ssaentltn qayahoaog upinavrtb aonssetho")

