products = \
    ["Feijão Carioca", "Arroz Parboilizado", "Macarrão Espaguete", "Açúcar Cristal", "Flocão de Milho",
     "Óleo de Soja", "Café Tradicional", "Leite Integral", "Leite em Pó Integral", "Manteiga com Sal",
     "Margarina com Sal", "Ovos", "Frutas", "Legumes", "Creme Dental",
     "Sabonete", "Papel Higiênico", "Álcool em Gel"]

values = \
    [8.30, 5.96, 3.65, 4.13, 2.97,
     9.07, 6.29, 5.45, 8.16, 5.97,
     6.05, 8.00, 2.00, 2.00, 11.67,
     4.23, 7.07, 10.3]

listChosenProducts = []
listValuesChosenProducts = []

optionUserBoolean = True

while optionUserBoolean:
    print(
        "\n############ MENU ########### \n\n"
        "1 - Escolher Produto \n"
        "2 - Listar Produtos Escolhidos \n"
        "3 - Sair \n")

    optionUser = int(input("Digite uma opção: "))

    if 1 <= optionUser <= 2:
        if optionUser == 1:
            for counter in range(len(products)):
                print("{}: {} - R$ {}".format(str(counter + 1), products[counter], str(values[counter])))

            chosenProduct = int(input("\nInsira o código do produto desejado: "))

            if 1 <= chosenProduct <= 18:
                productQuantity = int(
                    input(
                        "\nVocê escolheu o produto " + products[
                            chosenProduct - 1] + ". Insira a quantidade desejada: "))

                valueSumQuantityProduct = productQuantity * values[chosenProduct - 1]

                listChosenProducts.append(products[chosenProduct - 1])
                listValuesChosenProducts.append(valueSumQuantityProduct)

                print("\n{} quantidade(s) de {} é R$ {:.2f}".format(productQuantity, products[chosenProduct - 1],
                                                                    valueSumQuantityProduct))
            else:
                print("\nINSIRA UM CÓDIGO VÁLIDO\n")

        else:
            for counter in range(len(listChosenProducts)):
                print("{}: {} {} - R$ {:.2f}".format(counter + 1, str(productQuantity), listChosenProducts[counter],
                                                     listValuesChosenProducts[counter]))

            print("\nO valor total da compra é R$ {:.2f}".format(sum(listValuesChosenProducts)))

    elif optionUser == 3:
        condition = int(input("\nRealmente deseja sair? \n"
                              "        1 - Sim \n"
                              "        2 - Não \n"
                              "Digite opção: "))

        if condition == 1:
            optionUserBoolean = False
    else:
        print("\nINSIRA UM NÚMERO VÁLIDO!\n")

print("\n############ PROGRAMA ENCERRADO ###########")
