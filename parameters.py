# parameters.py

# # Default values for calculations
# DEFAULT_VALUES = {
#     'percentage_commercial': 20.0,
#     'adoption_rate_residential': 5.0,
#     'adoption_rate_commercial': 5.0,
#     'fee_rate': 4.0,
#     'avg_rent_residential': 600,
#     'avg_rent_commercial': 1000,
#     'credit_card_additional_fee': 1.6,
#     'tenant_screening_fee': 5,
#     'percentage_screening': 50.0,
#     'sepa_fee': 3.0,
#     'credit_card_fee_percentage': 1.4,
#     'credit_card_fee_fixed': 0.35,
#     'insurance_cost_percentage': 0.7,
#     'customer_support_cost': 5000,
#     'marketing_sales_cost': 10000,
#     'infrastructure_it_cost': 8000,
#     'training_development_cost': 3000,
#     'depreciation_cost': 2000,
#     'legal_costs': 1500,
#     'cloud_app_costs': 4000,
#     'screening_cost': 2.0,
#     'salary_cost': 60000
# }

# def calculate_market_size_revenue(
#     percentage_commercial, adoption_rate_residential, adoption_rate_commercial,
#     fee_rate, avg_rent_residential, avg_rent_commercial, credit_card_additional_fee,
#     tenant_screening_fee, percentage_screening
# ):
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
    
#     return {
#         'total_households': total_households,
#         'rental_households': rental_households,
#         'commercial_properties': commercial_properties,
#         'residential_properties': residential_properties,
#         'potential_residential_tenants': potential_residential_tenants,
#         'potential_commercial_tenants': potential_commercial_tenants,
#         'revenue_residential_landlords': revenue_residential_landlords,
#         'revenue_commercial_landlords': revenue_commercial_landlords,
#         'revenue_credit_card_residential': revenue_credit_card_residential,
#         'revenue_credit_card_commercial': revenue_credit_card_commercial,
#         'revenue_tenant_screening_residential': revenue_tenant_screening_residential,
#         'revenue_tenant_screening_commercial': revenue_tenant_screening_commercial,
#         'total_revenue': total_revenue
#     }

# def calculate_costs(
#     sepa_fee, credit_card_fee_percentage, credit_card_fee_fixed, insurance_cost_percentage,
#     customer_support_cost, marketing_sales_cost, infrastructure_it_cost, training_development_cost,
#     depreciation_cost, legal_costs, cloud_app_costs, screening_cost, salary_cost,
#     potential_residential_tenants, potential_commercial_tenants, avg_rent_residential, avg_rent_commercial
# ):
#     num_residential_transactions = potential_residential_tenants
#     num_commercial_transactions = potential_commercial_tenants

#     total_sepa_cost = sepa_fee * (num_residential_transactions + num_commercial_transactions)
#     total_credit_card_fee = (credit_card_fee_percentage / 100) * (avg_rent_residential * num_residential_transactions + avg_rent_commercial * num_commercial_transactions) + credit_card_fee_fixed * (num_residential_transactions + num_commercial_transactions)
#     total_insurance_cost = (insurance_cost_percentage / 100) * (avg_rent_residential * num_residential_transactions + avg_rent_commercial * num_commercial_transactions)
#     total_screening_cost = screening_cost * (num_residential_transactions + num_commercial_transactions)

#     total_costs = total_sepa_cost + total_credit_card_fee + total_insurance_cost + total_screening_cost + customer_support_cost + marketing_sales_cost + infrastructure_it_cost + training_development_cost + depreciation_cost + legal_costs + cloud_app_costs + salary_cost

#     return {
#         'total_sepa_cost': total_sepa_cost,
#         'total_credit_card_fee': total_credit_card_fee,
#         'total_insurance_cost': total_insurance_cost,
#         'total_screening_cost': total_screening_cost,
#         'total_costs': total_costs
#     }
    
# DEFAULT_VALUES = {
#     'percentage_commercial': 20.0, # Percentage of commercial properties in the market (default: 20%) 
#     'adoption_rate_residential': 5.0, 
#     'adoption_rate_commercial': 5.0,
#     'fee_rate': 4.0, # Fee rate charged to landlords (default: 4%)
#     'avg_rent_residential': 600, # Average rent for residential properties (default: €600)
#     'avg_rent_commercial': 1000, # Average rent for commercial properties (default: €1000)
#     'credit_card_additional_fee': 1.6, # Additional fee charged to tenants for credit card payments (default: 1.6%)
#     'credit_card_usage_rate': 20.0, # Percentage of tenants using credit card payments (default: 20%)
#     'tenant_screening_fee': 5, # Fee charged to tenants for tenant screening (default: €5)
#     'percentage_screening': 50.0, # Percentage of tenants using tenant screening (default: 50%)
#     'sepa_fee': 3.0, # Fee charged for SEPA transactions (default: €3)
#     'credit_card_fee_percentage': 1.4, # Percentage fee charged for credit card transactions (default: 1.4%) 
#     'insurance_cost_percentage': 0.7, # Percentage of insurance cost based on total rent (default: 0.7%)
#     'customer_support_cost': 5000, # Monthly cost for customer support (default: €5000)
#     'marketing_sales_cost': 10000, # Monthly cost for marketing and sales (default: €10000)
#     'infrastructure_it_cost': 8000, # Monthly cost for infrastructure and IT (default: €8000)
#     'training_development_cost': 3000, # Monthly cost for training and development (default: €3000)
#     'depreciation_cost': 3000, # Monthly cost for depreciation (default: €2000)
#     'legal_costs': 1500, # Monthly legal costs (default: €1500)
#     'cloud_app_costs': 4000, # Monthly cost for cloud and other applications (default: €4000)
#     'screening_cost': 2.0, # Cost for tenant screening (default: €2)
#     'salary_cost': 210000 # Monthly salary cost (default: €210000)
# }


# Default values for market size calculations
DEFAULT_MARKET_VALUES = { 
    'total_households': 4332447, # Total number of households in the market
    'rental_households': 1299176, # Total number of rental households in the market
    'percentage_commercial': 20.0, # Percentage of commercial properties in the market (default: 20%)
    'adoption_rate_residential': 5.0, # Adoption rate for residential properties (default: 5%)
    'adoption_rate_commercial': 5.0, # Adoption rate for commercial properties (default: 5%)
    'percentage_screening': 50.0, # Percentage of tenants using tenant screening (default: 50%)
    'credit_card_usage_rate': 20.0, # Percentage of tenants using credit card payments (default: 20%)
    'avg_rent_residential': 600, # Average rent for residential properties (default: €600)
    'avg_rent_commercial': 1000, # Average rent for commercial properties (default: €1000)
}

# Default values for revenue calculations
DEFAULT_REVENUE_VALUES = { 
    'fee_rate': 4.0, # Fee rate charged to landlords (default: 4%)
    'credit_card_additional_fee': 1.6, # Additional fee charged to tenants for credit card payments (default: 1.6%)
    'tenant_screening_fee': 5 # Fee charged to tenants for tenant screening (default: €5)
}

DEFAULT_FIX_COSTS_VALUES = { # Default values for FIX cost calculations
    'sepa_fee': 3.0, # Fee charged per SEPA transactions (default: €3)
    'credit_card_fee_percentage': 1.4, # Percentage fee charged for credit card transactions (default: 1.4%)
    'insurance_cost_percentage': 0.7, # Percentage of insurance cost based on total rent (default: 0.7%)
    'customer_support_cost': 8000, # Monthly cost for customer support for the target market (default: €8000)
    'marketing_sales_cost': 10000, # Monthly cost for marketing and sales for the target market(default: €10000)
    'infrastructure_it_cost': 8000, # Monthly cost for infrastructure and IT (default: €8000)
    'training_development_cost': 3000, # Monthly cost for training and development (default: €3000)
    'depreciation_cost': 3000, # Monthly cost for depreciation (default: €2000)
    'legal_costs': 1500, # Monthly legal costs (default: €1500)
    'cloud_storage_data_transfer_costs': 3000, # Monthly cost for cloud and other applications (default: €4000)
    'screening_cost': 2.0, # Cost for tenant screening (default: €2)
    'salary_cost': 210000, # Annual salary cost (default: €210000)
    'legal_costs': 1500, # Monthly legal costs (default: €1500)
    'heroku_cost': 0.02 # Monthly cost per customer for Heroku (default: €0.02)
}

# Functions with rounding to 2 decimal places
def calculate_market_size( # Function to calculate market size
    total_households, rental_households, percentage_commercial, adoption_rate_residential,
    adoption_rate_commercial, percentage_screening, credit_card_usage_rate
):
    commercial_properties = (percentage_commercial / 100) * rental_households # Calculate number of commercial properties
    residential_properties = rental_households # Calculate number of residential properties
    
    potential_residential_tenants = (adoption_rate_residential / 100) * residential_properties # Calculate potential residential tenants
    potential_commercial_tenants = (adoption_rate_commercial / 100) * commercial_properties # Calculate potential commercial tenants
    
    target_market_size = potential_commercial_tenants + potential_residential_tenants # Calculate target market size
    
    return { # Return dictionary with calculated values
        'commercial_properties': round(commercial_properties, 2),
        'residential_properties': round(residential_properties, 2),
        'potential_residential_tenants': round(potential_residential_tenants, 2),
        'potential_commercial_tenants': round(potential_commercial_tenants, 2),
        'target_market_size': round(target_market_size, 2)
    }
    
def calculate_revenue( # Function to calculate revenue
    fee_rate, credit_card_additional_fee, tenant_screening_fee, avg_rent_residential, avg_rent_commercial,
    potential_residential_tenants, potential_commercial_tenants, credit_card_usage_rate, percentage_screening
):
    
    revenue_residential_landlords = avg_rent_residential * (fee_rate / 100) * 12 * potential_residential_tenants # Calculate revenue from residential landlords
    revenue_commercial_landlords = avg_rent_commercial * (fee_rate / 100) * 12 * potential_commercial_tenants # Calculate revenue from commercial landlords
    
    revenue_credit_card_residential = avg_rent_residential * (credit_card_additional_fee / 100) * 12 * potential_residential_tenants * (credit_card_usage_rate / 100) # Calculate revenue from credit card payments for residential properties
    revenue_credit_card_commercial = avg_rent_commercial * (credit_card_additional_fee / 100) * 12 * potential_commercial_tenants * (credit_card_usage_rate / 100) # Calculate revenue from credit card payments for commercial properties
    
    revenue_tenant_screening_residential = tenant_screening_fee * (percentage_screening / 100) * potential_residential_tenants # Calculate revenue from tenant screening for residential properties
    revenue_tenant_screening_commercial = tenant_screening_fee * (percentage_screening / 100) * potential_commercial_tenants # Calculate revenue from tenant screening for commercial properties
    
    total_revenue = (revenue_residential_landlords + revenue_commercial_landlords + # Calculate total revenue
                     revenue_credit_card_residential + revenue_credit_card_commercial +
                     revenue_tenant_screening_residential + revenue_tenant_screening_commercial)
    
    return { # Return dictionary with calculated values
        'revenue_residential_landlords': round(revenue_residential_landlords, 2),
        'revenue_commercial_landlords': round(revenue_commercial_landlords, 2),
        'revenue_credit_card_residential': round(revenue_credit_card_residential, 2),
        'revenue_credit_card_commercial': round(revenue_credit_card_commercial, 2),
        'revenue_tenant_screening_residential': round(revenue_tenant_screening_residential, 2),
        'revenue_tenant_screening_commercial': round(revenue_tenant_screening_commercial, 2),
        'total_revenue': round(total_revenue, 2)
    }
    
def calculate_fix_costs( # Function to calculate fix costs
                        customer_support_cost, marketing_sales_cost, infrastructure_it_cost, training_development_cost,
                        depreciation_cost, legal_costs, cloud_app_costs, salary_cost                      
):
    total_fix_costs = (customer_support_cost + marketing_sales_cost + infrastructure_it_cost + # Calculate total fixed costs
                       training_development_cost + depreciation_cost + legal_costs + cloud_app_costs + salary_cost)
    
    return { # Return dictionary with calculated values
        'total_fix_costs': round(total_fix_costs, 2)
    }
    
def calculate_variable_costs( # Function to calculate variable costs
    sepa_fee, credit_card_fee_percentage, insurance_cost_percentage, screening_cost,
    potential_residential_tenants, potential_commercial_tenants, avg_rent_residential, avg_rent_commercial,
    credit_card_usage_rate, percentage_screening
):
    
    total_sepa_cost = sepa_fee * (potential_residential_tenants + potential_commercial_tenants) # Calculate total SEPA cost
    total_credit_card_fee = ((credit_card_fee_percentage / 100) * (avg_rent_residential * potential_residential_tenants + avg_rent_commercial * potential_commercial_tenants) * (credit_card_usage_rate / 100)) # Calculate total credit card fee
    total_insurance_cost = (insurance_cost_percentage / 100) * (avg_rent_residential * potential_residential_tenants + avg_rent_commercial * potential_commercial_tenants) # Calculate total insurance cost
    total_screening_cost = screening_cost * (potential_residential_tenants + potential_commercial_tenants) * (percentage_screening / 100) # Calculate total screening cost
    
    total_variable_costs = (total_sepa_cost + total_credit_card_fee + total_insurance_cost + total_screening_cost) # Calculate total variable costs
    
    return { # Return dictionary with calculated values
        'total_sepa_cost': round(total_sepa_cost, 2),
        'total_credit_card_fee': round(total_credit_card_fee, 2),
        'total_insurance_cost': round(total_insurance_cost, 2),
        'total_screening_cost': round(total_screening_cost, 2),
        'total_variable_costs': round(total_variable_costs, 2)
    }
    
#     sepa_fee, credit_card_fee_percentage, insurance_cost_percentage,
#     customer_support_cost, marketing_sales_cost, infrastructure_it_cost, training_development_cost,
#     depreciation_cost, legal_costs, cloud_app_costs, screening_cost, salary_cost,
#     potential_residential_tenants, potential_commercial_tenants, avg_rent_residential, avg_rent_commercial, credit_card_usage_rate, percentage_screening
# ):
#     num_residential_transactions = potential_residential_tenants # Calculate number of residential transactions
#     num_commercial_transactions = potential_commercial_tenants # Calculate number of commercial transactions
#     total_transactions = num_residential_transactions + num_commercial_transactions # Calculate total number of transactions
    
#     total_sepa_cost = sepa_fee * (num_residential_transactions + num_commercial_transactions) # Calculate total SEPA cost
#     total_credit_card_fee = ((credit_card_fee_percentage / 100) * (total_transactions * (credit_card_usage_rate / 100))) # Calculate total credit card fee
#     total_insurance_cost = (insurance_cost_percentage / 100) * (avg_rent_residential * num_residential_transactions + avg_rent_commercial * num_commercial_transactions) # Calculate total insurance cost
#     total_screening_cost = screening_cost * (num_residential_transactions + num_commercial_transactions) * (percentage_screening / 100) # Calculate total screening cost
    
#     total_costs = (total_sepa_cost + total_credit_card_fee + total_insurance_cost + total_screening_cost + # Calculate total costs
#                    customer_support_cost + marketing_sales_cost + infrastructure_it_cost +
#                    training_development_cost + depreciation_cost + legal_costs + cloud_app_costs + salary_cost)
    
#     return { # Return dictionary with calculated values
#         'total_sepa_cost': round(total_sepa_cost, 2),
#         'total_credit_card_fee': round(total_credit_card_fee, 2),
#         'total_insurance_cost': round(total_insurance_cost, 2),
#         'total_screening_cost': round(total_screening_cost, 2),
#         'total_costs': round(total_costs, 2)
#     }

# # Functions with rounding to 2 decimal places
# def calculate_market_size_revenue(
#     percentage_commercial, adoption_rate_residential, adoption_rate_commercial,
#     fee_rate, avg_rent_residential, avg_rent_commercial, credit_card_additional_fee,
#     tenant_screening_fee, percentage_screening
# ):
#     total_households = 4332447
#     rental_households = 1299176
#     commercial_properties = round((percentage_commercial / 100) * rental_households, 2)
#     residential_properties = round(rental_households, 2)

#     potential_residential_tenants = round((adoption_rate_residential / 100) * residential_properties, 2)
#     potential_commercial_tenants = round((adoption_rate_commercial / 100) * commercial_properties, 2)

#     revenue_residential_landlords = round(avg_rent_residential * (fee_rate / 100) * 12 * potential_residential_tenants, 2)
#     revenue_commercial_landlords = round(avg_rent_commercial * (fee_rate / 100) * 12 * potential_commercial_tenants, 2)

#     revenue_credit_card_residential = round(avg_rent_residential * (credit_card_additional_fee / 100) * 12 * potential_residential_tenants * (credit_card_usage_rate / 100), 2)
#     revenue_credit_card_commercial = round(avg_rent_commercial * (credit_card_additional_fee / 100) * 12 * potential_commercial_tenants * (credit_card_usage_rate / 100), 2)

#     revenue_tenant_screening_residential = round(tenant_screening_fee * (percentage_screening / 100) * potential_residential_tenants, 2)
#     revenue_tenant_screening_commercial = round(tenant_screening_fee * (percentage_screening / 100) * potential_commercial_tenants, 2)

#     total_revenue = round((revenue_residential_landlords + revenue_commercial_landlords +
#                      revenue_credit_card_residential + revenue_credit_card_commercial +
#                      revenue_tenant_screening_residential + revenue_tenant_screening_commercial), 2)
    
#     return {
#         'total_households': total_households,
#         'rental_households': rental_households,
#         'commercial_properties': commercial_properties,
#         'residential_properties': residential_properties,
#         'potential_residential_tenants': potential_residential_tenants,
#         'potential_commercial_tenants': potential_commercial_tenants,
#         'revenue_residential_landlords': revenue_residential_landlords,
#         'revenue_commercial_landlords': revenue_commercial_landlords,
#         'revenue_credit_card_residential': revenue_credit_card_residential,
#         'revenue_credit_card_commercial': revenue_credit_card_commercial,
#         'revenue_tenant_screening_residential': revenue_tenant_screening_residential,
#         'revenue_tenant_screening_commercial': revenue_tenant_screening_commercial,
#         'total_revenue': total_revenue
#     }

# def calculate_costs(
#     sepa_fee, credit_card_fee_percentage, credit_card_fee_fixed, insurance_cost_percentage,
#     customer_support_cost, marketing_sales_cost, infrastructure_it_cost, training_development_cost,
#     depreciation_cost, legal_costs, cloud_app_costs, screening_cost, salary_cost,
#     potential_residential_tenants, potential_commercial_tenants, avg_rent_residential, avg_rent_commercial, credit_card_usage_rate
# ):
#     num_residential_transactions = potential_residential_tenants
#     num_commercial_transactions = potential_commercial_tenants
#     total_transactions = num_residential_transactions + num_commercial_transactions

#     total_sepa_cost = round(sepa_fee * (num_residential_transactions + num_commercial_transactions), 2)
#     total_credit_card_fee = round(((credit_card_fee_percentage / 100) * (total_transactions * (credit_card_usage_rate / 100))) - ((total_transactions * (credit_card_usage_rate / 100) ) * credit_card_fee_fixed), 2)
#     total_insurance_cost = round((insurance_cost_percentage / 100) * (avg_rent_residential * num_residential_transactions + avg_rent_commercial * num_commercial_transactions), 2)
#     total_screening_cost = round(screening_cost * (num_residential_transactions + num_commercial_transactions), 2)

#     total_costs = round(total_sepa_cost + total_credit_card_fee + total_insurance_cost + total_screening_cost + customer_support_cost + marketing_sales_cost + infrastructure_it_cost + training_development_cost + depreciation_cost + legal_costs + cloud_app_costs + salary_cost, 2)

#     return {
#         'total_sepa_cost': total_sepa_cost,
#         'total_credit_card_fee': total_credit_card_fee,
#         'total_insurance_cost': total_insurance_cost,
#         'total_screening_cost': total_screening_cost,
#         'total_costs': total_costs
#     }