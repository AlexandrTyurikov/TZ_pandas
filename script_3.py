from script_1 import create_csv
from script_2 import normalized_csv


token_address_WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
base_address_USDC = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
base_address_USDT = "0xdac17f958d2ee523a2206206994597c13d831ec7"
since = "2020-10-04"

create_csv(token_address_WETH, base_address_USDC, since, 'WETH_USDC_raw.csv')
create_csv(token_address_WETH, base_address_USDT, since, 'WETH_USDT_raw.csv')

normalized_csv('WETH_USDC_raw.csv', 'WETH_USDC_normalized.csv')
normalized_csv('WETH_USDT_raw.csv', 'WETH_USDT_normalized.csv')
