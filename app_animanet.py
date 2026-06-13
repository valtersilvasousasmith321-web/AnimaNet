import hashlib
import time
import os
import streamlit as st
from google import genai

# Configuração da página do site para ser moderna e elegante
st.set_page_config(
    page_title="AnimaNet Protocol", page_icon="⚫", layout="centered"
)

# Estilo discreto e minimalista
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
           
        # Pega a chave direto do sistema do Streamlit Cloud de forma oculta
        self.api_key = st.secrets.get("GEMINI_API_KEY") if "GEMINI_API_KEY" in st.secrets else os.environ.get("GEMINI_API_KEY")
       
        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
        else:
            self.client = None

    def chamar_ia(self, prompt_sistema, dilema):
        if not self.client:
            return "❌ Erro de Segurança: Chave não detectada nas configurações (Secrets) do Streamlit."
        try:
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=f"{prompt_sistema}\n\nCenário: {dilema}"
            )
            return response.text
        except Exception as e:
            return f"Erro na IA: {str(e)}"

    def renderizar_plataforma(self):
        st.title("⚫ AnimaNet Protocol")
       
        st.markdown("""
        Digite abaixo o dilema ou decisão estratégica que deseja mapear. O protocolo processará as
        consequências através da rede oculta de background.
        """)
       
        exemplo_texto = "Celebridade expõe sua vida íntima excessivamente para ganhar engajamento rápido"
        dilema_input = st.text_area("O que você deseja simular?", value=exemplo_texto, height=100)
       
        if st.button("Processar Vetor Causal"):
            if not dilema_input.strip():
                st.error("Por favor, digite um dilema válido.")
                return
               
            with st.spinner("Processando vetor causal pela rede oculta..."):
                time.sleep(1) # Simula o tempo de rede
               
                # Bloco 1: Análise Causal
                p1 = "Você é um nó supervisor da malha causal AnimaNet. Faça uma 'Análise Causal Liberada pela Rede' em tópicos curtos, focando nas causas e efeitos imediatos."
                st.subheader("🌐 Análise Causal Liberada pela Rede")
                st.info(self.chamar_ia(p1, dilema_input))
               
                # Bloco 2: Cenário Futuro
                p2 = "Você é um nó de projeção. Faça uma 'Análise de Cenário Futuro' realista sobre como o ecossistema reage a essa decisão a médio prazo."
                st.subheader("📂 Análise de Cenário Futuro")
                st.success(self.chamar_ia(p2, dilema_input))
               
                # Bloco 3: Longo Prazo
                p3 = "Você é o validador de longo prazo. Faça um 'Desdobramento em Longo Prazo' explicando se essa escolha é sustentável e quais os riscos ocultos."
                st.subheader("⏳ Desdobramento em Longo Prazo")
                st.warning(self.chamar_ia(p3, dilema_input))

if __name__ == "__main__":
    app = AnimaNetInterfaceWeb()
    app.renderizar_plataforma()
