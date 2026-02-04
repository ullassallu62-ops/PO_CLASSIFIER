import streamlit as st
import json
from classifier import classify_po

st.set_page_config(page_title="PO Category Classifier", layout="centered")

st.title("PO L1-L2-L3 Classifier")
st.caption("Paste a purchase order description and optionally add a supplier name.")

with st.sidebar:
    st.subheader("Tips")
    st.write(
        "Be specific: include item type, material, service type, and usage context."
    )
    st.write("Example: 3/8 in. stainless steel bolts, 500 count for assembly line")

with st.form("po_form", clear_on_submit=False):
    po_description = st.text_area(
        "PO Description",
        height=140,
        placeholder="Describe the item or service...",
    )
    supplier = st.text_input("Supplier (optional)", placeholder="Acme Industrial Co.")
    submitted = st.form_submit_button("Classify")

if submitted:
    if not po_description.strip():
        st.warning("Please enter a PO description.")
    else:
        with st.spinner("Classifying..."):
            result = classify_po(po_description, supplier)

        try:
            st.success("Classification complete.")
            st.json(json.loads(result))
        except Exception:
            st.error("Invalid model response")
            st.text(result)
