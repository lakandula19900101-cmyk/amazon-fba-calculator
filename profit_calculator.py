import streamlit as st

st.set_page_config(
    page_title="亚马逊FBA利润计算器",
    page_icon="📦"
)

st.title("📦 亚马逊 FBA 利润计算器")

purchase_price = st.number_input(
    "产品采购成本（人民币）",
    min_value=0.0,
    value=50.0
)

selling_price_usd = st.number_input(
    "亚马逊售价（美元）",
    min_value=0.0,
    value=29.99
)

exchange_rate = st.number_input(
    "美元汇率",
    min_value=1.0,
    value=7.2
)

shipping_cost = st.number_input(
    "头程运费（人民币）",
    min_value=0.0,
    value=15.0
)

fba_fee = st.number_input(
    "FBA配送费（人民币）",
    min_value=0.0,
    value=35.0
)

commission_rate = st.number_input(
    "平台佣金 (%)",
    min_value=0.0,
    value=15.0
)

ad_cost = st.number_input(
    "广告费（人民币）",
    min_value=0.0,
    value=20.0
)

if st.button("计算利润"):

    sales_rmb = selling_price_usd * exchange_rate

    commission_fee = sales_rmb * commission_rate / 100

    total_cost = (
        purchase_price
        + shipping_cost
        + fba_fee
        + commission_fee
        + ad_cost
    )

    profit = sales_rmb - total_cost

    if sales_rmb > 0:
        margin = profit / sales_rmb * 100
    else:
        margin = 0

    st.subheader("📊 利润分析")

    st.write(f"销售额：¥ {sales_rmb:.2f}")
    st.write(f"平台佣金：¥ {commission_fee:.2f}")
    st.write(f"总成本：¥ {total_cost:.2f}")

    if profit >= 0:
        st.success(f"利润：¥ {profit:.2f}")
    else:
        st.error(f"亏损：¥ {profit:.2f}")

    st.info(f"利润率：{margin:.2f}%")

    if margin >= 30:
        st.success("🟢 优秀产品")
    elif margin >= 15:
        st.warning("🟡 利润一般")
    else:
        st.error("🔴 利润偏低，需优化")