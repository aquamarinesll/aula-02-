softwares_criticos = ["ERP", "banco de dados SQL","firewall"]
software_novo = input ("Digite o nome do novo software:")

if software_novo in softwares_criticos:
    print ("Atenção: Este software é crítico e já está instalado. Nenhuma alteração é necessária.")
else:
    print (f"Instalação iniciada para'{software_novo}'.")
    softwares_criticos.append(software_novo)


print ("Inventário atualizado de softares críticos:")
print (softwares_criticos)