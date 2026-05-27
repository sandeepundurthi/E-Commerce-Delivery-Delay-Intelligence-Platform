import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from sqlalchemy import create_engine

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="E-Commerce Delivery Intelligence",
    page_icon="📦",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("📦 E-Commerce Delivery Delay Intelligence System")
st.write(
    "Operations analytics dashboard for shipment delay analysis, "
    "logistics performance monitoring, and delivery risk prediction."
)

# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------
DB_USER = "sandeepundurthi"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ecommerce_delay_db"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

@st.cache_data
def load_data():
    query = "SELECT * FROM shipment_data"
    return pd.read_sql(query, engine)

df = load_data()

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------
st.sidebar.header("🔍 Filters")

selected_warehouse = st.sidebar.multiselect(
    "Warehouse",
    options=sorted(df["warehouse_block"].unique()),
    default=sorted(df["warehouse_block"].unique())
)

selected_mode = st.sidebar.multiselect(
    "Shipment Mode",
    options=sorted(df["mode_of_shipment"].unique()),
    default=sorted(df["mode_of_shipment"].unique())
)

selected_importance = st.sidebar.multiselect(
    "Product Importance",
    options=sorted(df["product_importance"].unique()),
    default=sorted(df["product_importance"].unique())
)

filtered_df = df[
    (df["warehouse_block"].isin(selected_warehouse)) &
    (df["mode_of_shipment"].isin(selected_mode)) &
    (df["product_importance"].isin(selected_importance))
]

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------
st.markdown("## 📊 Operational KPIs")

total_orders = len(filtered_df)
delay_rate = filtered_df["is_delayed"].mean() * 100
on_time_rate = 100 - delay_rate
avg_weight = filtered_df["weight_in_gms"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("📦 Total Orders", f"{total_orders:,}")
col2.metric("⚠️ Delay Rate", f"{delay_rate:.2f}%")
col3.metric("✅ On-Time Rate", f"{on_time_rate:.2f}%")
col4.metric("🏋️ Avg Package Weight", f"{avg_weight:.0f} g")

st.divider()

# --------------------------------------------------
# DELIVERY STATUS PIE CHART
# --------------------------------------------------
st.markdown("## 🚚 Delivery Status Overview")

delay_counts = filtered_df["is_delayed"].value_counts().reset_index()
delay_counts.columns = ["Status", "Count"]

delay_counts["Status"] = delay_counts["Status"].map({
    0: "On-Time",
    1: "Delayed"
})

fig_pie = px.pie(
    delay_counts,
    names="Status",
    values="Count",
    title="Shipment Delivery Status",
    hole=0.4
)

st.plotly_chart(fig_pie, use_container_width=True)

st.divider()

# --------------------------------------------------
# OPERATIONAL ANALYTICS CHARTS
# --------------------------------------------------
st.markdown("## 📈 Operational Performance Analysis")

col5, col6 = st.columns(2)

with col5:
    warehouse_perf = (
        filtered_df.groupby("warehouse_block")["is_delayed"]
        .mean()
        .reset_index()
    )
    warehouse_perf["delay_rate"] = warehouse_perf["is_delayed"] * 100

    fig1 = px.bar(
        warehouse_perf,
        x="warehouse_block",
        y="delay_rate",
        title="Delay Rate by Warehouse",
        labels={
            "warehouse_block": "Warehouse",
            "delay_rate": "Delay Rate (%)"
        }
    )

    st.plotly_chart(fig1, use_container_width=True)

with col6:
    shipment_perf = (
        filtered_df.groupby("mode_of_shipment")["is_delayed"]
        .mean()
        .reset_index()
    )
    shipment_perf["delay_rate"] = shipment_perf["is_delayed"] * 100

    fig2 = px.bar(
        shipment_perf,
        x="mode_of_shipment",
        y="delay_rate",
        title="Delay Rate by Shipment Mode",
        labels={
            "mode_of_shipment": "Shipment Mode",
            "delay_rate": "Delay Rate (%)"
        }
    )

    st.plotly_chart(fig2, use_container_width=True)

col7, col8 = st.columns(2)

with col7:
    importance_perf = (
        filtered_df.groupby("product_importance")["is_delayed"]
        .mean()
        .reset_index()
    )
    importance_perf["delay_rate"] = importance_perf["is_delayed"] * 100

    fig3 = px.bar(
        importance_perf,
        x="product_importance",
        y="delay_rate",
        title="Delay Rate by Product Importance",
        labels={
            "product_importance": "Product Importance",
            "delay_rate": "Delay Rate (%)"
        }
    )

    st.plotly_chart(fig3, use_container_width=True)

with col8:
    calls_perf = (
        filtered_df.groupby("customer_care_calls")["is_delayed"]
        .mean()
        .reset_index()
    )
    calls_perf["delay_rate"] = calls_perf["is_delayed"] * 100

    fig4 = px.line(
        calls_perf,
        x="customer_care_calls",
        y="delay_rate",
        markers=True,
        title="Customer Care Calls vs Delay Rate",
        labels={
            "customer_care_calls": "Customer Care Calls",
            "delay_rate": "Delay Rate (%)"
        }
    )

    st.plotly_chart(fig4, use_container_width=True)

st.divider()

# --------------------------------------------------
# FEATURE IMPORTANCE SECTION
# --------------------------------------------------
st.markdown("## 📌 Operational Risk Drivers")

importance_df = pd.DataFrame({
    "Feature": [
        "Discount Offered",
        "Weight in grams",
        "Cost of Product",
        "Prior Purchases",
        "Customer Care Calls",
        "Customer Rating"
    ],
    "Importance": [
        0.402501,
        0.349629,
        0.119914,
        0.062379,
        0.035472,
        0.030104
    ]
})

fig_importance = px.bar(
    importance_df.sort_values("Importance", ascending=True),
    x="Importance",
    y="Feature",
    orientation="h",
    title="Random Forest Feature Importance"
)

st.plotly_chart(fig_importance, use_container_width=True)

st.divider()

# --------------------------------------------------
# DELAY RISK PREDICTION SECTION
# --------------------------------------------------
st.markdown("## 🤖 Delivery Delay Risk Prediction")

model = joblib.load("models/random_forest_delay_model.pkl")

col9, col10, col11 = st.columns(3)

with col9:
    customer_care_calls = st.number_input(
        "Customer Care Calls",
        min_value=2,
        max_value=7,
        value=4
    )

    customer_rating = st.number_input(
        "Customer Rating",
        min_value=1,
        max_value=5,
        value=3
    )

with col10:
    cost_of_the_product = st.number_input(
        "Cost of Product",
        min_value=50,
        max_value=400,
        value=200
    )

    prior_purchases = st.number_input(
        "Prior Purchases",
        min_value=1,
        max_value=10,
        value=3
    )

with col11:
    discount_offered = st.number_input(
        "Discount Offered",
        min_value=0,
        max_value=70,
        value=10
    )

    weight_in_gms = st.number_input(
        "Weight in grams",
        min_value=1000,
        max_value=8000,
        value=3000
    )

input_data = pd.DataFrame([{
    "customer_care_calls": customer_care_calls,
    "customer_rating": customer_rating,
    "cost_of_the_product": cost_of_the_product,
    "prior_purchases": prior_purchases,
    "discount_offered": discount_offered,
    "weight_in_gms": weight_in_gms
}])

if st.button("Predict Delay Risk"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f"⚠️ High Delay Risk Probability: {probability:.2f}%")
    else:
        st.success(f"✅ Low Delay Risk Probability: {probability:.2f}%")

# --------------------------------------------------
# BUSINESS INSIGHTS SECTION
# --------------------------------------------------
st.divider()

st.markdown("## 💡 Key Business Insights")

st.write("""
- Overall shipment delay rate is approximately **40%**, showing a major operational improvement opportunity.
- Warehouse **A** showed the highest delay rate among fulfillment centers.
- **Road shipments** had the highest delay percentage compared with Flight and Ship.
- **High-importance products** had fewer delays, suggesting successful operational prioritization.
- Customer care calls increased with delivery delay risk, making support activity a useful early warning signal.
- Random Forest achieved the best model performance with approximately **68% accuracy**.
- Feature importance analysis showed that **discount offered** and **package weight** were the strongest predictors of delay risk.
""")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.caption(
    "Built with Python, PostgreSQL, SQL, Scikit-learn, XGBoost, Random Forest, Plotly, and Streamlit."
)
