# app.py
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from database import (adicionar_usuario, listar_usuarios, adicionar_boulder, 
                      listar_boulders, adicionar_pontuacao, listar_pontuacoes_por_usuario,
                      calcular_ranking, verificar_nome_existente, verificar_boulder_existente,
                      atualizar_pontuacao, remover_pontuacao, remover_usuario, remover_boulder)

st.title("Open de Boulder - Kmon de escalada")

# Opções de pontuação
TIPOS_PONTUACAO = ["Flash", "Cadena", "Insucesso"]

# Opções de categoria
CATEGORIAS = [""] + [
    "Infantil A", "Infantil B", "Juvenil A", "Juvenil B",
    "Juvenil C", "Junior", "Iniciante", "Amador", "Pro", "Master"
]

# Opções de Sexo
SEXO = [""] + ["Masculino", "Feminino"]

# Barra lateral para navegação
menu = st.sidebar.selectbox("Menu", ["Ranking Público", "Cadastro de Participantes", "Cadastro de Boulder", "Lançamento de Pontuação"])

if menu == "Cadastro de Participantes":
    st.header("Cadastro de Participantes")
    
    # Formulário de cadastro de participantes
    with st.form("adicionar_usuario"):
        nome = st.text_input("Nome")
        categoria = st.selectbox("Categoria do Participante", CATEGORIAS, index=0)
        sexo = st.selectbox("Sexo", SEXO, index=0)
        submit = st.form_submit_button("Adicionar Participante")
        
        # Validação e cadastro
        if submit:
            if not nome:
                st.error("O campo Nome é obrigatório.")
            elif categoria == "":
                st.error("Selecione uma categoria para o participante.")
            elif sexo == "":
                st.error("Selecione o sexo.")
            elif verificar_nome_existente(nome):
                st.error("Esse nome já está cadastrado. Tente um nome diferente.")
            else:
                adicionar_usuario(nome, categoria, sexo)
                st.success("Participante adicionado com sucesso!")
    
    # Exibir a lista de participantes com opção de remover
    st.subheader("Lista de Participantes")
    usuarios = listar_usuarios()
    for usuario in usuarios:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"ID: {usuario[0]} | Nome: {usuario[1]} | Sexo: {usuario[3]} | Categoria: {usuario[2]}")
        with col2:
            if st.button("Remover", key=f"remover_usuario_{usuario[0]}"):
                remover_usuario(usuario[0])
                st.warning("Participante removido.")


elif menu == "Cadastro de Boulder":
    st.header("Cadastro de Boulder")
    
    # Formulário de cadastro de boulders com campo de pontuação
    with st.form("adicionar_boulder"):
        nome_boulder = st.text_input("Nome do Boulder")
        pontuacao_boulder = st.number_input("Pontuação Base do Boulder", min_value=0, step=1)  # Novo campo de pontuação base
        submit_boulder = st.form_submit_button("Adicionar Boulder")
        
        # Validação e cadastro
        if submit_boulder:
            if not nome_boulder:
                st.error("O campo Nome do Boulder é obrigatório.")
            elif verificar_boulder_existente(nome_boulder):
                st.error("Esse boulder já está cadastrado. Tente um nome diferente.")
            else:
                adicionar_boulder(nome_boulder, pontuacao_boulder)
                st.success("Boulder adicionado com sucesso!")
    
    # Exibir a lista de boulders com opção de remover
    st.subheader("Lista de Boulders")
    boulders = listar_boulders()
    for boulder in boulders:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"ID: {boulder[0]}, Nome: {boulder[1]}, Pontuação Base: {boulder[2]}")
        with col2:
            if st.button("Remover", key=f"remover_boulder_{boulder[0]}"):
                remover_boulder(boulder[0])
                st.warning("Boulder removido.")

elif menu == "Lançamento de Pontuação":
    st.header("Lançamento de Pontuação")
    
    # Listar participantes e boulders
    usuarios = listar_usuarios()
    boulders = listar_boulders()
    
    if usuarios and boulders:
        # Selecionar o participante
        usuario_id = st.selectbox("Selecionar Participante", [user[0] for user in usuarios], format_func=lambda x: [u[1] for u in usuarios if u[0] == x][0])

        # Formulário para adicionar nova pontuação
        st.subheader("Adicionar Nova Pontuação")
        boulder_id = st.selectbox("Selecionar Boulder", [b[0] for b in boulders], format_func=lambda x: [b[1] for b in boulders if b[0] == x][0])
        tipo_pontuacao = st.selectbox("Tipo de Pontuação", TIPOS_PONTUACAO)
        
        if st.button("Lançar Pontuação"):
            adicionar_pontuacao(usuario_id, boulder_id, tipo_pontuacao)
            st.success("Pontuação adicionada com sucesso!")
        
        # Listar pontuações do participante selecionado abaixo do botão
        st.subheader("Pontuações do Participante")
        pontuacoes = listar_pontuacoes_por_usuario(usuario_id)
        if pontuacoes:
            for pontuacao in pontuacoes:
                col1, col2 = st.columns([6, 2])  # Ajusta as colunas para remover o botão Editar
                with col1:
                    st.write(f"Boulder: {pontuacao[1]}, Tipo: {pontuacao[2]}")
                with col2:
                    if st.button("Remover", key=f"remover_{pontuacao[0]}"):
                        remover_pontuacao(pontuacao[0])
                        st.warning("Pontuação removida.")
        else:
            st.info("Nenhuma pontuação registrada para este participante.")
    else:
        st.warning("Cadastre pelo menos um participante e um boulder antes de lançar pontuação.")

# Intervalo de atualização automática em milissegundos
intervalo_atualizacao = 10000  # 10 segundos

if menu == "Ranking Público":
    st.header("Ranking de Participantes")
    
    # Configura a atualização automática a cada 10 segundos
    st_autorefresh(interval=intervalo_atualizacao, limit=None, key="ranking_refresh")
    
    # Exibe o ranking
    ranking = calcular_ranking()
    
    if not ranking.empty:
        st.table(ranking)
    else:
        st.info("Nenhum participante ou pontuação registrada.")
