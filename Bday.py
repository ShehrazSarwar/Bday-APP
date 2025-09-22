import streamlit as st
import time

# Configure page
st.set_page_config(
    page_title="🎉 Birthday Wishes 🎉",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for black theme and proper layout
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

    /* Hide empty containers and fix layout */
    .element-container:empty {
        display: none !important;
    }

    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }

    /* Main app background - Black theme */
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
        background-attachment: fixed;
        color: white;
    }

    /* Title styling */
    .birthday-title {
        font-size: clamp(2.5rem, 6vw, 4.5rem);
        font-weight: 800;
        background: linear-gradient(135deg, #ff6b6b, #4ecdc4, #45b7d1, #ffd93d);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        background-clip: text;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        font-family: 'Poppins', sans-serif;
        line-height: 1.2;
    }

    /* Subtitle styling */
    .birthday-subtitle {
        font-size: clamp(1.1rem, 3vw, 1.6rem);
        color: #e0e0e0;
        margin-bottom: 3rem;
        font-weight: 400;
        line-height: 1.5;
        font-family: 'Poppins', sans-serif;
    }

    /* Main container (centered horizontally, top aligned) */
    .main-birthday-container {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;   /* top */
        align-items: center;           /* horizontal center */
        text-align: center;
        padding-top: 50px;
    }

    /* Force Streamlit button to center */
    div.stButton {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
    }

    /* Birthday message styling */
    .birthday-message {
        background: linear-gradient(135deg, rgba(30,30,30,0.95) 0%, rgba(40,40,40,0.95) 100%);
        border-radius: 25px;
        padding: 2.5rem;
        margin: 2rem 0;
        color: #f0f0f0;
        font-size: clamp(1rem, 2.5vw, 1.2rem);
        line-height: 1.8;
        border: 2px solid rgba(78, 205, 196, 0.3);
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        animation: slideInUp 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-align: left;
        font-family: 'Poppins', sans-serif;
    }

    .birthday-message h2 {
        color: #ff6b6b;
        font-size: clamp(1.5rem, 4vw, 2.2rem);
        margin-bottom: 1.5rem;
        text-align: center;
        font-weight: 700;
        font-family: 'Poppins', sans-serif;
    }

    .birthday-message p {
        margin-bottom: 1.2rem;
        color: #e0e0e0;
    }

    .birthday-message .final-wish {
        font-size: clamp(1.1rem, 3vw, 1.4rem);
        font-weight: 600;
        color: #4ecdc4;
        text-align: center;
        margin-top: 2rem;
        padding: 1.5rem;
        background: rgba(78, 205, 196, 0.15);
        border-radius: 15px;
        border: 1px solid rgba(78, 205, 196, 0.3);
    }

    /* Fix Streamlit button style */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%) !important;
        border: 2px solid rgba(255,255,255,0.2) !important;
        border-radius: 60px !important;
        padding: 20px 40px !important;
        font-size: clamp(1.1rem, 3vw, 1.3rem) !important;
        font-weight: 700 !important;
        color: white !important;
        font-family: 'Poppins', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        box-shadow: 0 15px 35px rgba(255, 107, 107, 0.4) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }

    div.stButton > button:hover {
        transform: translateY(-5px) scale(1.05) !important;
        box-shadow: 0 20px 40px rgba(255, 107, 107, 0.6) !important;
        background: linear-gradient(135deg, #ff5252 0%, #26c6da 100%) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Session state ---
if 'show_surprise' not in st.session_state:
    st.session_state.show_surprise = False
if 'show_balloons' not in st.session_state:
    st.session_state.show_balloons = False
if 'music_started' not in st.session_state:
    st.session_state.music_started = False

# --- Main container ---
st.markdown('<div class="main-birthday-container">', unsafe_allow_html=True)

st.markdown("""
<style>
.birthday-title {
    text-align: center;
    font-size: 3rem;
    margin-bottom: 0.5rem;
}

.birthday-subtitle {
    text-align: center;
    font-size: 1.5rem;
    margin-top: 0;
}
</style>
""", unsafe_allow_html=True)

# Title + Subtitle
st.markdown("""
<h1 class="birthday-title">🎉 Happy Birthday!🎂</h1>
<p class="birthday-subtitle">Hope your special day is filled with happiness, joy, and wonderful memories!✨</p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2.5, 1])  # middle column is wider
with col2:
    if st.button("🎈 Click Here for a Surprise! 🎈", key="surprise_btn", help="Something magical awaits..."):
        st.session_state.show_surprise = True
        st.session_state.show_balloons = True
        st.session_state.music_started = True
        st.rerun()

# Music
if st.session_state.music_started:
    st.markdown("""
    <audio autoplay loop>
        <source src="https://townsquare.media/site/189/files/2012/11/onedirection-littlethings-1.mp3" type="audio/wav">
    </audio>
    """, unsafe_allow_html=True)

# Surprise Content
if st.session_state.show_surprise:
    st.markdown("""
    <div class="birthday-message">
        <h2>🌟 A Special Birthday Message Just for You! 🌟</h2>
        <p>
            Today marks another year of your incredible journey through life, and what a beautiful journey it has been! 
            As you blow out the candles on your cake, remember that each flame represents a wish, a dream, and all the 
            amazing experiences that await you in the year ahead.
        </p>
        <p>
            May this new chapter bring you endless laughter, unforgettable adventures, and moments that make your heart 
            sing with joy. You deserve all the happiness in the world because you bring so much light and positivity 
            to everyone around you.
        </p>
        <p>
            Here's to celebrating YOU today - your kindness, your strength, your unique spirit, and all the wonderful 
            ways you make this world a brighter place. May your birthday be as extraordinary as you are!
        </p>
        <div class="final-wish">
            🎊 Wishing you the happiest of birthdays and a year filled with endless blessings! 🎊
        </div>
    </div>
    """, unsafe_allow_html=True)

# Balloons
if st.session_state.show_balloons:
    st.balloons()
    time.sleep(5)
    st.session_state.show_balloons = False
    st.rerun()

# Close main container
st.markdown('</div>', unsafe_allow_html=True)
