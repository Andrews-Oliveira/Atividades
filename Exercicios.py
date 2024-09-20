class Exercicio1:
    def calcular_soma(self):
        indice = 13
        soma = 0
        k = 0
        while k < indice:
            k += 1
            soma += k
        return soma



class Exercicio2:
    def verificar_fibonacci(self, num):
        a, b = 0, 1
        while a <= num:
            if a == num:
                return True
            a, b = b, a + b
        return False


class Exercicio3:
    def calcular_faturamento(self, faturamento_mensal):
        faturamentos = [d["faturamento"] for d in faturamento_mensal if d["faturamento"] > 0]
        menor_faturamento = min(faturamentos)
        maior_faturamento = max(faturamentos)
        media_mensal = sum(faturamentos) / len(faturamentos)
        dias_acima_da_media = len([f for f in faturamentos if f > media_mensal])

        return {
            "menor_faturamento": menor_faturamento,
            "maior_faturamento": maior_faturamento,
            "dias_acima_da_media": dias_acima_da_media
        }


class Exercicio4:
    def calcular_percentual_faturamento(self, faturamento_estados):
        faturamento_total = sum(faturamento_estados.values())
        percentuais = {}
        for estado, valor in faturamento_estados.items():
            percentual = (valor / faturamento_total) * 100
            percentuais[estado] = percentual
        return percentuais


class Exercicio5:
    def inverter_string(self, s):
        invertida = ""
        for char in s:
            invertida = char + invertida
        return invertida



if __name__ == "__main__":

    ex1 = Exercicio1()
    print ("Exercicio 1")
    print("Soma:", ex1.calcular_soma())
    print ("")


    ex2 = Exercicio2()
    print("Exercicio 2")
    numero = int(input("Informe um número para verificar na sequência de Fibonacci: "))
    if ex2.verificar_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
    print ("")


    print("Exercicio 3")
    faturamento_mensal = [
        {"dia": 1, "faturamento": 1000.0},
        {"dia": 2, "faturamento": 0.0},
        {"dia": 3, "faturamento": 1500.0},
        {"dia": 4, "faturamento": 3000.0},
        {"dia": 5, "faturamento": 0.0},
        {"dia": 6, "faturamento": 2000.0},
        {"dia": 7, "faturamento": 2500.0}
    ]
    ex3 = Exercicio3()
    resultados = ex3.calcular_faturamento(faturamento_mensal)
    print(f"Menor faturamento: {resultados['menor_faturamento']}")
    print(f"Maior faturamento: {resultados['maior_faturamento']}")
    print(f"Dias com faturamento acima da média: {resultados['dias_acima_da_media']}")
    print("")


    print("Exercicio 4")
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    ex4 = Exercicio4()
    percentuais = ex4.calcular_percentual_faturamento(faturamento_estados)
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")
    print("")


    print("Exercicio 5")
    ex5 = Exercicio5()
    string = input("Digite uma string: ")
    print(f"String invertida: {ex5.inverter_string(string)}")
    print("")