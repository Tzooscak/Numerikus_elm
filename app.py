import streamlit as st
import numpy as np

# --- 1. OLDAL BEÁLLÍTÁSAI ---
st.set_page_config(
    page_title="Numerikus Módszerek",
    page_icon="🧮",
    layout="wide"
)

def main():
    # --- 2. OLDALSÁV (NAVIGÁCIÓ) ---
    st.sidebar.title("🧮 Témakörök")
    
    # A te listád alapján kialakított menüpontok
    menu_options = [
        "🏠 Kezdőlap",
        "1️⃣ Nemlineáris egyenletek",
        "2️⃣ Polinom interpoláció",
        "3️⃣ Legkisebb négyzetek módszere",
        "4️⃣ Numerikus integrálás"
    ]
    
    choice = st.sidebar.radio("Válassz egy témát:", menu_options)
    
    st.sidebar.divider()
    st.sidebar.info("Készült a Numerikus módszerek vizsgakövetelményei alapján.")

    # --- 3. TARTALOM MEGJELENÍTÉSE ---

    # -- KEZDŐLAP --
    if choice == "🏠 Kezdőlap":
        st.title("Numerikus Módszerek Alkalmazás")
        st.write("Válassz a bal oldali menüből, hogy megtekintsd az adott témakör elméletét és interaktív példáit!")
        
        st.subheader("A tananyag tartalma:")
        st.markdown("""
        * **Nemlineáris egyenletek:** Fixpont iteráció, Banach-féle tétel, Newton-módszer.
        * **Interpoláció:** Lagrange- és Newton-féle alak.
        * **Legkisebb négyzetek:** Lineáris és nemlineáris regresszió alapjai.
        * **Integrálás:** Newton-Cotes, érintő, trapéz és Simpson formulák.
        """)

    # -- 1. TÉMA: NEMLINEÁRIS EGYENLETEK --
    elif choice == "1️⃣ Nemlineáris egyenletek":
        st.title("Nemlineáris egyenletek megoldása")
        
        tab1, tab2 = st.tabs(["Fixpont iterációk", "Newton-módszer"])
        
        with tab1:
            st.header("Fixpont iterációk és Kontrakció")
            st.write("A kontrakció fogalma és a Banach-féle fixponttétel az $[a; b]$ intervallumon.")
            # Példa képlet megjelenítésére Streamlitben
            st.latex(r"x_{k+1} = \Phi(x_k)")
            st.info("Ide jöhet az elméleti leírás és egy interaktív Python példa, ahol a felhasználó megadhatja az iterációk számát.")
            
        with tab2:
            st.header("Newton-módszer (Érintőmódszer)")
            st.write("Iteratív módszer a gyökkeresésre.")
            st.latex(r"x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}")
            # Ide jöhetne egy gomb, ami kiszámol egy lépést
            if st.button("Szimulálj egy iterációs lépést!"):
                st.success("Iteráció végrehajtva! (Itt majd a kódod fut le)")

    # -- 2. TÉMA: POLINOM INTERPOLÁCIÓ --
    elif choice == "2️⃣ Polinom interpoláció":
        st.title("Polinom interpoláció")
        st.write("Adott pontokra illeszkedő polinom keresése.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Lagrange-féle alak")
            st.write("Alappolinomok segítségével felírt interpoláció.")
            st.latex(r"L_n(x) = \sum_{i=0}^{n} y_i \cdot \ell_i(x)")
            
        with col2:
            st.subheader("Newton-féle alak")
            st.write("Osztott differenciákra épülő felírás.")
            st.latex(r"N_n(x) = f(x_0) + \sum_{i=1}^{n} f[x_0, \dots, x_i] \prod_{j=0}^{i-1} (x - x_j)")

    # -- 3. TÉMA: LEGKISEBB NÉGYZETEK --
    elif choice == "3️⃣ Legkisebb négyzetek módszere":
        st.title("Legkisebb négyzetek módszere")
        
        st.subheader("Fogalma")
        st.write("Túlhatározott egyenletrendszerek 'legjobb' közelítő megoldása, ahol a hibák négyzetösszege minimális.")
        
        st.subheader("Megoldási módszere")
        st.write("A normálegyenlet felírása:")
        st.latex(r"A^T A x = A^T b")
        
        st.info("Itt érdemes lenne egy interaktív grafikont (pl. `st.pyplot`) megjeleníteni, ami egy ponthalmazra egyenest illeszt.")

    # -- 4. TÉMA: NUMERIKUS INTEGRÁLÁS --
    elif choice == "4️⃣ Numerikus integrálás":
        st.title("Numerikus integrálás")
        st.write("Interpolációs típusú kvadratúra formulák.")
        
        # Egy harmonika (expander) a formulák részletezéséhez
        with st.expander("Newton-Cotes formulák és pontosságuk"):
            st.write("Az érintő, trapéz és Simpson formula alapjai.")
            
        st.subheader("Alapformulák")
        colA, colB, colC = st.columns(3)
        
        with colA:
            st.markdown("**Érintő (Középponti) formula**")
            st.latex(r"\approx (b-a)f\left(\frac{a+b}{2}\right)")
            
        with colB:
            st.markdown("**Trapéz formula**")
            st.latex(r"\approx \frac{b-a}{2}(f(a)+f(b))")
            
        with colC:
            st.markdown("**Simpson formula**")
            st.latex(r"\approx \frac{b-a}{6}\left(f(a)+4f\left(\frac{a+b}{2}\right)+f(b)\right)")
            
        st.divider()
        st.subheader("Összetett formulák és pontosságuk")
        st.write("A részintervallumokra bontott integrálási szabályok hibájának elemzése.")

if __name__ == "__main__":
    main()