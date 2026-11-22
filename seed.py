from models import SessionLocal, Viatura

def popular_banco():
    # Abre a sessão com o banco
    session = SessionLocal()

    # Verifica se o banco já tem viaturas para não duplicar toda vez que rodar
    if session.query(Viatura).count() > 0:
        print("O banco já possui viaturas cadastradas!")
        session.close()
        return

    # Gerando 30 viaturas de teste
    for i in range(1, 31):
        # Formatando o número para ter sempre 2 dígitos (ex: 01, 02... 10... 30)
        numero_formatado = f"{i:02d}"
        
        nova_viatura = Viatura(
            prefixo=f"VTR-{numero_formatado}",
            modelo="Toyota Hilux" if i % 2 == 0 else "Ford Ranger", # Varia o modelo
            placa=f"ABC-{1000 + i}" # Gera placas tipo ABC-1001, ABC-1002...
        )
        session.add(nova_viatura)

    # Salva tudo no banco
    session.commit()
    session.close()
    print("30 viaturas cadastradas com sucesso no banco!")

if __name__ == "__main__":
    popular_banco()