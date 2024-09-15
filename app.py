import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from parameters import DEFAULT_VALUES, calculate_market_size_revenue, calculate_costs

# sidebar
st.sidebar.title("PayMyRent.gr Business Model and Financial Projections")
choice = st.sidebar.radio("Select an Option", ["Description", "Market Size Estimation and Revenue Projections", "Cost Analysis"])

# Title of the Streamlit app
st.title("PayMyRent.gr Business Model and Financial Projections")

if choice == "Description":

    # Introduction to the Business Model
    st.header("Overview of PayMyRent.gr")

    st.write("""
    **PayMyRent.gr** is a service designed to streamline the rent payment process for landlords. 
    We offer an automated system for recurring monthly rent payments and a tenant screening service to help landlords choose reliable tenants. 

    ### Value Proposition:

    The **value proposition** of PayMyRent.gr offers a well-rounded solution tailored primarily for landlords, addressing key challenges and enhancing security and convenience.

    #### **For Landlords:**

    1. **Efficiency:**
    - **Automated rent collection** through SEPA or credit card simplifies the process, ensuring **consistent, on-time payments** with minimal administrative effort.
    - This allows landlords to focus on other aspects of property management without worrying about payment delays.

    2. **Financial Security:**
    - The service includes **insurance protection** that covers up to **3 months of unpaid rent**, giving landlords peace of mind in case tenants default on payments.
    - Moreover, the insurance also covers **unpaid utility bills** and **legal costs** involved in pursuing unpaid rent, offering comprehensive financial protection.

    3. **Tenant Screening:**
    - PayMyRent.gr provides a **tenant screening service** via a **credit score check**, helping landlords select financially reliable tenants.
    - This reduces the risk of renting to tenants who may default, offering landlords a way to mitigate potential risks upfront.

    #### **For Tenants:**

    1. **Convenience:**
    - Tenants benefit from **automated monthly rent payments**, eliminating the need for manual payments and reducing the risk of late fees.
    - Payments can be made via SEPA or, for those preferring credit-based payments, through **credit card** (with an additional 1.5% fee).


    ### Key Services:
    - **Automated Rent Payments**: Landlords can receive rent through SEPA transfers or credit card payments. 
    - **Tenant Screening**: We provide a credit score check for landlords who are looking for new tenants, ensuring they can select tenants with a solid financial background.
    - **Insurance**: We offer insurance coverage that protects landlords against up to 3 months of unpaid rent.
    """)

if choice == "Description":

    # Introduction to the Business Model
    st.header("Overview of PayMyRent.gr")

    st.write(""" 
    **PayMyRent.gr** is a service designed to streamline the rent payment process for landlords. 
    We offer an automated system for recurring monthly rent payments and a tenant screening service to help landlords choose reliable tenants. 

    ### Value Proposition:

    The **value proposition** of PayMyRent.gr offers a well-rounded solution tailored primarily for landlords, addressing key challenges and enhancing security and convenience.

    #### **For Landlords:**

    1. **Efficiency:**
    - **Automated rent collection** through SEPA or credit card simplifies the process, ensuring **consistent, on-time payments** with minimal administrative effort.
    - This allows landlords to focus on other aspects of property management without worrying about payment delays.

    2. **Financial Security:**
    - The service includes **insurance protection** that covers up to **3 months of unpaid rent**, giving landlords peace of mind in case tenants default on payments.
    - Moreover, the insurance also covers **unpaid utility bills** and **legal costs** involved in pursuing unpaid rent, offering comprehensive financial protection.

    3. **Tenant Screening:**
    - PayMyRent.gr provides a **tenant screening service** via a **credit score check**, helping landlords select financially reliable tenants.
    - This reduces the risk of renting to tenants who may default, offering landlords a way to mitigate potential risks upfront.

    #### **For Tenants:**

    1. **Convenience:**
    - Tenants benefit from **automated monthly rent payments**, eliminating the need for manual payments and reducing the risk of late fees.
    - Payments can be made via SEPA or, for those preferring credit-based payments, through **credit card** (with an additional 1.5% fee).

    ### Key Services:
    - **Automated Rent Payments**: Landlords can receive rent through SEPA transfers or credit card payments. 
    - **Tenant Screening**: We provide a credit score check for landlords who are looking for new tenants, ensuring they can select tenants with a solid financial background.
    - **Insurance**: We offer insurance coverage that protects landlords against up to 3 months of unpaid rent.
    """)

# if choice == "Market Size Estimation and Revenue Projections":
    
#     st.header("Market Size Estimation and Revenue Projections")
    
#     # Sidebar inputs for interactive adjustments
#     st.sidebar.header("Adjust Parameters")

#     # Default values for calculations
#     default_percentage_commercial = 20.0  # percentage of commercial properties
#     default_adoption_rate_residential = 5.0  # adoption rate for residential
#     default_adoption_rate_commercial = 5.0  # adoption rate for commercial
#     default_fee_rate = 4.0  # fee rate in percentage
#     default_avg_rent_residential = 600  # average rent for residential properties
#     default_avg_rent_commercial = 1000  # average rent for commercial properties
#     default_credit_card_additional_fee = 1.6  # additional fee for credit card payments
#     default_tenant_screening_fee = 5  # fee per tenant screening
#     default_percentage_screening = 50.0  # percentage of tenants using screening

#     # Sidebar inputs
#     percentage_commercial = st.sidebar.slider("Percentage of Commercial Properties (%)", 0.0, 100.0, default_percentage_commercial)
#     adoption_rate_residential = st.sidebar.slider("Adoption Rate for Residential (%)", 0.0, 100.0, default_adoption_rate_residential)
#     adoption_rate_commercial = st.sidebar.slider("Adoption Rate for Commercial (%)", 0.0, 100.0, default_adoption_rate_commercial)
#     fee_rate = st.sidebar.slider("Fee Rate (%)", 0.0, 10.0, default_fee_rate)
#     avg_rent_residential = st.sidebar.number_input("Average Monthly Rent for Residential (€)", value=default_avg_rent_residential)
#     avg_rent_commercial = st.sidebar.number_input("Average Monthly Rent for Commercial (€)", value=default_avg_rent_commercial)
#     credit_card_additional_fee = st.sidebar.slider("Additional Credit Card Fee (%)", 0.0, 10.0, default_credit_card_additional_fee)
#     tenant_screening_fee = st.sidebar.number_input("Tenant Screening Fee (€)", value=default_tenant_screening_fee)
#     percentage_screening = st.sidebar.slider("Percentage of Tenants Using Screening (%)", 0.0, 100.0, default_percentage_screening)

#     # Market Size Calculation
#     total_households = 4332447
#     rental_households = 1299176
#     commercial_properties = (percentage_commercial / 100) * rental_households
#     residential_properties = rental_households - commercial_properties

#     potential_residential_tenants = (adoption_rate_residential / 100) * residential_properties
#     potential_commercial_tenants = (adoption_rate_commercial / 100) * commercial_properties

#     revenue_residential_landlords = avg_rent_residential * (fee_rate / 100) * 12 * potential_residential_tenants
#     revenue_commercial_landlords = avg_rent_commercial * (fee_rate / 100) * 12 * potential_commercial_tenants

#     revenue_credit_card_residential = avg_rent_residential * (credit_card_additional_fee / 100) * (adoption_rate_residential / 100) * 12 * potential_residential_tenants
#     revenue_credit_card_commercial = avg_rent_commercial * (credit_card_additional_fee / 100) * (adoption_rate_commercial / 100) * 12 * potential_commercial_tenants

#     revenue_tenant_screening_residential = tenant_screening_fee * (percentage_screening / 100) * potential_residential_tenants
#     revenue_tenant_screening_commercial = tenant_screening_fee * (percentage_screening / 100) * potential_commercial_tenants

#     total_revenue = (revenue_residential_landlords + revenue_commercial_landlords +
#                      revenue_credit_card_residential + revenue_credit_card_commercial +
#                      revenue_tenant_screening_residential + revenue_tenant_screening_commercial)
    
#     st.write(f"**Total Number of Households in Greece:** {total_households:,.0f}")
#     st.write(f"**Total Number of Rental Households:** {rental_households:,.0f}")
#     st.write(f"**Estimated Number of Commercial Properties:** {commercial_properties:,.0f}")
#     st.write(f"**Estimated Number of Residential Properties:** {residential_properties:,.0f}")
#     st.write(f"**Potential Residential Tenants:** {potential_residential_tenants:,.0f}")
#     st.write(f"**Potential Commercial Tenants:** {potential_commercial_tenants:,.0f}")
#     st.write(f"**Total Annual Revenue from Residential Landlords:** €{revenue_residential_landlords:,.2f}")
#     st.write(f"**Total Annual Revenue from Commercial Landlords:** €{revenue_commercial_landlords:,.2f}")
#     st.write(f"**Total Annual Revenue from Credit Card Payments (Residential):** €{revenue_credit_card_residential:,.2f}")
#     st.write(f"**Total Annual Revenue from Credit Card Payments (Commercial):** €{revenue_credit_card_commercial:,.2f}")
#     st.write(f"**Total Annual Revenue from Tenant Screening (Residential):** €{revenue_tenant_screening_residential:,.2f}")
#     st.write(f"**Total Annual Revenue from Tenant Screening (Commercial):** €{revenue_tenant_screening_commercial:,.2f}")
    
#     st.write(f"**Total Annual Revenue Potential:** €{total_revenue:,.2f}")
    
#     # Market Size and Target Pie Charts
#     # Data for pie charts
#     total_market_size = rental_households
#     target_market_size = potential_residential_tenants + potential_commercial_tenants

#     labels = ['Total Market Size', 'Target Market Size']
#     sizes = [total_market_size, target_market_size]
#     colors = ['#ff9999','#66b3ff']
    
#     fig, ax = plt.subplots()
#     ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
#     ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#     st.pyplot(fig)
    
#     ### Source
#     st.write("""Data on the number of households is sourced from the [Hellenic Statistical Authority](https://www.statistics.gr/el/2021-census-res-pop-results) (2021 Census).
#     """)

#     st.write("""
#     ### Parameters Analysis

#     - **Percentage of Commercial Properties:** Adjusts the proportion of rental properties that are commercial. Increasing this percentage will affect commercial revenue calculations.
#     - **Adoption Rate for Residential:** Represents the percentage of residential properties adopting the service. Higher adoption rates increase potential revenue from residential properties.
#     - **Adoption Rate for Commercial:** Similar to the residential adoption rate but for commercial properties.
#     - **Fee Rate:** The percentage fee applied to the average rent amount for each property. Higher fees increase potential revenue.
#     - **Average Monthly Rent for Residential:** The typical rent for residential properties. Adjusting this changes the revenue calculations for residential properties.
#     - **Average Monthly Rent for Commercial:** Similar to residential rent but for commercial properties.
#     - **Additional Credit Card Fee:** Represents the extra charge for using a credit card. Higher fees impact potential revenue from credit card payments.
#     - **Tenant Screening Fee:** The fee charged for screening tenants. This contributes to revenue based on the percentage of tenants using the screening service.
#     - **Percentage of Tenants Using Screening:** The proportion of tenants who opt for the screening service. Increasing this percentage enhances revenue from screening fees.
#     """)
    
# if choice == "Financial Projections":

#     # Sidebar inputs for interactive adjustments
#     st.sidebar.header("Adjust Parameters")

#     # Default values for calculations
#     default_num_landlords = 90000
#     default_num_tenants = 90000
#     default_avg_rent = 600
#     default_sepa_fee_percent = 0.04
#     default_credit_card_fee_percent = 0.015
#     default_tenant_screening_fee = 5
#     default_salaries = 210000
#     default_insurance_cost = 70
#     default_credit_card_percentage = 0.2  # 20% use credit cards

#     # Additional operational costs
#     default_customer_support_cost = 25200  # €24,000 staff + €1,200 tools
#     default_marketing_sales_cost = 45000  # €12,000 marketing + €30,000 sales + €3,000 materials
#     default_legal_compliance_cost = 7000  # €5,000 legal fees + €2,000 compliance
#     default_it_infrastructure_cost = 4500  # €3,000 maintenance + €1,500 software
#     default_banking_fees_cost = 1000
#     default_training_development_cost = 3000
#     default_depreciation_cost = 3000

#     # Sidebar inputs
#     num_landlords = st.sidebar.number_input("Number of Landlords", value=default_num_landlords)
#     num_tenants = st.sidebar.number_input("Number of Tenants", value=default_num_tenants)
#     avg_rent = st.sidebar.number_input("Average Monthly Rent (€)", value=default_avg_rent)
#     sepa_fee_percent = st.sidebar.slider("SEPA Fee (%)", 0.0, 10.0, default_sepa_fee_percent * 100) / 100
#     credit_card_fee_percent = st.sidebar.slider("Credit Card Additional Fee (%)", 0.0, 10.0, default_credit_card_fee_percent * 100) / 100
#     tenant_screening_fee = st.sidebar.number_input("Tenant Screening Fee (€)", value=default_tenant_screening_fee)
#     salaries = st.sidebar.number_input("Annual Salaries (€)", value=default_salaries)
#     insurance_cost = st.sidebar.number_input("Annual Insurance Cost (€)", value=default_insurance_cost)
#     credit_card_percentage = st.sidebar.slider("Percentage of Landlords Using Credit Card (%)", 0.0, 100.0, default_credit_card_percentage * 100) / 100

#     # Additional operational costs
#     customer_support_cost = st.sidebar.number_input("Customer Support Cost (€)", value=default_customer_support_cost)
#     marketing_sales_cost = st.sidebar.number_input("Marketing and Sales Cost (€)", value=default_marketing_sales_cost)
#     legal_compliance_cost = st.sidebar.number_input("Legal and Compliance Cost (€)", value=default_legal_compliance_cost)
#     it_infrastructure_cost = st.sidebar.number_input("IT Infrastructure Cost (€)", value=default_it_infrastructure_cost)
#     banking_fees_cost = st.sidebar.number_input("Banking Fees Cost (€)", value=default_banking_fees_cost)
#     training_development_cost = st.sidebar.number_input("Training and Development Cost (€)", value=default_training_development_cost)
#     depreciation_cost = st.sidebar.number_input("Depreciation Cost (€)", value=default_depreciation_cost)

#     # Number of landlords using SEPA and Credit Card
#     num_credit_card_landlords = int(num_landlords * credit_card_percentage)
#     num_sepa_landlords = num_landlords - num_credit_card_landlords

#     # Calculations using numpy
#     # Monthly SEPA Revenue Calculation
#     monthly_sepa_revenue_per_landlord = avg_rent * sepa_fee_percent
#     annual_sepa_revenue = monthly_sepa_revenue_per_landlord * 12 * num_sepa_landlords

#     # Monthly Credit Card Revenue Calculation
#     monthly_credit_card_revenue_per_landlord = avg_rent * (sepa_fee_percent + credit_card_fee_percent)
#     annual_credit_card_revenue = monthly_credit_card_revenue_per_landlord * 12 * num_credit_card_landlords

#     # Annual Revenue from Tenant Screening Fees
#     annual_tenant_screening_revenue = tenant_screening_fee * num_tenants

#     # Cost Calculations
#     # SEPA Transaction Costs
#     sepa_transaction_cost_per_month = 2.35 + 0.002 * avg_rent
#     annual_sepa_transaction_cost = sepa_transaction_cost_per_month * 12 * num_sepa_landlords

#     # Credit Card Transaction Costs
#     credit_card_transaction_cost_per_month = avg_rent * 0.015
#     annual_credit_card_transaction_cost = credit_card_transaction_cost_per_month * 12 * num_credit_card_landlords

#     # Tenant Screening Costs
#     annual_tenant_screening_cost = 2 * num_tenants

#     # Total Costs
#     total_annual_costs = (annual_sepa_transaction_cost + annual_credit_card_transaction_cost + 
#                         annual_tenant_screening_cost + customer_support_cost + 
#                         marketing_sales_cost + legal_compliance_cost + 
#                         it_infrastructure_cost + banking_fees_cost + 
#                         training_development_cost + depreciation_cost + 
#                         salaries + insurance_cost * num_landlords)

#     # Revenue Calculations
#     total_annual_revenue = annual_sepa_revenue + annual_credit_card_revenue + annual_tenant_screening_revenue

#     # Net Revenue
#     net_annual_revenue = total_annual_revenue - total_annual_costs

#     # Break-Even Point Calculation
#     break_even_landlords = total_annual_costs / (monthly_sepa_revenue_per_landlord * 12)

#     # Display Calculations
#     st.header("Business Model and Financial Calculations")

#     st.subheader("Revenue Streams")
#     st.write(f"**Annual Revenue from SEPA Payments:** €{annual_sepa_revenue:,.2f}")
#     st.write(f"**Annual Revenue from Credit Card Payments:** €{annual_credit_card_revenue:,.2f}")
#     st.write(f"**Annual Revenue from Tenant Screening Fees:** €{annual_tenant_screening_revenue:,.2f}")

#     st.subheader("Total Costs")
#     st.write(f"**Total Annual Costs:** €{total_annual_costs:,.2f}")

#     st.subheader("Net Annual Revenue")
#     st.write(f"**Net Annual Revenue (after costs):** €{net_annual_revenue:,.2f}")

#     st.subheader("Break-Even Point")
#     st.write(f"**Break-Even Number of Landlords:** {int(break_even_landlords)} landlords")

#     # Explanation of the Business Model
#     st.header("Explanation of the Business Model")

#     st.write("""
#     ### **What We Do:**
#     PayMyRent.gr automates the rent collection process, making it easier for landlords to receive payments on time. We also offer tenant screening services to help landlords find reliable tenants.

#     ### **How We Do It:**
#     - **Automated Rent Payments**: We process rent payments through SEPA or credit card. Landlords choose their preferred method, and we handle the rest.
#     - **Tenant Screening**: We charge tenants a small fee for a credit score check, which is then shared with landlords to help them make informed decisions.
#     - **Insurance**: We provide landlords with an insurance option that covers up to 3 months of unpaid rent, offering peace of mind.

#     ### **Advantages:**
#     - **Convenience**: Automating rent payments reduces the administrative burden on landlords.
#     - **Security**: SEPA and credit card payments are secure and reliable.
#     - **Risk Management**: The insurance coverage protects landlords from potential losses due to unpaid rent.

#     ### **Market Size Estimation:**
#     We estimate the market size based on the number of rental properties in Greece. With approximately 90,000 landlords managing rental properties, we have a significant market to tap into. These figures are derived from market research on the rental housing sector.

#     ### **Key Assumptions:**
#     - **Landlords**: 90,000 landlords in the market.
#     - **Tenants**: 90,000 tenants being screened annually.
#     - **Average Rent**: €600 per month.
#     - **SEPA Fee**: 4% of the rental amount.
#     - **Credit Card Fee**: An additional 1.5% on top of the SEPA fee.
#     - **Break-Even Analysis**: The break-even point is calculated based on covering all annual costs with revenue from landlord fees.
#     """)

#     # Graphs
#     st.header("Graphs")

#     # Revenue and Cost Breakdown
#     fig, ax = plt.subplots(figsize=(12, 8))
#     categories = ['SEPA Payments', 'Credit Card Payments', 'Tenant Screening Fees']
#     revenue_values = [annual_sepa_revenue, annual_credit_card_revenue, annual_tenant_screening_revenue]

#     costs_categories = ['SEPA Transaction Costs', 'Credit Card Transaction Costs', 'Tenant Screening Costs', 'Customer Support', 'Marketing and Sales', 'Legal and Compliance', 'IT Infrastructure', 'Banking Fees', 'Training and Development', 'Depreciation']
#     costs_values = [annual_sepa_transaction_cost, annual_credit_card_transaction_cost, annual_tenant_screening_cost, customer_support_cost, marketing_sales_cost, legal_compliance_cost, it_infrastructure_cost, banking_fees_cost, training_development_cost, depreciation_cost]

#     ax.bar(categories, revenue_values, color='blue', label='Revenue')
#     ax.bar(costs_categories, costs_values, color='red', label='Costs', alpha=0.6)
#     ax.set_xlabel('Categories')
#     ax.set_ylabel('Amount (€)')
#     ax.set_title('Revenue vs Costs')
#     ax.legend()

#     st.pyplot(fig)

#     # Break-Even Analysis
#     fig_break_even, ax = plt.subplots(figsize=(10, 6))

#     ax.plot([0, break_even_landlords], [total_annual_costs, total_annual_costs], 'r-', label='Total Costs')
#     ax.plot([0, num_landlords], [0, total_annual_revenue], 'b-', label='Total Revenue')
#     ax.set_xlabel('Number of Landlords')
#     ax.set_ylabel('Amount (€)')
#     ax.set_title('Break-Even Analysis')
#     ax.legend()

#     st.pyplot(fig_break_even)

#     st.write("Use the sidebar to adjust parameters and see how they affect your financial projections and graphs.")

# Initialize session state attributes

if 'potential_residential_tenants' not in st.session_state:
    st.session_state['potential_residential_tenants'] = 0
if 'potential_commercial_tenants' not in st.session_state:
    st.session_state['potential_commercial_tenants'] = 0

# Sidebar for Market Size and Revenue Parameters
if choice == "Market Size Estimation and Revenue Projections":

    st.header("Market Size Estimation and Revenue Projections")

    # Sidebar inputs
    percentage_commercial = st.sidebar.slider("Percentage of Commercial Properties (%)", 0.0, 100.0, DEFAULT_VALUES['percentage_commercial'])
    adoption_rate_residential = st.sidebar.slider("Adoption Rate for Residential (%)", 0.0, 100.0, DEFAULT_VALUES['adoption_rate_residential'])
    adoption_rate_commercial = st.sidebar.slider("Adoption Rate for Commercial (%)", 0.0, 100.0, DEFAULT_VALUES['adoption_rate_commercial'])
    fee_rate = st.sidebar.slider("Fee Rate (%)", 0.0, 10.0, DEFAULT_VALUES['fee_rate'])
    avg_rent_residential = st.sidebar.number_input("Average Monthly Rent for Residential (€)", value=DEFAULT_VALUES['avg_rent_residential'])
    avg_rent_commercial = st.sidebar.number_input("Average Monthly Rent for Commercial (€)", value=DEFAULT_VALUES['avg_rent_commercial'])
    credit_card_additional_fee = st.sidebar.slider("Additional Credit Card Fee (%)", 0.0, 10.0, DEFAULT_VALUES['credit_card_additional_fee'])
    credit_card_usage_rate = st.sidebar.slider("Percentage of Tenants Using Credit Card (%)", 0.0, 100.0, DEFAULT_VALUES['credit_card_usage_rate'])
    tenant_screening_fee = st.sidebar.number_input("Tenant Screening Fee (€)", value=DEFAULT_VALUES['tenant_screening_fee'])
    percentage_screening = st.sidebar.slider("Percentage of Tenants Using Screening (%)", 0.0, 100.0, DEFAULT_VALUES['percentage_screening'])

    # Calculate market size and revenue
    market_size_revenue = calculate_market_size_revenue(
        percentage_commercial, adoption_rate_residential, adoption_rate_commercial,
        fee_rate, avg_rent_residential, avg_rent_commercial, credit_card_additional_fee,
        tenant_screening_fee, percentage_screening, credit_card_usage_rate
    )

    # Update session state
    st.session_state['potential_residential_tenants'] = market_size_revenue['potential_residential_tenants']
    st.session_state['potential_commercial_tenants'] = market_size_revenue['potential_commercial_tenants']

    # Display market size and revenue results
    st.write(f"**Total Number of Households in Greece:** {market_size_revenue['total_households']:,}")
    st.write(f"**Total Number of Rental Households:** {market_size_revenue['rental_households']:,}")
    st.write(f"**Estimated Number of Commercial Properties:** {market_size_revenue['commercial_properties']:,}")
    st.write(f"**Estimated Number of Residential Properties:** {market_size_revenue['residential_properties']:,}")
    st.write(f"**Potential Residential Tenants:** {market_size_revenue['potential_residential_tenants']:,}")
    st.write(f"**Potential Commercial Tenants:** {market_size_revenue['potential_commercial_tenants']:,}")
    st.write(f"**Total Annual Revenue from Residential Landlords:** €{market_size_revenue['revenue_residential_landlords']:.2f}")
    st.write(f"**Total Annual Revenue from Commercial Landlords:** €{market_size_revenue['revenue_commercial_landlords']:.2f}")
    st.write(f"**Total Annual Revenue from Credit Card Payments (Residential):** €{market_size_revenue['revenue_credit_card_residential']:.2f}")
    st.write(f"**Total Annual Revenue from Credit Card Payments (Commercial):** €{market_size_revenue['revenue_credit_card_commercial']:.2f}")
    st.write(f"**Total Annual Revenue from Tenant Screening (Residential):** €{market_size_revenue['revenue_tenant_screening_residential']:.2f}")
    st.write(f"**Total Annual Revenue from Tenant Screening (Commercial):** €{market_size_revenue['revenue_tenant_screening_commercial']:.2f}")
    st.write(f"**Total Annual Revenue Potential:** €{market_size_revenue['total_revenue']:.2f}")

    # Market Size and Target Pie Charts
    total_market_size = market_size_revenue['rental_households']
    target_market_size = market_size_revenue['potential_residential_tenants'] + market_size_revenue['potential_commercial_tenants']

    labels = ['Total Market Size', 'Target Market Size']
    sizes = [total_market_size, target_market_size]
    colors = ['#ff9999','#66b3ff']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)
    
    revenue_labels = ['Residential Landlords', 'Commercial Landlords', 'Credit Card Payments (Residential)', 'Credit Card Payments (Commercial)', 'Tenant Screening (Residential)', 'Tenant Screening (Commercial)']
    revenue_values = [market_size_revenue['revenue_residential_landlords'], market_size_revenue['revenue_commercial_landlords'],
                      market_size_revenue['revenue_credit_card_residential'], market_size_revenue['revenue_credit_card_commercial'],
                      market_size_revenue['revenue_tenant_screening_residential'], market_size_revenue['revenue_tenant_screening_commercial']]
    
    fig_revenue, ax = plt.subplots()
    ax.bar(revenue_labels, revenue_values, color='blue')
    ax.set_ylabel('Revenue (€)')
    ax.set_title('Revenue Projections')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig_revenue)

    # Source
    st.write("""Data on the number of households is sourced from the [Hellenic Statistical Authority](https://www.statistics.gr/el/2021-census-res-pop-results) (2021 Census).""")

    st.write("""
    ### Parameters Analysis
    - **Percentage of Commercial Properties:** Adjusts the proportion of rental properties that are commercial. Increasing this percentage will affect commercial revenue calculations.
    - **Adoption Rate for Residential:** Represents the percentage of residential properties adopting the service. Higher adoption rates increase potential revenue from residential properties.
    - **Adoption Rate for Commercial:** Similar to the residential adoption rate but for commercial properties.
    - **Fee Rate:** The percentage fee applied to the average rent amount for each property. Higher fees increase potential revenue.
    - **Average Monthly Rent for Residential:** The typical rent for residential properties. Adjusting this changes the revenue calculations for residential properties.
    - **Average Monthly Rent for Commercial:** Similar to residential rent but for commercial properties.
    - **Additional Credit Card Fee:** Represents the extra charge for using a credit card. Higher fees impact potential revenue from credit card payments.
    - **Tenant Screening Fee:** The fee charged for screening tenants. This contributes to revenue based on the percentage of tenants using the screening service.
    - **Percentage of Tenants Using Screening:** The proportion of tenants who opt for the screening service. Increasing this percentage enhances revenue from screening fees.
    """)

# Sidebar for Costs
if choice == "Cost Analysis":

    st.header("Cost Analysis")

    # Sidebar inputs for costs
    sepa_fee = st.sidebar.number_input("SEPA Fee per Transaction (€)", value=DEFAULT_VALUES['sepa_fee'])
    credit_card_fee_percentage = st.sidebar.number_input("Credit Card Fee Percentage (%)", value=DEFAULT_VALUES['credit_card_fee_percentage'])
    credit_card_fee_fixed = st.sidebar.number_input("Credit Card Fee Fixed (€)", value=DEFAULT_VALUES['credit_card_fee_fixed'])
    credit_card_usage_rate = st.sidebar.number_input("Percentage of Tenants Using Credit Card (%)", value=DEFAULT_VALUES['credit_card_usage_rate'])
    insurance_cost_percentage = st.sidebar.number_input("Insurance Cost Percentage (%)", value=DEFAULT_VALUES['insurance_cost_percentage'])
    customer_support_cost = st.sidebar.number_input("Customer Support Cost (€)", value=DEFAULT_VALUES['customer_support_cost'])
    marketing_sales_cost = st.sidebar.number_input("Marketing and Sales Cost (€)", value=DEFAULT_VALUES['marketing_sales_cost'])
    infrastructure_it_cost = st.sidebar.number_input("Infrastructure and IT Cost (€)", value=DEFAULT_VALUES['infrastructure_it_cost'])
    training_development_cost = st.sidebar.number_input("Training and Development Cost (€)", value=DEFAULT_VALUES['training_development_cost'])
    depreciation_cost = st.sidebar.number_input("Depreciation Cost (€)", value=DEFAULT_VALUES['depreciation_cost'])
    legal_costs = st.sidebar.number_input("Legal Costs (€)", value=DEFAULT_VALUES['legal_costs'])
    cloud_app_costs = st.sidebar.number_input("Cloud and App Costs (€)", value=DEFAULT_VALUES['cloud_app_costs'])
    screening_cost = st.sidebar.number_input("Screening Cost (€)", value=DEFAULT_VALUES['screening_cost'])
    salary_cost = st.sidebar.number_input("Salary Cost (€)", value=DEFAULT_VALUES['salary_cost'])

    # Retrieve the number of transactions from session state
    num_residential_transactions = st.session_state.get('potential_residential_tenants', 0)
    num_commercial_transactions = st.session_state.get('potential_commercial_tenants', 0)

    # Calculate costs
    costs = calculate_costs(
        sepa_fee, credit_card_fee_percentage, credit_card_fee_fixed, insurance_cost_percentage,
        customer_support_cost, marketing_sales_cost, infrastructure_it_cost, training_development_cost,
        depreciation_cost, legal_costs, cloud_app_costs, screening_cost, salary_cost,
        num_residential_transactions, num_commercial_transactions, credit_card_usage_rate,
        DEFAULT_VALUES['avg_rent_residential'], DEFAULT_VALUES['avg_rent_commercial']
    )

    # Display cost analysis results
    st.write(f"**Total SEPA Cost:** €{costs['total_sepa_cost']:.2f}")
    st.write(f"**Total Credit Card Fees:** €{costs['total_credit_card_fee']:.2f}")
    st.write(f"**Total Insurance Cost:** €{costs['total_insurance_cost']:.2f}")
    st.write(f"**Total Screening Cost:** €{costs['total_screening_cost']:.2f}")
    st.write(f"**Customer Support Cost:** €{DEFAULT_VALUES['customer_support_cost']:.2f}")
    st.write(f"**Marketing and Sales Cost:** €{DEFAULT_VALUES['marketing_sales_cost']:.2f}")
    st.write(f"**Infrastructure and IT Cost:** €{DEFAULT_VALUES['infrastructure_it_cost']:.2f}")
    st.write(f"**Training and Development Cost:** €{DEFAULT_VALUES['training_development_cost']:.2f}")
    st.write(f"**Depreciation Cost:** €{DEFAULT_VALUES['depreciation_cost']:.2f}")
    st.write(f"**Legal Costs:** €{DEFAULT_VALUES['legal_costs']:.2f}")
    st.write(f"**Cloud and App Costs:** €{DEFAULT_VALUES['cloud_app_costs']:.2f}")
    st.write(f"**Total Costs:** €{costs['total_costs']:.2f}")
    
    # Labels and values for cost distribution
    cost_labels = ['SEPA Fees', 'Credit Card Fees', 'Insurance Cost', 'Screening Cost', 'Customer Support', 'Marketing & Sales', 'IT Infrastructure', 
                   'Training & Development', 'Depreciation', 'Legal Costs', 'Cloud & Apps', 'Salaries']
    
    cost_values = [
        costs['total_sepa_cost'], costs['total_credit_card_fee'], costs['total_insurance_cost'], 
        costs['total_screening_cost'], customer_support_cost, marketing_sales_cost, infrastructure_it_cost, 
        training_development_cost, depreciation_cost, legal_costs, cloud_app_costs, salary_cost
    ]

    # Create a Bar Chart for Cost Distribution
    fig, ax = plt.subplots()
    ax.bar(cost_labels, cost_values, color=plt.cm.Paired.colors)

    ax.set_ylabel('Costs (€)')
    ax.set_title('Cost Distribution')

    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)
    
