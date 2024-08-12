import random


query = """
query QueryValidacaoPriceB2CEmerson(
    $condition: String!,
    $zip_code: String!,
    $sku_code: [String!],
    $sales_region: String,
    $sales_organization_code:[String!]
) {
    get_price(
    filters: {condition: $condition
    sales_region_code: $sales_region
    sales_organization_code: $sales_organization_code
    zip_code: $zip_code
    sku_code: $sku_code
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
                activity_sector
                buyer_code
                buyer_identifier
                distribution_channel_code
                payment_condition
                material_type_size_agregator {
                  kilograms {
                    brl {
                      currency_name
                      price_itens {
                        item_category_agregator {
                          item_category_code
                          price_detail {
                            base_price
                            discount_percent
                            discount_price
                            max_price
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
                              tributary_substitution_discount {
                                country
                                tax_percentage
                                tax_value
                              }
                            }
                          }
                        }
                        sku_code
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
"""


all_zip_codes = ["88301-600", "05347-020", "04543-120", "04057-000", "05640-004", "05321-010", "06253-000", "11390-150"]
all_sales_organization_code = ["1688", "1689", "1691", "1693", "1694", "1698", "1699", "1705"]
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


selected_zip_code = random.choice(all_zip_codes)
selected_sales_organization_code = random.sample(all_sales_organization_code, random.randint(1, 3))
selected_sku_codes = random.sample(all_sku_codes, random.randint(1, 10))


variables = {
    "zip_code": selected_zip_code,
    "condition": "YB2B",
    "sales_organization_code": selected_sales_organization_code,
    "sales_document_type":"YB2C",
	"sku_code": selected_sku_codes
}