# Case Sequência x Classe

## Melhoria da View `usuario_view`

A classe foi melhorada visualmente sem alterar sua estrutura ou funcionamento, garantindo compatibilidade total com o restante do sistema.

### Principais melhorias

* **Organização visual**: uso de linhas (`=` e `-`) para separar seções
* **Ícones (emojis)**: interface mais amigável e intuitiva
* **Melhor formatação**: dados dos usuários mais alinhados e fáceis de ler
* **Feedback ao usuário**: mensagem quando não há usuários cadastrados
* **Títulos mais claros**: seções mais descritivas
* **Destaque de mensagens**: melhor visualização de avisos e ações
* **Entrada de dados destacada**: área de criação de usuário mais clara

---

### Resultado

✔ Interface mais bonita
✔ Melhor experiência no terminal
✔ Código continua simples e compatível

---

## Estrutura de Pastas
```
project/
 ├── controller/
 │   └── usuario_controller.py
 ├── service/
 │   └── usuario_service.py
 ├── repository/
 │   └── usuario_repository.py
 ├── model/
 │   └── usuario.py
 ├── view/
 │   └── usuario_view.py
 ├── db/
 │   └── database.py
 └── main.py
```

 ## Diagrama de Classes (PlantUML)
 <img width="334" height="539" alt="Diagrama de Classes (PlantUML)" src="https://github.com/user-attachments/assets/660376de-efdb-4622-b2b2-2577bdfdf6c4" />


 ## Diagrama de Sequência – Criar Usuário (PlantUML)

 <img width="814" height="531" alt="Diagrama de Sequência – Criar Usuário (PlantUML)" src="https://github.com/user-attachments/assets/82830338-04e3-4158-991d-af442a16fb4a" />

