import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title of the Streamlit app
st.title("PayMyRent.gr Business Model and Financial Projections")

# Introduction to the Business Model
st.header("Overview of PayMyRent.gr Business Model")

st.write("""
**PayMyRent.gr** is a service designed to streamline the rent payment process for landlords. 
We offer an automated system for recurring monthly rent payments and a tenant screening service to help landlords choose reliable tenants. 

### Key Services:
- **Automated Rent Payments**: Landlords can receive rent through SEPA transfers or credit card payments. 
- **Tenant Screening**: We provide a credit score check for landlords who are looking for new tenants, ensuring they can select tenants with a solid financial background.
- **Insurance**: We offer insurance coverage that protects landlords against up to 3 months of unpaid rent.
""")

# Sidebar inputs for interactive adjustments
st.sidebar.header("Adjust Parameters")

# Default values for calculations
default_num_landlords = 90000
default_num_tenants = 90000
default_avg_rent = 600
default_sepa_fee_percent = 0.04
default_credit_card_fee_percent = 0.015
default_tenant_screening_fee = 5
default_salaries = 210000
default_insurance_cost = 70
default_credit_card_percentage = 0.2  # 20% use credit cards

# Additional operational costs
default_customer_support_cost = 25200  # €24,000 staff + €1,200 tools
default_marketing_sales_cost = 45000  # €12,000 marketing + €30,000 sales + €3,000 materials
default_legal_compliance_cost = 7000  # €5,000 legal fees + €2,000 compliance
default_it_infrastructure_cost = 4500  # €3,000 maintenance + €1,500 software
default_banking_fees_cost = 1000
default_training_development_cost = 3000
default_depreciation_cost = 3000

# Sidebar inputs
num_landlords = st.sidebar.number_input("Number of Landlords", value=default_num_landlords)
num_tenants = st.sidebar.number_input("Number of Tenants", value=default_num_tenants)
avg_rent = st.sidebar.number_input("Average Monthly Rent (€)", value=default_avg_rent)
sepa_fee_percent = st.sidebar.slider("SEPA Fee (%)", 0.0, 10.0, default_sepa_fee_percent * 100) / 100
credit_card_fee_percent = st.sidebar.slider("Credit Card Additional Fee (%)", 0.0, 10.0, default_credit_card_fee_percent * 100) / 100
tenant_screening_fee = st.sidebar.number_input("Tenant Screening Fee (€)", value=default_tenant_screening_fee)
salaries = st.sidebar.number_input("Annual Salaries (€)", value=default_salaries)
insurance_cost = st.sidebar.number_input("Annual Insurance Cost (€)", value=default_insurance_cost)
credit_card_percentage = st.sidebar.slider("Percentage of Landlords Using Credit Card (%)", 0.0, 100.0, default_credit_card_percentage * 100) / 100

# Additional operational costs
customer_support_cost = st.sidebar.number_input("Customer Support Cost (€)", value=default_customer_support_cost)
marketing_sales_cost = st.sidebar.number_input("Marketing and Sales Cost (€)", value=default_marketing_sales_cost)
legal_compliance_cost = st.sidebar.number_input("Legal and Compliance Cost (€)", value=default_legal_compliance_cost)
it_infrastructure_cost = st.sidebar.number_input("IT Infrastructure Cost (€)", value=default_it_infrastructure_cost)
banking_fees_cost = st.sidebar.number_input("Banking Fees Cost (€)", value=default_banking_fees_cost)
training_development_cost = st.sidebar.number_input("Training and Development Cost (€)", value=default_training_development_cost)
depreciation_cost = st.sidebar.number_input("Depreciation Cost (€)", value=default_depreciation_cost)

# Number of landlords using SEPA and Credit Card
num_credit_card_landlords = int(num_landlords * credit_card_percentage)
num_sepa_landlords = num_landlords - num_credit_card_landlords

# Calculations using numpy
# Monthly SEPA Revenue Calculation
monthly_sepa_revenue_per_landlord = avg_rent * sepa_fee_percent
annual_sepa_revenue = monthly_sepa_revenue_per_landlord * 12 * num_sepa_landlords

# Monthly Credit Card Revenue Calculation
monthly_credit_card_revenue_per_landlord = avg_rent * (sepa_fee_percent + credit_card_fee_percent)
annual_credit_card_revenue = monthly_credit_card_revenue_per_landlord * 12 * num_credit_card_landlords

# Annual Revenue from Tenant Screening Fees
annual_tenant_screening_revenue = tenant_screening_fee * num_tenants

# Cost Calculations
# SEPA Transaction Costs
sepa_transaction_cost_per_month = 2.35 + 0.002 * avg_rent
annual_sepa_transaction_cost = sepa_transaction_cost_per_month * 12 * num_sepa_landlords

# Credit Card Transaction Costs
credit_card_transaction_cost_per_month = avg_rent * 0.015
annual_credit_card_transaction_cost = credit_card_transaction_cost_per_month * 12 * num_credit_card_landlords

# Tenant Screening Costs
annual_tenant_screening_cost = 2 * num_tenants

# Total Costs
total_annual_costs = (annual_sepa_transaction_cost + annual_credit_card_transaction_cost + 
                      annual_tenant_screening_cost + customer_support_cost + 
                      marketing_sales_cost + legal_compliance_cost + 
                      it_infrastructure_cost + banking_fees_cost + 
                      training_development_cost + depreciation_cost + 
                      salaries + insurance_cost * num_landlords)

# Revenue Calculations
total_annual_revenue = annual_sepa_revenue + annual_credit_card_revenue + annual_tenant_screening_revenue

# Net Revenue
net_annual_revenue = total_annual_revenue - total_annual_costs

# Break-Even Point Calculation
break_even_landlords = total_annual_costs / (monthly_sepa_revenue_per_landlord * 12)

# Display Calculations
st.header("Business Model and Financial Calculations")

st.subheader("Revenue Streams")
st.write(f"**Annual Revenue from SEPA Payments:** €{annual_sepa_revenue:,.2f}")
st.write(f"**Annual Revenue from Credit Card Payments:** €{annual_credit_card_revenue:,.2f}")
st.write(f"**Annual Revenue from Tenant Screening Fees:** €{annual_tenant_screening_revenue:,.2f}")

st.subheader("Total Costs")
st.write(f"**Total Annual Costs:** €{total_annual_costs:,.2f}")

st.subheader("Net Annual Revenue")
st.write(f"**Net Annual Revenue (after costs):** €{net_annual_revenue:,.2f}")

st.subheader("Break-Even Point")
st.write(f"**Break-Even Number of Landlords:** {int(break_even_landlords)} landlords")

# Explanation of the Business Model
st.header("Explanation of the Business Model")

st.write("""
### **What We Do:**
PayMyRent.gr automates the rent collection process, making it easier for landlords to receive payments on time. We also offer tenant screening services to help landlords find reliable tenants.

### **How We Do It:**
- **Automated Rent Payments**: We process rent payments through SEPA or credit card. Landlords choose their preferred method, and we handle the rest.
- **Tenant Screening**: We charge tenants a small fee for a credit score check, which is then shared with landlords to help them make informed decisions.
- **Insurance**: We provide landlords with an insurance option that covers up to 3 months of unpaid rent, offering peace of mind.

### **Advantages:**
- **Convenience**: Automating rent payments reduces the administrative burden on landlords.
- **Security**: SEPA and credit card payments are secure and reliable.
- **Risk Management**: The insurance coverage protects landlords from potential losses due to unpaid rent.

### **Market Size Estimation:**
We estimate the market size based on the number of rental properties in Greece. With approximately 90,000 landlords managing rental properties, we have a significant market to tap into. These figures are derived from market research on the rental housing sector.

### **Key Assumptions:**
- **Landlords**: 90,000 landlords in the market.
- **Tenants**: 90,000 tenants being screened annually.
- **Average Rent**: €600 per month.
- **SEPA Fee**: 4% of the rental amount.
- **Credit Card Fee**: An additional 1.5% on top of the SEPA fee.
- **Break-Even Analysis**: The break-even point is calculated based on covering all annual costs with revenue from landlord fees.
""")

# Graphs
st.header("Graphs")

# Revenue and Cost Breakdown
fig, ax = plt.subplots(figsize=(12, 8))
categories = ['SEPA Payments', 'Credit Card Payments', 'Tenant Screening Fees']
revenue_values = [annual_sepa_revenue, annual_credit_card_revenue, annual_tenant_screening_revenue]

costs_categories = ['SEPA Transaction Costs', 'Credit Card Transaction Costs', 'Tenant Screening Costs', 'Customer Support', 'Marketing and Sales', 'Legal and Compliance', 'IT Infrastructure', 'Banking Fees', 'Training and Development', 'Depreciation']
costs_values = [annual_sepa_transaction_cost, annual_credit_card_transaction_cost, annual_tenant_screening_cost, customer_support_cost, marketing_sales_cost, legal_compliance_cost, it_infrastructure_cost, banking_fees_cost, training_development_cost, depreciation_cost]

ax.bar(categories, revenue_values, color='blue', label='Revenue')
ax.bar(costs_categories, costs_values, color='red', label='Costs', alpha=0.6)
ax.set_xlabel('Categories')
ax.set_ylabel('Amount (€)')
ax.set_title('Revenue vs Costs')
ax.legend()

st.pyplot(fig)

# Break-Even Analysis
fig_break_even, ax = plt.subplots(figsize=(10, 6))

ax.plot([0, break_even_landlords], [total_annual_costs, total_annual_costs], 'r-', label='Total Costs')
ax.plot([0, num_landlords], [0, total_annual_revenue], 'b-', label='Total Revenue')
ax.set_xlabel('Number of Landlords')
ax.set_ylabel('Amount (€)')
ax.set_title('Break-Even Analysis')
ax.legend()

st.pyplot(fig_break_even)

st.write("Use the sidebar to adjust parameters and see how they affect your financial projections and graphs.")
