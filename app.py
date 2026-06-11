import streamlit as st

# Oldal beállításai
st.set_page_config(page_title="Numerikus Módszerek - Tananyag", page_icon="📚", layout="centered")

st.title("📚 Numerikus Módszerek: Interaktív Tananyag")
st.markdown("Ezen az oldalon a numerikus módszerek alapfogalmait és a konvergencia rendjét sajátíthatod el.")

st.divider()

# Fülek (Tabs) létrehozása
tab1, tab2 = st.tabs(["📖 1. Előadás (Alapok)", "🔍 Konvergencia Rendje (p)"])

# ==========================================
# 1. FÜL: AZ EREDETI ANYAGOD
# ==========================================
with tab1:
    st.header("1. Algoritmusok és Stabilitás")
    with st.container():
        st.info("**Definíció: Numerikus algoritmus**\n\nA numerikus algoritmus aritmetikai és logikai műveletek véges sorozata.")
        st.info("**Definíció: Algoritmus stabilitása**\n\nA numerikus algoritmus stabil, ha létezik olyan C>0 konstans, hogy a kétféle B_1, B_2 bemenő adatból kapott K_1, K_2 kimenő adatokra teljesül a következő egyenlőtlenség:")
        st.latex(r"||K_{1}-K_{2}||\le C\cdot||B_{1}-B_{2}||")

    st.divider()
    st.header("2. Lebegőpontos számok és Gépi számok")
    with st.container():
        st.info("**Definíció: Normalizált lebegőpontos szám**\n\nLegyen:")
        st.latex(r"m=\sum_{i=1}^{t}m_{i}\cdot2^{-i}, \quad \text{ahol } t\in\mathbb{N}, m_1 = 1, m_{i}\in\{0,1\}")
        st.markdown("Ekkor az alábbi alakú számot normalizált lebegőpontos számnak nevezzük:")
        st.latex(r"a=\pm m\cdot2^{k} \quad (k\in\mathbb{Z})")
        
        st.info("**Definíció: Gépi számok halmaza (M)**")
        st.latex(r"M(t,k^{-},k^{+}) = \left\{ a=\pm2^{k}\cdot\sum_{i=1}^{t}m_{i}\cdot2^{-i} : k^{-}\le k\le k^{+}, m_{i}\in\{0,1\}, m_{1}=1 \right\} \cup \{0\}")

    st.divider()
    st.header("3. Hibaszámítás és Hibaterjedés")
    with st.container():
        st.info("**Definíció: Input függvény (fl)**\n\nAz fl függvényt input függvénynek nevezzük, ha:")
        st.latex(r"fl(x) = \begin{cases} 0, & \text{ha } |x|<\epsilon_{0} \\ \tilde{x}, & \text{ha } \epsilon_{0}\le|x|\le M_{\infty} \end{cases}")
        
        st.success("**Tétel: Input hiba**\n\nMinden valós szám esetén:")
        st.latex(r"|x-fl(x)| \le \begin{cases} \epsilon_{0} \\ \frac{1}{2}|x|\cdot\epsilon_{1} \end{cases}")

        st.info("**Definíció: Hibák jellemzése**\n\nLegyen A egy pontos érték, a pedig egy közelítő értéke.")
        st.markdown("- **Pontos hiba:** $\\Delta a := A - a$")
        st.markdown("- **Abszolút hiba:** $|\\Delta a| := |A - a|$")
        st.markdown("- **Relatív hiba:** $\\delta a := \\frac{\\Delta a}{A} \\approx \\frac{\\Delta a}{a}$")

        st.success("**Tétel: Az alapműveletek hibakorlátai**")
        st.markdown("**Abszolút hibakorlátok:**")
        st.latex(r"\Delta_{a\pm b} = \Delta_{a} + \Delta_{b}")
        st.latex(r"\Delta_{a\cdot b} = |b|\cdot\Delta_{a} + |a|\cdot\Delta_{b}")
        st.latex(r"\Delta_{a/b} = \frac{|b|\cdot\Delta_{a} + |a|\cdot\Delta_{b}}{b^{2}}")
        st.markdown("**Relatív hibakorlátok:**")
        st.latex(r"\delta_{a\cdot b} = \delta_{a} + \delta_{b}")
        st.latex(r"\delta_{a/b} = \delta_{a} + \delta_{b}")

    st.divider()
    st.header("4. Függvényérték hibája és Kondíciószám")
    with st.container():
        st.success("**1. Tétel: A függvényérték hibája (Első deriválttal)**")
        st.latex(r"\Delta_{f(a)} = M_{1}\cdot\Delta_{a}")
        st.markdown("Ahol $M_{1}=max\\{|f^{\\prime}(\\xi)|\\}$")

        st.success("**2. Tétel: A függvényérték hibája (Második deriválttal)**")
        st.latex(r"\Delta_{f(a)} = |f^{\prime}(a)|\Delta_{a} + \frac{M_{2}}{2}\cdot\Delta_{a}^{2}")
        st.markdown("Ahol $M_{2}=max\\{|f^{\\prime\\prime}(\\xi)|\\}$")

        st.info("**Definíció: Kondíciószám**\n\nAz f függvény a-beli kondíciószámának az alábbi mennyiséget nevezzük:")
        st.latex(r"c(f,a) = \frac{|a||f^{\prime}(a)|}{|f(a)|}")

# ==========================================
# 2. FÜL: A KONVERGENCIA RENDJE (ÚJ ANYAG)
# ==========================================
with tab2:
    st.header("P-adrendű konvergencia")
    
    with st.container():
        st.info("**Definíció: p-adrendű konvergencia**\n\nAz (x_k) konvergens sorozat p-adrendben konvergens, ha:")
        st.latex(r"\lim_{k\to\infty} \frac{|x_{k+1} - x^*|}{|x_k - x^*|^p} = c > 0")
        
        st.markdown("""
        **Megjegyzések (emberi nyelven):**
        1. **$p$ egyértelmű és $p \ge 1$**: A módszernek fix sebességfokozata van. Ha kisebb lenne 1-nél, a hiba lépésről lépésre nőne!
        2. **Fokozatok (sebesség)**: 
            * $p=1$: Lineáris (sima gyaloglás, lassan feleződik a hiba)
            * $p=2$: Kvadratikus (rakétasebesség, a hiba a négyzetére zuhan, pl. Newton-módszer)
            * $1 < p < 2$: Szuperlineáris (arany középút)
        3. **Gyakorlati képlet**: A programozásban a limesz helyett egy egyszerűsített felső korlátot (legrosszabb esetet) használnak:
        """)
        st.latex(r"|x_{k+1} - x^*| \le M|x_k - x^*|^p")

    st.divider()
    
    # --- Interaktív Tesztelő ---
    st.subheader("🕵️‍♂️ Detektív Játék: Miért van a képletben a p?")
    st.markdown("Válaszd ki a tesztalanyt, majd próbálj rájönni, milyen sebességfokozaton pörög a gép! **Cél:** Állítsd be úgy a $p$ hatványt, hogy az alsó két dobozban az osztás (a $c$ konstans) eredménye ugyanaz a fix szám maradjon!")
    
    gep_tipus = st.selectbox(
        "Melyik algoritmust (gépet) szeretnéd tesztelni?", 
        ["Lineáris Gép (pl. Felező módszer)", "Kvadratikus Gép (pl. Newton-módszer)"]
    )
    
    # Adatok generálása a választott gép alapján
    e0 = 0.1 # Kezdeti hiba
    if gep_tipus == "Lineáris Gép (pl. Felező módszer)":
        e1, e2, e3 = 0.05, 0.025, 0.0125
        helyes_p = 1
    else:
        e1, e2, e3 = 0.01, 0.0001, 0.00000001
        helyes_p = 2
        
    st.markdown("**A gép által produkált hibák listája:**")
    st.code(f"1. lépés (Mai hiba):       {e0}\n2. lépés (Holnapi hiba):   {e1}\n3. lépés (Holnaputáni):    {e2}")
    
    teszt_p = st.slider("Tesztelem a nevezőt! Szerintem a gép p értéke ennyi:", min_value=1, max_value=3, value=1)
    
    # Osztás elvégzése
    osztas1 = e1 / (e0 ** teszt_p)
    osztas2 = e2 / (e1 ** teszt_p)
    
    st.markdown(f"**Osztás tesztelése $p={teszt_p}$ esetén (Holnapi hiba / Mai hiba a p-ediken):**")
    
    col1, col2 = st.columns(2)
    col1.metric(label="1. lépésből a 2.-ba", value=f"{osztas1:.4f}")
    col2.metric(label="2. lépésből a 3.-ba", value=f"{osztas2:.4f}")
    
    # Visszajelzés
    if osztas1 == osztas2:
        st.success(f"🎉 BINGO! A két eredmény azonos! Megtaláltad a gép igazi sebességét. Ez a gép $p={teszt_p}$ fokozatban működik!")
        if teszt_p == 2:
            st.balloons()
    else:
        st.error("❌ A számok ugrálnak, a gép nem ezen a fokozaton megy. Próbálj ki egy másik p értéket a csúszkán!")

st.markdown("---")
st.caption("Készült a Numerikus Módszerek vizsgafelkészüléshez.")