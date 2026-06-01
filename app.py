import streamlit as st

# Oldal beállításai
st.set_page_config(page_title="Numerikus Módszerek - Tananyag", page_icon="📚", layout="centered")

st.title("📚 Numerikus Módszerek: 1. Előadás")
st.markdown("Ezen az oldalon a numerikus módszerek alapfogalmait, a lebegőpontos számábrázolást és a hibaszámítás alaptételeit sajátíthatod el.")

st.divider()

# --- 1. Szekció: Algoritmusok ---
st.header("1. Algoritmusok és Stabilitás")

with st.container():
    st.info("**Definíció: Numerikus algoritmus**\n\nA numerikus algoritmus aritmetikai és logikai műveletek véges sorozata.")
    
    st.info("**Definíció: Algoritmus stabilitása**\n\nA numerikus algoritmus stabil, ha létezik olyan $C>0$ konstans, hogy a kétféle $B_1, B_2$ bemenő adatból kapott $K_1, K_2$ kimenő adatokra teljesül a következő egyenlőtlenség:")
    st.latex(r"||K_{1}-K_{2}||\le C\cdot||B_{1}-B_{2}||")

st.divider()

# --- 2. Szekció: Lebegőpontos számok ---
st.header("2. Lebegőpontos számok és Gépi számok")

with st.container():
    st.info("**Definíció: Normalizált lebegőpontos szám**\n\nLegyen:")
    st.latex(r"m=\sum_{i=1}^{t}m_{i}\cdot2^{-i}, \quad \text{ahol } t\in\mathbb{N}, m_1 = 1, m_{i}\in\{0,1\}")
    st.markdown("Ekkor az alábbi alakú számot normalizált lebegőpontos számnak nevezzük:")
    st.latex(r"a=\pm m\cdot2^{k} \quad (k\in\mathbb{Z})")
    
    st.info("**Definíció: Gépi számok halmaza ($M$)**")
    st.latex(r"M(t,k^{-},k^{+}) = \left\{ a=\pm2^{k}\cdot\sum_{i=1}^{t}m_{i}\cdot2^{-i} : k^{-}\le k\le k^{+}, m_{i}\in\{0,1\}, m_{1}=1 \right\} \cup \{0\}")

st.divider()

# --- 3. Szekció: Hibaszámítás ---
st.header("3. Hibaszámítás és Hibaterjedés")

with st.container():
    st.info("**Definíció: Input függvény ($fl$)**\n\nAz $fl: \mathbb{R}_{M}\rightarrow M$ függvényt input függvénynek nevezzük, ha:")
    st.latex(r"fl(x) = \begin{cases} 0, & \text{ha } |x|<\epsilon_{0} \\ \tilde{x}, & \text{ha } \epsilon_{0}\le|x|\le M_{\infty} \end{cases}")
    
    st.success("**Tétel: Input hiba**\n\nMinden $x\in\mathbb{R}_{M}$ esetén:")
    st.latex(r"|x-fl(x)| \le \begin{cases} \epsilon_{0} \\ \frac{1}{2}|x|\cdot\epsilon_{1} \end{cases}")

    st.info("**Definíció: Hibák jellemzése**\n\nLegyen $A$ egy pontos érték, $a$ pedig egy közelítő értéke.")
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

# --- 4. Szekció: Függvényértékek hibája ---
st.header("4. Függvényérték hibája és Kondíciószám")

with st.container():
    st.success("**1. Tétel: A függvényérték hibája (Első deriváltal)**\n\nHa $f\in C^{1}(k_{\Delta_{a}}(a))$, akkor:")
    st.latex(r"\Delta_{f(a)} = M_{1}\cdot\Delta_{a}")
    st.markdown("Ahol $M_{1}=max\\{|f^{\\prime}(\\xi)|:\\xi\\in k_{\\Delta_{a}}(a)\\}$")

    st.success("**2. Tétel: A függvényérték hibája (Második deriváltal)**\n\nHa $f\in C^{2}(k_{\Delta_{a}}(a))$, akkor:")
    st.latex(r"\Delta_{f(a)} = |f^{\prime}(a)|\Delta_{a} + \frac{M_{2}}{2}\cdot\Delta_{a}^{2}")
    st.markdown("Ahol $M_{2}=max\\{|f^{\\prime\\prime}(\\xi)|:\\xi\\in k_{\\Delta_{a}}(a)\\}$")

    st.info("**Definíció: Kondíciószám**\n\nAz $f$ függvény $a$-beli kondíciószámának az alábbi mennyiséget nevezzük:")
    st.latex(r"c(f,a) = \frac{|a||f^{\prime}(a)|}{|f(a)|}")

st.markdown("---")
st.caption("Készült a Numerikus Módszerek 1. előadásának anyaga alapján.")