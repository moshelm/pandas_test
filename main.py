from utils import *


if __name__=='__main__':

    # level 0
    data_json = 'orders_simple.json'
    df = load_json(data_json)

    # level 1
    clean_numbers(df,'total_amount')
    convert_to_numeric(df,'total_amount')
    convert_to_datetime(df,'order_date')

    # level 2
    remove_html_tags(df,'items_html')

    # level 3
    replacing_empty_value(df,'coupon_used')

    # level 4
    df = create_column_order_month(df,'order_date','order_month')

    # level 5
    create_column_high_value_order(df,'total_amount','high_value_order')
    df = sort_data_frame(df,'total_amount',asc=False)

    # level 6
    create_column_rating_by_country(df, 'rating', 'country')

    # level 7
    df = filter_by_rating_amount(df, 'total_amount', 'rating')

    # level 8
    create_column_delivery_status(df,'delivery_status')
