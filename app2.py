import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title("Startup Financial Analysis")

population = 10423054
total_households = 4332447
rental_households = 1299176
commercial_properties = 385000
households_target_market = rental_households * (5 / 100)
commercial_target_market = commercial_properties * (5 / 100)
total_target_market = (households_target_market + commercial_target_market)

# Input parameters
st.sidebar.header("Input Parameters")

choice = st.sidebar.radio("Select Option", ["Market", "Revenue", "Costs", "Profit"])

# Market Parameters
st.sidebar.subheader("Market Parameters")

if choice == "Market":
    st.sidebar.markdown("### Market Parameters")
    
    # Initialize session state variables if not already set
    if 'target_market_size' not in st.session_state:
        st.session_state.target_market_size = None
    if 'monthly_residencial_rent' not in st.session_state:
        st.session_state.monthly_residencial_rent = None
    if 'monthly_commercial_rent' not in st.session_state:
        st.session_state.monthly_commercial_rent = None

    # Target Market Size
    target_market_size = st.sidebar.number_input("**Target Market Size**", value=total_target_market)
    st.sidebar.markdown("Target Market Size: The estimated number of potential clients in the target market.")

    # Estimated Monthly Rent per Residencial Property
    monthly_residencial_rent = st.sidebar.number_input("**Monthly Rent per Client (€)**", value=600)
    st.sidebar.markdown("Monthly Rent per Client (€): The average rent paid by each client per month.")
    
    # Estimated Monthly Rent per Commercial Property
    monthly_commercial_rent = st.sidebar.number_input("**Monthly Rent per Commercial Property (€)**", value=1000)
    st.sidebar.markdown("Monthly Rent per Commercial Property (€): The average rent paid by each commercial client per month.")
    
    st.header("Market Analysis")
    
    st.write("**Population of Greece:** 10,423,054")
    
    st.write("**Total households:** 4,332,447")
    
    st.write("**Rental households:** 1,299,176")
    
    ### Source
    st.write("""Data on the number of households is sourced from the [Hellenic Statistical Authority](https://www.statistics.gr/el/2021-census-res-pop-results) (2021 Census).
      """)
    
    st.write("""**Commercial Properties:**
             Total number of businesses: According to the Hellenic Statistical Authority (ELSTAT), Greece has around 700,000 businesses.
             Percentage of businesses renting properties: Based on trends across European countries, around 50-60% of businesses rent their commercial spaces.
             Using a midpoint estimate of 55%, the number of rental commercial properties in Greece can be estimated as: 385,000""")
    
    st.write(f"As **Target Market Size** we estimate 5% of the total rental market: {total_target_market}")
    st.write(f"**Monthly Rent per Client:** €{monthly_residencial_rent}")
    st.write(f"**Monthly Rent per Commercial Property:** €{monthly_commercial_rent}")
    
    # Plotting the Market Analysis
    labels = ['Total Households', 'Rental Households', 'Commercial Properties']
    sizes = [total_households, rental_households, commercial_properties]
    colors = ['#ff9999','#66b3ff','#99ff99']
    explode = (0.1, 0, 0)
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)
    
    # Plotting the Target Market Analysis
    labels = ['Households Target Market', 'Commercial Target Market']
    sizes = [households_target_market, commercial_target_market]
    colors = ['#ff9999','#66b3ff']
    explode = (0.1, 0)
    
    fig2, ax2 = plt.subplots()
    ax2.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    ax2.axis('equal')
    st.pyplot(fig2)
    
    # Plotting the Target Market Size
    labels = ['Total Target Market', 'Remaining Market']
    sizes = [total_target_market, total_households - total_target_market]
    colors = ['#ff9999','#66b3ff']
    explode = (0.1, 0)
    
    fig3, ax3 = plt.subplots()
    ax3.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    ax3.axis('equal')
    st.pyplot(fig3)
    
elif choice == "Revenue":
    
    # Check if variables are already defined in session state
    if 'target_market_size' not in st.session_state or 'monthly_residencial_rent' or 'monthly_commercial_rent ' not in st.session_state:
        st.warning("Please set the 'Market' parameters first.")
    else:
        target_market_size = st.session_state.target_market_size
        monthly_residencial_rent = st.session_state.monthly_residencial_rent
        monthly_commercial_rent = st.session_state.monthly_commercial_rent
        
    # Monthly Fee Rate
    charge_rate = st.sidebar.number_input("**Monthly charge rate (%)**", value=4) / 100
    st.sidebar.markdown("Monthly charge_rate (%): The percentage of the rent that is charged as a fee to the client.")

    # Credit Card Fee Percentage
    credit_card_charge_percentage = st.sidebar.number_input("**Credit Card Fee (%)**", value=1.6) / 100
    st.sidebar.markdown("Credit Card Fee (%): The percentage fee charged for credit card transactions.")

    # Percentage of Credit Card Transactions
    credit_card_transaction_cost_percentage = st.sidebar.number_input("**Percentage of Credit Card Transactions (%)**", value=20) / 100
    st.sidebar.markdown("Percentage of Credit Card Transactions (%): The proportion of transactions made using credit cards.")

    # Screening charges
    screening_charges = st.sidebar.number_input("**Tenant Screening charge (€)**", value=5)
    st.sidebar.markdown("Tenant Screening charge (€): The charge for screening each tenant.")
    
    # Screening percentage
    screening_percentage = st.sidebar.number_input("**Percentage of clients screened (%)**", value=50) / 100
    st.sidebar.markdown("Percentage of clients screened (%): The percentage of clients that are screened.")
    
    st.header("Revenue Analysis")
    
    st.write(f"**Monthly Fee Rate (%):** {charge_rate * 100}")
    st.write(f"**Credit Card Fee (%):** {credit_card_charge_percentage * 100}")
    st.write(f"**Percentage of Credit Card Transactions (%):** {credit_card_transaction_cost_percentage * 100}")
    st.write(f"**Total Residencial Potential Clients:** {households_target_market}")
    st.write(f"**Total Commercial Potential Clients:** {commercial_target_market}")
    st.write(f"**Total Potential Clients:** {total_target_market}")
    st.write(f"**Monthly Rent per Residencial Client:** €{monthly_residencial_rent}")
    st.write(f"**Monthly Rent per Commercial Property:** €{monthly_commercial_rent}")
    st.write(f"**Monthly Residencial Revenue:** €{households_target_market * monthly_residencial_rent * charge_rate}")
    st.write(f"**Monthly Commercial Revenue:** €{commercial_target_market * monthly_commercial_rent * charge_rate}")
    st.write(f"**Screening charges Revenue:** €{screening_charges*total_target_market*screening_percentage}")
    st.write(f"**Total Monthly Revenue:** €{total_target_market * (monthly_residencial_rent * charge_rate + monthly_commercial_rent * charge_rate) * screening_charges*screening_percentage*total_target_market}")
    
    # Plotting the Revenue Analysis
    labels = ['Residencial Revenue', 'Commercial Revenue']
    sizes = [households_target_market * monthly_residencial_rent * charge_rate, commercial_target_market * monthly_commercial_rent * charge_rate]
    colors = ['#ff9999','#66b3ff']
    explode = (0.1, 0)
    
    fig4, ax4 = plt.subplots()
    ax4.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    ax4.axis('equal')
    st.pyplot(fig4)
    
    # Plotting the Total Revenue Analysis
    labels = ['Total Residencial Revenue', 'Total Commercial Revenue']
    sizes = [households_target_market * monthly_residencial_rent * charge_rate, commercial_target_market * monthly_commercial_rent * charge_rate]
    colors = ['#ff9999','#66b3ff']
    explode = (0.1, 0)
    
    fig5, ax5 = plt.subplots()
    ax5.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    ax5.axis('equal')
    st.pyplot(fig5)
    
elif choice == "Costs":
    
    if 'target_market_size' not in st.session_state or 'monthly_residencial_rent' or 'monthly_commercial_rent ' or 'screening_percentage' not in st.session_state:
        st.warning("Please set the 'Market' parameters first.")
    else:
        target_market_size = st.session_state.target_market_size
        monthly_residencial_rent = st.session_state.monthly_residencial_rent
        monthly_commercial_rent = st.session_state.monthly_commercial_rent
        screening_percentage = st.session_state.screening_percentage
        
    # SEPA Fee per Transaction
    sepa_cost = st.sidebar.number_input("**SEPA cost per Transaction (€)**", value=3.0)
    st.sidebar.markdown("SEPA cost per Transaction (€): The cost associated with processing each SEPA transaction.")
    
    # Credit Card Cost percentage per Transaction
    credit_card_cost_percentage = st.sidebar.number_input("**Credit Card Cost (%)**", value=1.4) / 100
    st.sidebar.markdown("Credit Card Cost (%): The percentage of the transaction cost for credit card transactions.")
    
    # Insurance Cost Percentage
    insurance_cost_percentage = st.sidebar.number_input("**Insurance Cost (%)**", value=0.7) / 100
    st.sidebar.markdown("Insurance Cost (%): The percentage of the rent that is used to cover insurance costs.")

    # Heroku Cost for 100,000 Clients
    heroku_cost = st.sidebar.number_input("**Heroku Cost for 100,000 Clients (€)**", value=1750)
    st.sidebar.markdown("Heroku Cost for 100,000 Clients (€): The monthly cost for hosting on Heroku when you have up to 100,000 clients.")

    # Infrastructure & IT Cost
    low_infrastructure_it_cost = 1000
    high_infrastructure_it_cost = 30000
    infrastructure_it_cost = st.sidebar.slider(
        "**Infrastructure & IT Cost (€)**",
        min_value=low_infrastructure_it_cost,
        max_value=high_infrastructure_it_cost,
        value=(low_infrastructure_it_cost + high_infrastructure_it_cost) // 2,
        step=1000
    )
    st.sidebar.markdown("Infrastructure & IT Cost (€): The monthly cost associated with infrastructure and IT services.")

    # Customer Support Cost
    low_customer_support_cost = 1000
    high_customer_support_cost = 5000
    customer_support_cost = st.sidebar.slider(
        "**Customer Support Cost (€)**",
        min_value=low_customer_support_cost,
        max_value=high_customer_support_cost,
        value=(low_customer_support_cost + high_customer_support_cost) // 2,
        step=100
    )
    st.sidebar.markdown("Customer Support Cost (€): The monthly expenditure for providing customer support services.")

    # Marketing & Sales Cost
    low_marketing_sales_cost = 12000
    high_marketing_sales_cost = 40000
    marketing_sales_cost = st.sidebar.slider(
        "**Marketing & Sales Cost (€)**",
        min_value=low_marketing_sales_cost,
        max_value=high_marketing_sales_cost,
        value=(low_marketing_sales_cost + high_marketing_sales_cost) // 2,
        step=1000
    )
    st.sidebar.markdown("Marketing & Sales Cost (€): The monthly cost for marketing and sales activities.")

    # Legal Costs
    legal_accounting_costs = st.sidebar.number_input("**Legal Costs (€)**", value=2000)
    st.sidebar.markdown("Legal Costs (€): Monthly costs related to legal compliance and services.")

    # Office Rent
    office_rent = st.sidebar.number_input("**Office Rent (€)**", value=2000)
    st.sidebar.markdown("Office Rent (€): The monthly cost of renting office space for the startup.")

    # Utilities
    utilities = st.sidebar.number_input("**Utilities (€)**", value=500)
    st.sidebar.markdown("Utilities (€): The monthly cost of utilities such as electricity, water, and internet.")

    # Insurance Costs
    insurance_costs = st.sidebar.number_input("**Insurance Costs (€)**", value=500)
    st.sidebar.markdown("Insurance Costs (€): The monthly cost of insurance for the startup.")

    # Miscellaneous Costs
    low_miscellaneous_costs = 500
    high_miscellaneous_costs = 2000
    miscellaneous_costs = st.sidebar.slider(
        "**Miscellaneous Costs (€)**",
        min_value=low_miscellaneous_costs,
        max_value=high_miscellaneous_costs,
        value=(low_miscellaneous_costs + high_miscellaneous_costs) // 2,
        step=100
    )
    st.sidebar.markdown("Miscellaneous Costs (€): Additional costs that may not fall into other specific categories.")

    # Tenant Screening Cost
    screening_cost = st.sidebar.number_input("**Tenant Screening Cost (€)**", value=2)
    st.sidebar.markdown("Tenant Screening Cost (€): The cost incurred for screening each tenant.")

    # Annual Salary per Founder
    annual_salary_founders = st.sidebar.number_input("**Annual Salary per Founder (€)**", value=50000)
    st.sidebar.markdown("Annual Salary per Founder (€): The annual salary for each founder of the startup.")

    # Number of Founders
    number_of_founders = st.sidebar.number_input("**Number of Founders**", value=3)
    st.sidebar.markdown("Number of Founders: The total number of founders in the startup.")

    # Annual Salary per Additional Staff
    annual_salary_additional_staff = st.sidebar.slider(
        "**Annual Salary per Additional Staff (€)**",
        min_value=30000,
        max_value=50000,
        value=40000,
        step=1000
    )
    st.sidebar.markdown("Annual Salary per Additional Staff (€): The annual salary for each additional staff member beyond the founders.")

    # Number of Additional Staff
    number_of_additional_staff = st.sidebar.number_input("**Number of Additional Staff**", value=6)
    st.sidebar.markdown("Number of Additional Staff: The total number of additional staff members.")
    
    # Display Costs
    total_fixed_costs = (office_rent + utilities + insurance_costs + legal_accounting_costs + miscellaneous_costs + annual_salary_founders * number_of_founders 
                         + annual_salary_additional_staff * number_of_additional_staff, screening_cost*target_market_size*screening_percentage)
    total_variable_costs = (heroku_cost + infrastructure_it_cost + 
                            customer_support_cost + marketing_sales_cost + insurance_cost_percentage * monthly_residencial_rent + sepa_cost*target_market_size + credit_card_cost_percentage*target_market_size*credit_card_transaction_cost_percentage)
    total_costs = total_fixed_costs + total_variable_costs
    
    st.header("Costs Analysis")
    
    st.write(f"**Insurance Cost (%):** {insurance_cost_percentage * 100}")
    st.write(f"**Heroku Cost for 100,000 Clients (€):** {heroku_cost}")
    st.write(f"**Infrastructure & IT Cost (€):** {infrastructure_it_cost}")
    st.write(f"**Customer Support Cost (€):** {customer_support_cost}")
    st.write(f"**Marketing & Sales Cost (€):** {marketing_sales_cost}")
    st.write(f"**Legal Costs (€):** {legal_accounting_costs}")
    st.write(f"**Office Rent (€):** {office_rent}")
    st.write(f"**Utilities (€):** {utilities}")
    st.write(f"**Insurance Costs (€):** {insurance_costs}")
    st.write(f"**Miscellaneous Costs (€):** {miscellaneous_costs}")
    st.write(f"**Tenant Screening Cost (€):** {screening_cost}")
    st.write(f"**Annual Salary per Founder (€):** {annual_salary_founders}")
    st.write(f"**Number of Founders:** {number_of_founders}")
    st.write(f"**Annual Salary per Additional Staff (€):** {annual_salary_additional_staff}")
    st.write(f"**Number of Additional Staff:** {number_of_additional_staff}")
    st.write(f"**Total Fixed Costs:** €{total_fixed_costs}")
    st.write(f"**Total Variable Costs:** €{total_variable_costs}")
    st.write(f"**Total Costs:** €{total_costs}")
    
    # Plotting the Costs Analysis
    labels = ['Fixed Costs', 'Variable Costs']
    sizes = [total_fixed_costs, total_variable_costs]
    colors = ['#ff9999','#66b3ff']
    explode = (0.1, 0)
    
    fig6, ax6 = plt.subplots()
    ax6.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    ax6.axis('equal')
    st.pyplot(fig6)