import requests
import time

ETHERSCAN_API_KEY = "YourApiKeyToken"
GAS_PRICE_API = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=" + ETHERSCAN_API_KEY

def fetch_gas_prices():
    try:
        response = requests.get(GAS_PRICE_API)
        data = response.json()
        if data['status'] == '1':
            result = data['result']
            print("⛽ Current SafeGasPrice:", result['SafeGasPrice'], "Gwei")
            print("⛽ Current ProposeGasPrice:", result['ProposeGasPrice'], "Gwei")
            print("⛽ Current FastGasPrice:", result['FastGasPrice'], "Gwei")
        else:
            print("⚠️ Error fetching gas prices:", data['message'])
    except Exception as e:
        print("⚠️ Exception occurred:", str(e))

def main():
    print(f"⏰ Gas Price Check at {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}")
    fetch_gas_prices()

if __name__ == "__main__":
    main()
