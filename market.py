import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
# Title of the app
st.title("Startup Financial Analysis")

population = 10423054
total_households = 4332447
rental_households = 1299176
commercial_properties = 385000
total_market = rental_households + commercial_properties
households_target_market = rental_households * 0.05
commercial_target_market = commercial_properties * 0.05
total_target_market = round(households_target_market + commercial_target_market)

# Input parameters
st.sidebar.header("Input Parameters")

choice = st.sidebar.radio("Select Option", ["Market", "Revenue", "Costs", "Profit", "Break Even Analysis", "Sensitivity Analysis"])

# Market Parameters
if choice == "Market":
    st.sidebar.markdown("### Market Parameters")
    
    # Initialize session state variables if not already set
    if 'monthly_residencial_rent' not in st.session_state:
        st.session_state.monthly_residencial_rent = None
    if 'monthly_commercial_rent' not in st.session_state:
        st.session_state.monthly_commercial_rent = None

    # Target Market Size
    total_target_market = st.sidebar.number_input("**Target Market Size**", value=round(total_target_market))
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
    
    # Pie chart
    
    labels = ["total market", "target market"]
    sizes = [total_market, total_target_market]
    fig, ax = plt.subplots()
    colors = ['#ff9999','#66b3ff']
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=(0, 0.1))
    ax.axis('equal')
    st.pyplot(fig)
    
    labels = ["Residential", "Commercial"]
    sizes = [households_target_market, commercial_target_market]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
    
    # Save the input parameters in session state
    st.session_state.monthly_residencial_rent = monthly_residencial_rent
    st.session_state.monthly_commercial_rent = monthly_commercial_rent
    st.session_state.total_target_market = total_target_market
    st.session_state.households_target_market = households_target_market
    st.session_state.commercial_target_market = commercial_target_market
    st.session_state.total_market = total_market
    
    
    
# Revenue Parameters

if choice == "Revenue":
    
    st.sidebar.subheader("Revenue Parameters")
        
    # Monthly Fee Rate
    subscription = st.sidebar.number_input("**Monthly charge rate (%)**", value=4) / 100
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
    screening_percentage = st.sidebar.number_input("**Percentage of tenants screened (%)**", value=50) / 100
    st.sidebar.markdown("Percentage of tenants screened (%): The percentage of clients that are screened.")
    
    # Revenue Calculation
    
    # Subscpription revenue
    residencial_revenue = households_target_market * st.session_state.monthly_residencial_rent * subscription
    commercial_revenue = commercial_target_market * st.session_state.monthly_commercial_rent * subscription
    total_subscription_revenue = residencial_revenue + commercial_revenue
    
    # Credit Card revenue
    credit_card_residencial_revenue = households_target_market * st.session_state.monthly_residencial_rent * credit_card_charge_percentage * credit_card_transaction_cost_percentage
    credit_card_commercial_revenue = commercial_target_market * st.session_state.monthly_commercial_rent * credit_card_charge_percentage * credit_card_transaction_cost_percentage
    credit_card_total_revenue = credit_card_residencial_revenue + credit_card_commercial_revenue
    
    # Tenant Screening revenue
    screening_revenue = total_target_market * screening_percentage * screening_charges
    
    # Total Revenue
    total_revenue = total_subscription_revenue + credit_card_total_revenue + screening_revenue
    
    # Save the input parameters in session state
    st.session_state.charge_rate = subscription
    st.session_state.credit_card_charge_percentage = credit_card_charge_percentage
    st.session_state.credit_card_transaction_cost_percentage = credit_card_transaction_cost_percentage
    st.session_state.screening_charges = screening_charges
    st.session_state.screening_percentage = screening_percentage
    st.session_state.credit_card_total_revenue = credit_card_total_revenue
    st.session_state.total_subscription_revenue = total_subscription_revenue
    st.session_state.screening_revenue = screening_revenue
    st.session_state.total_revenue = total_revenue
    st.session_state.residencial_revenue = residencial_revenue
    st.session_state.commercial_revenue = commercial_revenue
    st.session_state.credit_card_residencial_revenue = credit_card_residencial_revenue
    st.session_state.credit_card_commercial_revenue = credit_card_commercial_revenue
    st.session_state.total_subscription_revenue = total_subscription_revenue
    
    
    st.header("Revenue Analysis")
    
    st.write(f"**Subscription rate (%):** {subscription * 100}")
    st.write(f"**Credit Card Fee (%):** {credit_card_charge_percentage * 100}")
    st.write(f"**Percentage of Credit Card Transactions (%):** {credit_card_transaction_cost_percentage * 100}")
    st.write(f"**Tenant Screening charge (€):** {screening_charges}")
    st.write(f"**Percentage of tenants screened (%):** {screening_percentage * 100}")
    st.write(f"**Monthly Rent per Recidencial Property (€):** {st.session_state.monthly_residencial_rent}")
    st.write(f"**Monthly Rent per Commercial Property (€):** {st.session_state.monthly_commercial_rent}")
    st.write(f"**Target Market Size:** {total_target_market:,}")
    
    st.write(f"**Monthly Subscription Residential Revenue:** €{round(households_target_market * st.session_state.monthly_residencial_rent * subscription):,}")
    st.write(f"**Monthly Subscription Commercial Revenue:** €{round(commercial_target_market * st.session_state.monthly_commercial_rent * subscription):,}")
    st.write(f"**Total Subscription Revenue:** €{round(total_target_market * (st.session_state.monthly_residencial_rent + st.session_state.monthly_commercial_rent) * subscription):,}")
    st.write(f"**Total Monthly Credit Card Revenue:** €{round(credit_card_total_revenue):,}")
    st.write(f"**Total Monthly Tenant Screening Revenue:** €{round(screening_revenue):,}")
    
    st.write(f"**Total Monthly Revenue:** €{round(total_revenue):,}")
    
    # Bar chart for revenue sources 
    revenue_sources = ["Subscription", "Credit Card", "Tenant Screening"]
    revenue = [total_subscription_revenue, credit_card_total_revenue, screening_revenue]
    fig, ax = plt.subplots()
    colors = ['#ff9999','#66b3ff', '#99ff99']
    ax.bar(revenue_sources, revenue, color=colors, alpha=0.7)
    st.pyplot(fig)
    
    # Pie chart for revenue sources
    labels = ["Subscription", "Credit Card", "Tenant Screening"]
    sizes = [total_subscription_revenue, credit_card_total_revenue, screening_revenue]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
    
elif choice == "Costs":
    
    credit_card_transaction_cost_percentage = st.session_state.credit_card_transaction_cost_percentage

    st.sidebar.subheader("Cost Parameters")
    
    # SEPA Fee per Transaction
    sepa_cost = st.sidebar.number_input("**SEPA cost per Transaction (€)**", value=3.0)
    st.sidebar.markdown("SEPA cost per Transaction (€): The cost associated with processing each SEPA transaction.")
    
    # Credit Card Cost percentage per Transaction
    credit_card_cost_percentage = st.sidebar.number_input("**Credit Card Cost (%)**", value=1.4) / 100
    st.sidebar.markdown("Credit Card Cost (%): The percentage of the transaction cost for credit card transactions.")
    
    # Insurance Cost Percentage
    client_insurance_cost = st.sidebar.number_input("**Insurance Cost (%)**", value=0.7) / 100
    st.sidebar.markdown("Insurance Cost (%): The percentage of the rent that is used to cover insurance costs.")
    
    # Tenant Screening Cost
    screening_cost = st.sidebar.number_input("**Tenant Screening Cost (€)**", value=2)
    st.sidebar.markdown("Tenant Screening Cost (€): The cost incurred for screening each tenant.")

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
    
    # Monthly Fixed Costs
    office_rent = office_rent
    utilities = utilities
    insurance_costs = insurance_costs
    legal_accounting_costs = legal_accounting_costs
    miscellaneous_costs = miscellaneous_costs
    salary_founders = (annual_salary_founders * number_of_founders) / 12
    salary_additional_staff = (annual_salary_additional_staff * number_of_additional_staff) / 12
    
    # Monthly Variable Costs for target market
    heroku_cost = heroku_cost
    infrastructure_it_cost = infrastructure_it_cost
    customer_support_cost = customer_support_cost
    marketing_sales_cost = marketing_sales_cost
    residencial_insurance_cost = client_insurance_cost * st.session_state.monthly_residencial_rent * households_target_market
    commercial_insurance_cost = client_insurance_cost * st.session_state.monthly_commercial_rent * commercial_target_market
    total_insurance_cost = residencial_insurance_cost + commercial_insurance_cost
    sepa_residencial_cost = sepa_cost * households_target_market
    sepa_commercial_cost = sepa_cost * commercial_target_market
    total_sepa_cost = sepa_residencial_cost + sepa_commercial_cost
    credit_card_residencial_cost = credit_card_cost_percentage * st.session_state.monthly_residencial_rent * credit_card_transaction_cost_percentage * households_target_market
    credit_card_commercial_cost = credit_card_cost_percentage * st.session_state.monthly_commercial_rent * credit_card_transaction_cost_percentage * commercial_target_market
    total_credit_card_cost = credit_card_residencial_cost + credit_card_commercial_cost
    screening_cost = screening_cost * total_target_market * st.session_state.screening_percentage
    
    # Variable Cost per Client
    monthly_variable_cost_per_client = (heroku_cost + infrastructure_it_cost + customer_support_cost + marketing_sales_cost + total_insurance_cost + total_sepa_cost + total_credit_card_cost + screening_cost) / total_target_market

    # Total Monthly Costs
    monthly_total_fixed_costs = office_rent + utilities + insurance_costs + legal_accounting_costs + miscellaneous_costs + salary_founders + salary_additional_staff
    monthly_total_variable_costs = monthly_variable_cost_per_client * total_target_market
    monthly_total_costs = monthly_total_fixed_costs + monthly_total_variable_costs
    
    # Save the input parameters in session state
    st.session_state.sepa_cost = sepa_cost
    st.session_state.credit_card_cost_percentage = credit_card_cost_percentage
    st.session_state.client_insurance_cost = client_insurance_cost
    st.session_state.screening_cost = screening_cost
    st.session_state.heroku_cost = heroku_cost
    st.session_state.infrastructure_it_cost = infrastructure_it_cost
    st.session_state.customer_support_cost = customer_support_cost
    st.session_state.marketing_sales_cost = marketing_sales_cost
    st.session_state.legal_accounting_costs = legal_accounting_costs
    st.session_state.office_rent = office_rent
    st.session_state.utilities = utilities
    st.session_state.insurance_costs = insurance_costs
    st.session_state.miscellaneous_costs = miscellaneous_costs
    st.session_state.annual_salary_founders = annual_salary_founders
    st.session_state.number_of_founders = number_of_founders
    st.session_state.annual_salary_additional_staff = annual_salary_additional_staff
    st.session_state.number_of_additional_staff = number_of_additional_staff
    st.session_state.total_fixed_costs = monthly_total_fixed_costs
    st.session_state.total_variable_costs = monthly_total_variable_costs
    st.session_state.total_costs = monthly_total_costs
    st.session_state.variable_cost_per_client = monthly_variable_cost_per_client
    st.session_state.total_sepa_cost = total_sepa_cost
    st.session_state.total_credit_card_cost = total_credit_card_cost
    st.session_state.total_insurance_cost = total_insurance_cost
    st.session_state.sepa_residencial_cost = sepa_residencial_cost
    st.session_state.sepa_commercial_cost = sepa_commercial_cost
    st.session_state.credit_card_residencial_cost = credit_card_residencial_cost
    st.session_state.credit_card_commercial_cost = credit_card_commercial_cost
    st.session_state.residencial_insurance_cost = residencial_insurance_cost
    st.session_state.commercial_insurance_cost = commercial_insurance_cost
    st.session_state.total_sepa_cost = total_sepa_cost
    st.session_state.total_credit_card_cost = total_credit_card_cost
    st.session_state.screening_cost = screening_cost
    
    st.header("Cost Analysis")
    
    st.write(f"**Total Monthly Fixed Costs:** €{round(monthly_total_fixed_costs):,}")
    st.write(f"**Total Monthly Variable Costs:** €{round(monthly_total_variable_costs):,}")
    
    st.write(f"**Total Monthly Costs:** €{round(monthly_total_costs):,}")
    
    # Bar chart for costs, title = "Monthly Costs"
    costs = ["Fixed Costs", "Variable Costs"]
    amounts = [monthly_total_fixed_costs, monthly_total_variable_costs]
    fig, ax = plt.subplots()
    colors = ['#ff9999','#66b3ff']
    ax.bar(costs, amounts, color=colors, alpha=0.7)
    ax.set_title("Monthly Costs")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)
    
    # Pie chart for costs
    labels = ["Fixed Costs", "Variable Costs"]
    sizes = [monthly_total_fixed_costs, monthly_total_variable_costs]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title("Monthly Costs")
    st.pyplot(fig)
    
    # pie chart for variable costs
    labels = ["SEPA", "Credit Card", "Insurance", "Screening"]
    sizes = [total_sepa_cost, total_credit_card_cost, total_insurance_cost, screening_cost]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title("Variable Costs")
    st.pyplot(fig)
    
    # bar chart for variable costs
    variable_costs = ["SEPA", "Credit Card", "Insurance", "Screening"]
    amounts = [total_sepa_cost, total_credit_card_cost, total_insurance_cost, screening_cost]
    fig, ax = plt.subplots()
    colors = ['#ff9999','#66b3ff', '#99ff99', '#ffcc99']
    ax.bar(variable_costs, amounts, color=colors, alpha=0.7)
    ax.set_title("Variable Costs")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)
    
    
    # pie chart for fixed costs
    labels = ["Office Rent", "Utilities", "Insurance", "Legal & Accounting", "Miscellaneous", "Salaries"]
    sizes = [office_rent, utilities, insurance_costs, legal_accounting_costs, miscellaneous_costs, salary_founders + salary_additional_staff]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', counterclock=False, pctdistance=0.85)
    ax.axis('equal')
    ax.set_title("Fixed Costs")
    st.pyplot(fig)
    
    # bar chart for fixed costs
    fixed_costs = ["Office Rent", "Utilities", "Insurance", "Legal & Accounting", "Miscellaneous", "Salaries"]
    amounts = [office_rent, utilities, insurance_costs, legal_accounting_costs, miscellaneous_costs, salary_founders + salary_additional_staff]
    fig, ax = plt.subplots()
    colors = ['#ff9999','#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
    ax.bar(fixed_costs, amounts, color=colors, alpha=0.7)
    ax.set_title("Fixed Costs")
    st.pyplot(fig)
    
elif choice == "Profit":
    st.header("Profit Analysis")
    
    # Calculate Profit
    total_revenue = st.session_state.total_revenue
    monthly_total_costs = st.session_state.total_costs
    total_profit = total_revenue - monthly_total_costs
    variable_costs = st.session_state.total_variable_costs
    fixed_costs = st.session_state.total_fixed_costs
    monthly_variable_cost_per_client = st.session_state.variable_cost_per_client
    total_subscription_revenue = st.session_state.total_subscription_revenue
    credit_card_total_revenue = st.session_state.credit_card_total_revenue
    screening_revenue = st.session_state.screening_revenue
    residencial_revenue = st.session_state.residencial_revenue
    commercial_revenue = st.session_state.commercial_revenue
    credit_card_residencial_revenue = st.session_state.credit_card_residencial_revenue
    credit_card_commercial_revenue = st.session_state.credit_card_commercial_revenue
    total_insurance_cost = st.session_state.total_insurance_cost
    total_sepa_cost = st.session_state.total_sepa_cost
    total_credit_card_cost = st.session_state.total_credit_card_cost
    screening_cost = st.session_state.screening_cost
    sepa_residencial_cost = st.session_state.sepa_residencial_cost
    sepa_commercial_cost = st.session_state.sepa_commercial_cost
    credit_card_residencial_cost = st.session_state.credit_card_residencial_cost
    credit_card_commercial_cost = st.session_state.credit_card_commercial_cost
    residencial_insurance_cost = st.session_state.residencial_insurance_cost
    commercial_insurance_cost = st.session_state.commercial_insurance_cost
    
    
    # Calculate Profit Margin
    profit_margin = (total_profit / total_revenue) * 100
    
    # Display Revenue
    
    subscription_cost = total_sepa_cost + total_insurance_cost
    
    # Display Profit
    st.write(f"**Total Monthly Revenue:** €{round(total_revenue):,}")
    st.write(f"**Total Monthly Costs:** €{round(monthly_total_costs):,}")
    st.write(f"**Total Monthly Profit:** €{round(total_profit):,}")
    st.write(f"**Profit Margin:** {round(profit_margin, 2)}%")
    
    # Bar chart for profit and costs
    amounts = [total_revenue, monthly_total_costs, total_profit]
    labels = ["Total Revenue", "Total Costs", "Total Profit"]
    fig, ax = plt.subplots()
    colors = ['#ff9999','#66b3ff', '#99ff99']
    ax.bar(labels, amounts, color=colors, alpha=0.7)
    ax.set_title("Profit and Costs")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)
    
    # Bar chart for revenue streams and their costs

    labels = ["Subscription", "Credit Card", "Tenant Screening"]
    revenues = [total_subscription_revenue, credit_card_total_revenue, screening_revenue]
    costs = [subscription_cost, total_credit_card_cost, screening_cost]

    # Define the positions for the bars on the x-axis
    x = np.arange(len(labels))

    # Set the width of the bars
    width = 0.35

    # Create subplots
    fig, ax = plt.subplots()

    # Plot revenues
    ax.bar(x - width/2, revenues, width, label='Revenue', color='#66b3ff', alpha=0.7)

    # Plot costs next to the revenues
    ax.bar(x + width/2, costs, width, label='Cost', color='#ff9999', alpha=0.7)

    # Add labels, title, and formatting
    ax.set_xlabel('Categories')
    ax.set_title('Revenue and Costs by Category')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    plt.xticks(rotation=45, ha='right')

    # Add legend
    ax.legend()

    # Show plot in Streamlit
    st.pyplot(fig)
    
elif choice == "Break Even Analysis":
    
    st.header("Break Even Analysis")
    
    total_customer = total_target_market
    total_revenue_per_customer = st.session_state.total_revenue / total_customer
    monthly_variable_cost_per_client = st.session_state.variable_cost_per_client
    
    # Calculate Break Even Point
    
    break_even_point = st.session_state.total_fixed_costs / (total_revenue_per_customer - monthly_variable_cost_per_client)
        
    st.write(f"**Total Monthly Fixed Costs:** €{round(st.session_state.total_fixed_costs):,}")
    st.write(f"**Total Monthly Variable Costs per Client:** €{round(monthly_variable_cost_per_client):,}")
    st.write(f"**Total Monthly Revenue per Client:** €{round(total_revenue_per_customer):,}")
    st.write(f"**Break Even Point:** {round(break_even_point)} clients")
    
    # generate a line plot for break even analysis
    Clients = np.arange(0, total_customer + 1)
    Revenue = total_revenue_per_customer * Clients
    Fixed_Costs = np.full_like(Clients, st.session_state.total_fixed_costs)
    Variable_Costs = monthly_variable_cost_per_client * Clients
    Total_Costs = Fixed_Costs + Variable_Costs
 
    fig, ax = plt.subplots()
    ax.plot(Clients, Revenue, label='Revenue', color='blue')
    ax.plot(Clients, Fixed_Costs, label='Fixed Costs', color='red')
    ax.plot(Clients, Total_Costs, label='Total_Costs', color='green')
    ax.set_xlabel('Number of Clients')
    ax.set_ylabel('Amount (€)')
    ax.set_title('Break Even Analysis')
    ax.legend()
    st.pyplot(fig)
    

    
    
    
    
    
        
        

        
        
        
        
        