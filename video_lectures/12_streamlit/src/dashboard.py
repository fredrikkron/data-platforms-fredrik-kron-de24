import streamlit as st
from kpis import approved_percentage, number_approved, total_applications, provider_kpis
from read_data import read_data
from charts import approved_by_area_bar

df = read_data()


def layout():
    st.markdown("# YH dashboard 2024 applications")

    st.markdown(
        "This is a simple dashboard about higher vocational education in Sweden (yrkeshögskola). The results from the education can be filtered in this dashboard."
    )

    st.markdown("## KPIs in Sweden")

    labels = ("total applications", "number approved", "approved percentage")

    cols = st.columns(3)

    kpis = (total_applications, number_approved, approved_percentage)

    for col, label, kpi in zip(cols, labels, kpis):
        with col:
            st.metric(label=label, value=kpi)

    st.markdown("## Approved by area")
    
    approved_by_area_bar()

    st.markdown("## Simple statictics on a given provider")

    st.markdown("Search for an educational provider")

    provider = st.selectbox(
        "Choose educational provider",
        df["Utbildningsanordnare administrativ enhet"].unique(),
    )

    provider_applications, provider_approved = provider_kpis(provider)

    st.markdown(
        f"This education provider {provider} has applied for {provider_applications} educations and gotten {provider_approved} educations approved"
    )

    st.markdown("## Raw data")

    st.dataframe(df)


if __name__ == "__main__":
    layout()
