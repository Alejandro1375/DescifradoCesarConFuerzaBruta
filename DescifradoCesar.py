alfabeto= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

cifrado="Si Cupdmzaplil Uikpwuis Icbwuwti lm Tmfpkw oi lmamtxmvilw cu xixms xzwbiñwupkw mu si opabwzpi g mu si nwztikpwu lm ucmabzw xipa. Sia bizmia acabiubpdia lm mabi puabpbckpwu xcjspki, icbwuwti g sipki awu si lwkmukpi, si pudmabpñikpwu g si lpncapwu lm si kcsbczi.Mu ms tculw ikilmtpkw ma zmkwuwkpli kwtw cui cupdmzaplil lm mfkmsmukpi. Si CUIT zmaxwulm is xzmamubm g tpzi ms ncbczw kwtw ms xzwgmkbw kcsbczis tia ptxwzbiubm lm Tmfpkw.Si CUIT ma cu maxikpw lm spjmzbilma. Mu mssi am xzikbpki kwbplpiuitmubm ms zmaxmbw, si bwsmziukpi g ms lpiswñw. Si xsczisplil lm plmia g lm xmuaitpmubw ma ixzmkpili kwtw apñuw lm ac zpycmhi g ucuki kwtw nikbwz lm lmjpsplil."

for key in range(1, len(alfabeto)):
    mensaje=""

    for letra in cifrado.upper():
        if letra in alfabeto:
            indice= alfabeto.find(letra)
            indice -= key
            if indice < 0:
                indice += 27
            mensaje += alfabeto[indice]
        else:
            mensaje += letra

    print(f"Key: {key} - {mensaje}")