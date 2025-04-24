import streamlit as st


st.set_page_config(page_title="Para ti 💖", page_icon="🌸", layout="centered")


audio_file = open('musica.mp3', 'rb')
st.audio(audio_file.read(), format='audio/mp3')


paginas = [
    "🌹 Hola mi vida, hago este mensaje para desearte mucha suerte en tu parcial. Quiero que sepas que estoy contigo en cada momento, aunque no esté ahí físicamente.",
    
    "🎶 Ve con toda, amor. Sé que te va a ir genial, porque te preparaste, porque eres inteligente y porque puedes con todo. Yo creo en ti con todo mi corazón.",

    "💪 Si en algún momento sientes duda, respira profundo y recuerda lo fuerte y capaz que eres. Tienes todo para brillar y triunfar amor.",

    "✨ Así que sonríe, confía en ti, y da lo mejor. Estoy aquí, mandándote todo mi amor y abrazos en pensamiento. ¡Tú puedes mi niña hermosa! 💖",

    "🌈 Eres la mujer más hermosa, fuerte y brillante que conozco. No hay reto que pueda contigo amor, porque tu corazón y tu mente son gigantes.",

    "💖 Te amo con todo lo que soy, y estaré aquí celebrando contigo, sabiendo que vas a salir de ese parcial con la frente en alto y una sonrisa de orgullo."
]


if "paso" not in st.session_state:
    st.session_state.paso = 0


st.markdown(f"<h2 style='text-align: center;'>{paginas[st.session_state.paso]}</h2>", unsafe_allow_html=True)


if st.session_state.paso < len(paginas) - 1:
    if st.button("Siguiente 👉"):
        st.session_state.paso += 1
        st.rerun()  # <- esta línea es la nueva
else:
    st.success("Fin del mensaje 💌. Espero que te haya gustado.")
