# christmas-countdown-bot

# ‼️ Aviso Importante
Caso você queira executar o código, certifique-se de atualizar todas as informações sensíveis antes de rodar, como:

- Seu número de telefone (para onde o SMS será enviado, campo to=)

- Número fornecido pelo Twilio (campo from_)

- SID da conta e Auth Token do Twilio

- Sem essas informações, o script não funcionará.


# 💾 Como transformar seu código em um arquivo .exe
1. Instale o PyInstaller
   
   - pode ser pelo terminal, usando "pip install pyinstaller"

2. Gere o executável
   
  - Dentro da pasta do arquivo .py, execute:  "pyinstaller --onefile nome_do_arquivo.py"

  - O --onefile cria apenas um único .exe, com tudo empacotado.

  - Caso queira esconder o terminal ao executar, use: "pyinstaller --onefile --noconsole nome_do_arquivo.py"

3. Encontre o arquivo executável

   - Depois de gerar o .exe o PyInstaller criará duas pastas:
   - build/
   - dist/
   - O arquivo exe estará disponivel na pasta dist

4. Agora configure no seu Agendador de Tarefas
   - Basta adicioná-lo ao Agendador de Tarefas do Windows e definir o horário da execução.


# 🎄 Notificador de Contagem Regressiva para o Natal
Este projeto é uma automação simples e divertida desenvolvida em Python que envia diariamente um SMS com a contagem regressiva em dias para o Natal.

Converti o script para .exe e configurado no Agendador de Tarefas do Windows, sendo executado automaticamente todos os dias às 14:50. Não é necessário abrir nada, a automação faz tudo sozinha.

# 🧑‍💻 O que o programa faz?

- Calcula quantos dias faltam para o Natal (25 de dezembro).
  
- Usa a API do Twilio para enviar um SMS automático para um número específico.

- Envia mensagens personalizadas de acordo com a data atual:
  
- Mais de 1 dia para o Natal → “Faltam X dias para o Natal!”

- 1 dia antes → “FALTA 1 DIA PARA O NATAL!!!”

- No dia de Natal → “HOJE TEM NATAL ÀS 00:00!!!”

- Depois do Natal → Caso você ainda deixe o programa funcionando ele informa quantos dias já passaram.

# 👨‍🔧 Como funciona tecnicamente

1. Pega a data atual usando datetime.now()

2. Calcula a diferença para o dia 25/12/2025

3. Monta a mensagem de acordo com os dias restantes

4. Usa o Twilio Client para enviar a mensagem como SMS

5. Foi convertido para .exe para rodar sem precisar abrir a sua IDE

6. Foi programado no Agendador de Tarefas para executar sozinho todo dia às 14:50.

#  🏛️ Arquitetura do meu projeto
Arquivo-programado.py  → Script principal

.exe gerado             → Versão executável do script principal

Agendador de Tarefas    →  Dispara o script diariamente

Twilio API              → Serviço que envia o SMS 

