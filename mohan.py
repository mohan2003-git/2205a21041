import streamlit as st

def delta_to_star(R12, R23, R31):
    denominator = R12 + R23 + R31
    R1 = (R12 * R31) / denominator
    R2 = (R12 * R23) / denominator
    R3 = (R23 * R31) / denominator
    return R1, R2, R3
st.title("2205a21041")
st.title("DELTA to STAR")
st.write("input parameters for R12, R23, and R31 to calculate R1, R2, and R3.")

col1, col2 = st.columns([1, 1])

with col1:
    
    R12 = st.number_input("input parameters R12 (in ohms):", min_value=0.0, step=0.01)
    R23 = st.number_input("input parameters  R23 (in ohms):", min_value=0.0, step=0.01)
    R31 = st.number_input("input parameters  R31 (in ohms):", min_value=0.0, step=0.01)
    compute=st.button("compute")
with col2:
    
    if R12 > 0 and R23 > 0 and R31 > 0:
        R1, R2, R3 = delta_to_star(R12, R23, R31)
        st.subheader("output parameters:")
        st.write(f"R1 = {R1:.2f} Ω")
        st.write(f"R2 = {R2:.2f} Ω")
        st.write(f"R3 = {R3:.2f} Ω")
   