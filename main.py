teksts = input("Ievadit tekstu: ")
def deletE(teksts):
  if teksts.count("e") > 0:
    teksts = teksts.replace("e", " ")
    teksts = teksts.upper()
    print(teksts)
  else:
    teksts = "Teksts nesatur vajadzīgo burtu."
    print(teksts)
  return(teksts)
deleteE(teksts)