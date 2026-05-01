class UsuarioView:

    def mostrar_menu(self):
        print("\n" + "=" * 40)
        print("        📋 MENU DE USUÁRIOS")
        print("=" * 40)
        print(" [1] ➜ Criar usuário")
        print(" [2] ➜ Listar usuários")
        print(" [0] ➜ Sair")
        print("=" * 40)

    def obter_dados_usuario(self):
        print("\n" + "-" * 40)
        print("        ✏️  NOVO USUÁRIO")
        print("-" * 40)
        nome = input("👤 Nome  : ")
        email = input("📧 Email : ")
        print("-" * 40)
        return nome, email

    def mostrar_usuarios(self, usuarios):
        print("\n" + "=" * 50)
        print("               👥 LISTA DE USUÁRIOS")
        print("=" * 50)

        if not usuarios:
            print("⚠️  Nenhum usuário cadastrado.")
        else:
            for u in usuarios:
                print(f"🆔 {u.id} | 👤 {u.nome} | 📧 {u.email}")

        print("=" * 50)

    def mostrar_mensagem(self, mensagem):
        print("\n" + "💬 " + mensagem)
