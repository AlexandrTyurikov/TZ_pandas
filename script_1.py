from bitquery import get_swap_prices


def create_csv(token_address, base_address, since, name_csv):
    df = get_swap_prices(token_address, base_address, since)
    df.to_csv(name_csv)


token_address_AAVE = "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9" # AAVE Token
base_address_WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2" # WETH address
since = "2020-10-04"

create_csv(token_address_AAVE, base_address_WETH, since, 'AAVE_ETH_raw.csv')