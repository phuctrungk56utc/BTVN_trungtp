def travefile():
	with open("file_docx.txt", "r",encoding = "utf8") as f:
		file = f.read()
		stringth = file.lower().strip()
	f.close()
	return stringth
list_kq = travefile().lstrip("\ufeff")
print(list_kq)
fix = []
def XuLyChuoi(file):
	stringth = file.lower().strip()
	text = []
	x = 0
	solanrong = 0
	text.append("")
	for i in stringth:
		if (i != " ") and (i != "\n") and (i != "/") and (i != ".") and (i != "\\"):
			text[x] = text[x] + i
			solanrong = 0
			continue
		solanrong += 1
		if solanrong > 1:
			continue
		x = x + 1
		text.append("")
	return text
X = XuLyChuoi(list_kq)
print(X)

dem = []

def demchuoi(mang1,mang2):
	soluong = 1
	for i in range(len(mang1)):
		#dem tung thang
		for j in range(i+1,len(mang1)):
			if mang1[i] == mang1[j]:
				soluong += 1
		#aaaaaaaa
		if i == 0:
			mang2.append(soluong)
			soluong = 1
			continue
		if i == 1:
			if mang1[0] == mang1[1]:
				soluong = 1
				continue
		check = 1
		for k in range(i):
			if mang1[i] == mang1[k]:
				check = 0
		if check:
			mang2.append(soluong)
			soluong = 1
			check = 1
			continue
		soluong = 1
	return mang2
chuoisaukhidem = demchuoi(XuLyChuoi(list_kq),dem)
print(chuoisaukhidem)

def xoatrunglap(s): 
    if (len(s)) < 2: 
	    return s 
    result = []
    for i in s: 
    	if i not in result: 
		    result.append(i)
    return ''.join(result)
C = xoatrunglap(X)
print(C)

def ketquabaitoan(chuoiso,chuoichu):
	chuoichu2 = []
	for i in range(len(chuoiso)):
		for j in range(i+1,len(chuoiso)):
			if int(chuoiso[j]) > int(chuoiso[i]):
				tem = chuoiso[j]
				chuoiso[j] = chuoiso[i]
				chuoiso[i] = tem
				chuoichu2.append(chuoichu[j])
				continue
		chuoichu2.append(chuoichu[i])	
	print(chuoichu2)
	print(chuoiso)
	return chuoiso
maxxx = ketquabaitoan(chuoisaukhidem,C)

