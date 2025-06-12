print (
    "===== CALCULADOR DE CALORIAS ====="
)

quantidade_de_refeicoes = int(input(
    "Digite a quantidade de refeicoes do dia: "
))

if quantidade_de_refeicoes < 1 or quantidade_de_refeicoes > 30: 
    print (
        "REFEICOES PERMITIDAS 0-30"
    )
    exit()
    
DEFINIR_LIMITE_CAL = int(input(
    "Digite o limite de cal do dia: "
))

if DEFINIR_LIMITE_CAL < 1 or DEFINIR_LIMITE_CAL > 300000: 
    print (
        "LIMITE DE CAL: 0-300.000"
    )
    exit()

print ("-=-"*10)

quantidade_ja_feitas = 0 

cal = []

while quantidade_ja_feitas < quantidade_de_refeicoes: 
    print (
        f"Refeição Numero: {quantidade_ja_feitas + 1}"
    )
    refeicao_proteinas = int(input(
        "Digite a quantidade de proteinas da refeição: "
    ))

    if refeicao_proteinas < 0 or refeicao_proteinas > 500: 
        print (
            "PROTEINA LIMITE: 0-500"
        )
        continue

    refeicao_gordura = int(input(
        "Digite a quantidade de gordura da refeição: "
    ))

    if refeicao_gordura < 0 or refeicao_proteinas > 500: 
        print (
            "GORDURA LIMITE: 0-500"
        )
        continue 

    refeicao_carboidratos = int(input(
        "Digite a quantidade de carboidrato da refeição: "
    ))

    if refeicao_carboidratos < 0 or refeicao_carboidratos > 500: 
        print (
            "CARBOIDRATO LIMITE: 0-500"
        )
        continue
    
    print ("-=-"*10)

    quantidade_ja_feitas += 1    

    cal_pro = refeicao_proteinas * 4

    cal_gor = refeicao_gordura * 9

    cal_car = refeicao_carboidratos * 4

    cal.append(cal_car)
    cal.append(cal_gor)
    cal.append(cal_pro)

resultado_cal = sum(cal)

cal_permitida = DEFINIR_LIMITE_CAL - resultado_cal

if cal_permitida > DEFINIR_LIMITE_CAL or cal_permitida < 0: 
    print (
        "CAL EXEDIDA, TENTE NOVAMENTE OUTRO DIA"
    )
    exit()

else: 
    print (
        f"CALORIA AINDA RESTANTE: {cal_permitida}"
        )