chamado = {
"equipamento": "servidor principal",
"tempo_parado_horas": 5,
"setor": "financeiro",
"status": "aberto"
}

if chamado ["equipamento"] == "servidor principal" or chamado ["tempo_parado_horas"] > 4:
    prioridade = "P1 - critica"

elif chamado ["setor"] == "financeiro" and chamado ["tempo_parado_horas"]> 1:
    prioridade = "P2 - alta"

else:
    prioridade = "P3 - normal"

print (f"equipamento:{chamado['equipamento']}")
print (f"prioridade definida:{prioridade}")