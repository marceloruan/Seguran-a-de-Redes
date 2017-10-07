def encrypt(text, key):
	text_list = list(text)
	text_encrypt = ""
	for i in text_list:
		if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
			if (i >= 'a' and i <= 'z'):
				ord_c = (ord(i) - ord('a') + key) % 26
				text_encrypt += chr(ord_c + ord('a'))
			else:
				ord_c = (ord(i) - ord('A') + key) % 26
				text_encrypt += chr(ord_c + ord('A'))
		else:
			text_encrypt += i
	return text_encrypt

def decrypt(text, key):
	text_list = list(text)
	text_encrypt = ""
	for i in text_list:
		if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
			if (i >= 'a' and i <= 'z'):
				ord_c = (ord(i) - ord('a') - key) % 26
				text_encrypt += chr(ord_c + ord('a'))
			else:
				ord_c = (ord(i) - ord('A') - key) % 26
				text_encrypt += chr(ord_c + ord('A'))
		else:
			text_encrypt += i
	return text_encrypt


texto = raw_input("Digite uma palavra para criptograr ou decritografar: ")
chave = int(raw_input("Digite o deslocamento: "))
chave =chave-chave-chave
modo = int(raw_input("Digite 1 para Criptografar e 2 para Decritar: "))
if modo==1:
	print(encrypt(texto, chave))
	
if modo==2:		
	print(decrypt(texto, chave))

