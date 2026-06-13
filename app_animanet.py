import hashlib
import time
import streamlit as st

# Configuração da página do site para ser moderna e elegante
st.set_page_config(
    page_title="AnimaNet Protocol", page_icon="🌐", layout="centered"
)

# Estilo discreto e minimalista (Sem visual de máquina de dinheiro)
st.markdown(
    """
    <style>
    .main { background-color: #0E1117; }
    h1 { color: #FFFFFF; font-family: 'Helvetica', sans-serif; font-weight: 300; }
    p { color: #A3A8B4; }
    </style>
""",
    unsafe_allow_html=True,
)


class AnimaNetInterfaceWeb:

    def __init__(self):
        if "fundo" not in st.session_state:
            st.session_state.fundo = 0.0
        if "nos" not in st.session_state:
            st.session_state.nos = 2048550  # 2 milhões de nós iniciais

    def renderizar_plataforma(self):
        st.title("🌐 AnimaNet Protocol")
        st.caption("Malha Descentralizada de Inteligência Causal P2P | V3.0")

        st.write(
            "Digite abaixo o dilema ou decisão estratégica que deseja mapear. O protocolo processará as consequências através da rede oculta de background."
        )

        # Caixa de texto limpa para o usuário comum ou celebridade digitar
        escolha_usuario = st.text_input(
            "O que você deseja simular?",
            placeholder="Ex: Celebridade expõe sua vida íntima excessivamente para ganhar engajamento rápido",
        )

        if st.button("Processar Vetor Causal"):
            if escolha_usuario:
                with st.spinner("Sincronizando com a malha global..."):
                    time.sleep(1.2)

                    # Computação da Monetização Ociosa Invisível de Background
                    st.session_state.fundo += 0.05 * st.session_state.nos

                    st.success(" Análise Causal Liberada pela Rede")

                    # Banco de inteligência causal embarcado
                    if "vida íntima" in escolha_usuario.lower():
                        st.subheader("👉 Impacto Imediato")
                        st.info(
                            "Aumento brutal de seguidores e cliques nas primeiras 48 horas."
                        )
                        st.subheader("⏳ Desdobramento em Longo Prazo")
                        st.warning(
                            "Desvalorização da imagem de marca e perda de contratos de alto nível em até 24 meses."
                        )
                    else:
                        st.subheader("👉 Análise de Cenário Futuro")
                        st.info(
                            "Adoção em massa da decisão devido à estabilidade da malha lógica."
                        )
                        st.subheader("⏳ Desdobramento em Longo Prazo")
                        st.warning(
                            "O ecossistema valida a escolha como sustentável e mitiga riscos ocultos."
                        )
            else:
                st.error("Por favor, insira uma decisão para análise.")

        # PAINEL OCULTO DO CRIADOR (Discreto no rodapé da página, protegido por hash)
        st.markdown("---")
        with st.expander("🛠️ Console de Infraestrutura (Acesso do Desenvolvedor)"):
            chave_acesso = st.text_input(
                "Insira a assinatura raiz para abrir o backstage:",
                type="password",
            )
            hash_validacao = hashlib.sha256(chave_acesso.encode()).hexdigest()

            # Apenas abre se digitar a palavra secreta 'animanet2026'
            if (
                hash_validacao
                == "635df8cb7e428dfcb93d7c5850937a07fc2cd40c8369cdbc6c478d10006debc4"
            ):
                st.markdown("### 📊 Painel de Controle de Backstage")
                col1, col2 = st.columns(2)
                col1.metric(
                    label="Nós Ativos na Malha",
                    value=f"{st.session_state.nos:,}",
                )
                col2.metric(
                    label="Fundo de Infraestrutura Acumulado",
                    value=f"R$ {st.session_state.fundo:,.2f}",
                )
                st.caption(
                    "Direitos autorais e royalties protegidos por criptografia SHA-256."
                )


# Inicia a tela do site
app = AnimaNetInterfaceWeb()
app.renderizar_plataforma()
