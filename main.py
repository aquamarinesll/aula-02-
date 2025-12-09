
login_salvo = "admin_ti"
senha_salva = "sistema@123"

#usuário
login_digitado = input ("Digite seu login:")
senha_digitada = input ("Digite sua senha:")

if login_digitado == login_salvo and senha_digitada == senha_salva:
    print ("Acesso Concedido. Bem-vindo ao Painel de Controle")

elif login_digitado == "guest" or senha_digitada == "123456":
    print ("Acesso Negado: Credenciais de baixo risco ou padrão de segurança.")

else:
print ("Erro de Acesso: Login ou senha inválidos.")