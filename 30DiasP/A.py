import os
os.system ("clear")



def alfa (text):
    text = text.lower()
    contar_t= text.count("t")
    contar_j= text.count("j")
    print(f"count_r: {contar_t} count_j: {contar_j}")
    return contar_t == contar_j

print (alfa("vargneyjjktgulktwrh"))

