sisalto = []
try:
    with open('sanoja.txt', 'r') as f:
        sisalto = f.readlines()
        sisalto = [sana.strip() for  sana in sisalto]

except IOError:
	print("Virheellinen tiedostonnimi")
	
sisalto.sort()
print("Sanat laitettuna aakkosjärjestykseen:")
#print(sisalto)
for sanat in sisalto:
	print(sanat)
	