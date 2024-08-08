from autoscraper import AutoScraper
import pandas as pd

def create_scraper():
    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    wanted_list = ["Lenovo ThinkPad L570", "$999.00", "3 reviews"]  # Sample data to train the scraper

    scraper = AutoScraper()
    result = scraper.build(url, wanted_list)

    # Get the rules created by AutoScraper
    print(scraper.get_result_similar(url, grouped=True))

    return scraper

def save_data_as_csv(scraper, url, output_file):
    data = scraper.get_result_similar(url, grouped=True)

    # Extract names, prices, and ratings
    names = data.get('Lenovo ThinkPad L570', [])
    prices = data.get('$999.00', [])
    ratings = data.get('3 reviews', [])

    # Ensure all lists have the same length
    min_length = min(len(names), len(prices), len(ratings))
    names = names[:min_length]
    prices = prices[:min_length]
    ratings = ratings[:min_length]

    # Print data to terminal
    for name, price, rating in zip(names, prices, ratings):
        print(f"Name: {name}, Price: {price}, Rating: {rating}")

    # Save data to CSV
    df = pd.DataFrame({'Name': names, 'Price': prices, 'Rating': ratings})
    df.to_csv(output_file, index=False)
    print(f"Data saved as {output_file}")

def main():
    url = "https://www.amazon.in/s?k=laptop+acer&crid=2AWI3W3GUPF72&sprefix=laptop+acer%2Caps%2C239&ref=nb_sb_noss_1"
    scraper = create_scraper()
    save_data_as_csv(scraper, url, 'Riya_The_Webscraper.csv')

if __name__ == "__main__":
    main()
