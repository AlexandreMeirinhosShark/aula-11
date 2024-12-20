def num_of_letters(phrase, letter):
    count = 0
    final = ""
    if not letter == "todas":
        for x in phrase:
            if x == letter:
                count = count + 1
            final = f"{count} letras {letter.upper()}"
    else:
        for r in "abcdefghijklmnopqrstuvwxyz":
            for x in phrase:
                if x == r:
                    count = count + 1
            if not count == 0:
                final += f"{count} letras {r.upper()}, "
            count = 0
    return final


frase = input("Entre com a frase: ").lower()
letra = input("Qual letra deseja verificar? ").lower()

contar = num_of_letters(frase, letra)

print(f'A frase "{frase}" apresenta {contar}.')
