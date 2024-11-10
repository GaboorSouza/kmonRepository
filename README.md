# Open de Boulder - Kmon de Escalada 🧗‍♂️

Aplicativo para gerenciamento de um campeonato de escalada, com funcionalidades de cadastro de participantes, registro de pontuação em boulders e exibição do ranking público. Desenvolvido em Python usando Streamlit para a interface, com armazenamento local em SQLite.

## Funcionalidades

- **Cadastro de Participantes**: Permite adicionar participantes com nome, categoria e sexo. Participantes também podem ser removidos.
- **Cadastro de Boulders**: Cadastra boulders com nome e pontuação base específica. Cada boulder pode ser removido individualmente.
- **Lançamento de Pontuação**: Registra a pontuação de cada participante em diferentes boulders, com opções de pontuação específicas: "Flash", "Cadena" e "Insucesso".
- **Ranking Público**: Exibe o ranking dos participantes de acordo com a pontuação acumulada, atualizado automaticamente a cada 10 segundos.

## Tecnologias Utilizadas

- **Python**
- **Streamlit**: Framework para a criação de interfaces web.
- **SQLite**: Banco de dados local.
- **streamlit-autorefresh**: Biblioteca para atualização automática do ranking.

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/GaboorSouza/kmonRepository/blob/main/app.py
   cd kmon-de-escalada

Uso
Cadastro de Participantes
Acesse a aba "Cadastro de Participantes".
Insira o Nome, Categoria e Sexo do participante.
Clique em "Adicionar Participante" para salvar.
A lista de participantes permite visualizar e remover qualquer participante cadastrado.

Cadastro de Boulder
Acesse a aba "Cadastro de Boulder".
Insira o Nome do Boulder e a Pontuação Base.
Clique em "Adicionar Boulder" para salvar.
A lista exibe os boulders com a opção de removê-los individualmente.

Lançamento de Pontuação
Acesse a aba "Lançamento de Pontuação".
Selecione um participante e um boulder.
Escolha o tipo de pontuação: Flash (pontuação completa), Cadena (pontuação completa - 200) ou Insucesso (0 pontos).
Clique em "Lançar Pontuação" para registrar.

Ranking Público
Acesse a aba "Ranking Público" para visualizar o ranking dos participantes, atualizado automaticamente a cada 10 segundos.# kmonRepository
