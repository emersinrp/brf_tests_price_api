import random

query = """
query QueryValidacaoPriceEmerson(
    $fiscal_code_buyer: [String!],
    $salesmen_code: String,
    $document_id_buyer: [String!],
    $buyer_code: [String!],
    $distribution_channel_code: String!,
    $sales_organization_code: [String!],
    $payment_condition:String!,
    $condition: String!,
    $units_of_measurements: [UnitsOfMeasurements!],
    $currencies: [Currencies!],
    $incoterms: [Incoterms!],
    $sales_document_type: String,
    $item_category_code: [String!],
    $sku_code: [String!],
    $fifo_range: [String!],
) {
    get_price( 
        filters: {
            condition: $condition
            fiscal_code_buyer: $fiscal_code_buyer
            buyer_code: $buyer_code
            salesmen_code: $salesmen_code
            document_id_buyer: $document_id_buyer
            sku_code: $sku_code
            shipment:{
                incoterms: $incoterms,
                country: null
            }
            currencies:$currencies      
            units_of_measurements: $units_of_measurements
            fifo_range: $fifo_range
            payment_code: $payment_condition      
            distribution_channel_code: $distribution_channel_code
            sales_organization_code: $sales_organization_code
            item_category_code: $item_category_code
            sales_document_type: $sales_document_type
            rounded: 6
            pagination_filter: { first: "10000" }
        }
    ) {
        agregators {
            sales_region_agregator {
                sales_region
                sales_organization_agregator {
                    sales_organization
                    price_sales_agregator {
                        edges {
                            cursor
                            node {
                                distribution_channel_code
                                activity_sector
                                buyer_code
                                payment_condition
                                material_type_size_agregator {
                                    kilograms {
                                        brl {
                                            currency_name
                                            price_itens {
                                                sku_code
                                                item_category_agregator {
                                                    item_category_code
                                                    price_detail {
                                                        base_price
                                                        discount_percent
                                                        max_price
                                                        discount_price
                                                        max_price_percentage
                                                        min_price
                                                        min_price_percentage
                                                        payment_percentage
                                                        price
                                                        tributary_substitution_discount_price
                                                        tributary_substitution_price
                                                        taxes {
                                                            icms {
                                                                country
                                                                tax_percentage
                                                                tax_value
                                                            }
                                                            tributary_substitution {
                                                                country
                                                                tax_percentage
                                                                tax_value
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        page_info {
            end_cursor
            has_next_page
            has_previous_page
            start_cursor
        }
    }
}
"""

all_buyer_codes = [
    "0000012272", "0000012265", "0000012285", "0000012287", "0000012297", "0000012299",
    "0000012307", "0000012354", "0000012461", "0000012467", "0000012472", "0000012477",
    "0000012479", "0000012486", "0000012488", "0000012515", "0000012519", "0000012520",
    "0000012524", "0000012535", "0000012560", "0000012566", "0000012581", "0000012609",
    "0000012613", "0000012618", "0000012646", "0000012667", "0000012725", "0000012755",
    "0000012766", "0000012775", "0000012781", "0000012793", "0000012809", "0000044911"
]
all_sku_codes = [
    "000000000000222812", "000000000000222813", "000000000000222814", 
    "000000000000222815", "000000000000222816", "000000000000222817", 
    "000000000000226491", "000000000000237914", "000000000000238058", 
    "000000000000267678", "000000000000270652", "000000000000272205", 
    "000000000000273236", "000000000000276669", "000000000000277770", 
    "000000000000280313", "000000000000286591", "000000000000287113", 
    "000000000000287156", "000000000000288357", "000000000000288500", 
    "000000000000293873", "000000000000293890", "000000000000294748", 
    "000000000000296236", "000000000000300837", "000000000000302767", 
    "000000000000303712", "000000000000305146", "000000000000305669", 
    "000000000000322570", "000000000000322598", "000000000000322600", 
    "000000000000322849", "000000000000330075", "000000000000330130", 
    "000000000000330131", "000000000000330142", "000000000000330250", 
    "000000000000331597", "000000000000335864", "000000000000335879", 
    "000000000000335918", "000000000000338133", "000000000000338150", 
    "000000000000339293", "000000000000339344", "000000000000340308", 
    "000000000000341067"
]
all_currencies = [
    "us_dolar", "chilean_peso", "emirari_dirham", "kwaiti_dinar",
    "argentine_peso", "euro", "omani_rial", "saudia_arabian_riyal",
    "qatari_riyal", "brazilian_real", "pound"
]
all_payment_conditions = ["R005", "R007", "R019"]
all_conditions = ["Y100", "YB2B"]


# Select 1 to 10 random buyer codes
selected_buyer_codes = random.sample(all_buyer_codes, random.randint(1, 10))
selected_sku_codes = random.sample(all_sku_codes, random.randint(1, 10))
selected_currency = random.choice(all_currencies)
selected_payment_condition = random.choice(all_payment_conditions)
selected_condition = random.choice(all_conditions)


variables = {
    "fiscal_code_buyer": None,
    "salesmen_code": None,
    "document_id_buyer": None,
    "buyer_code": selected_buyer_codes,
    "distribution_channel_code": "10",
    "payment_condition": selected_payment_condition,
    "condition": selected_condition,
    "units_of_measurements": None,
    "currencies": selected_currency,
    "sales_document_type": None,
    "item_category_code": None,
    "fifo_range": ["Z100", "Z098", "Z101", "Z102"],
    "sku_code": selected_sku_codes
}
