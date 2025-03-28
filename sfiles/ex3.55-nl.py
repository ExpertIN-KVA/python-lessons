def calculate_financial_aid(losses):
    """
    Calculates the financial aid for a company based on its reported losses over four consecutive years.
    
    Args:
    - losses (list of float): A list containing four loss amounts for four years.
    
    Returns:
    - float: The financial aid amount.
    """
    if len(losses) != 4:
        raise ValueError("Exactly four years of losses must be provided.")
    
    max_loss = max(losses)
    min_loss = min(losses)

    # Remove only ONE occurrence of max and min losses
    temp_losses = losses.copy()
    temp_losses.remove(max_loss)
    temp_losses.remove(min_loss)

    # Calculate the average of the remaining two losses
    avg_remaining_losses = sum(temp_losses) / 2
    financial_aid = 0.55 * avg_remaining_losses
    
    return financial_aid

def process_company(company_name, losses):
    """
    Processes a company's losses and calculates the financial aid.
    
    Args:
    - company_name (str): The name of the company.
    - losses (list of float): The losses for four years.
    
    Returns:
    - dict: Contains the company name and financial aid amount.
    """
    financial_aid = calculate_financial_aid(losses)
    return {
        "company_name": company_name,
        "financial_aid": financial_aid
    }

def main():
    # Example: One company's losses for 4 years
    company_name = "Example Corp"
    losses = [5000, 7000, 4000, 6000]  # Example loss values for four years
    
    # Process the company
    aid_info = process_company(company_name, losses)
    
    # Compute additional info
    total_aid = aid_info["financial_aid"] * 1000  # Assuming 1000 companies
    max_loss = max(losses)
    min_loss = min(losses)
    max_difference = max_loss - min_loss

    # Output results
    print(f"Company: {aid_info['company_name']}")
    print(f"Financial Aid Granted: {aid_info['financial_aid']:.2f}")
    print(f"Total Aid Given to All Companies: {total_aid:.2f}")
    print(f"Max Difference in Losses: {max_difference:.2f}")

if __name__ == "__main__":
    main()
