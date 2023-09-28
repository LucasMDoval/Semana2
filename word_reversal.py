frase_input = str(input("Tu frase para invertir :"))
frase_list = frase_input.split(" ")
frase_list_reversed = reversed(frase_list)
frase_list_joined = " ".join(frase_list_reversed)

print(frase_list_joined)