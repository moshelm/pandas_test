from utils import *
if __name__=='__main__':
    data_json = 'orders_simple.json'
    df = load_json(data_json)
    clean_numbers(df,'total_amount')
    convert_to_datetime(df,'order_date')
    remove_html_tags(df,'items_html')
    replacing_empty_value(df,'coupon_used')
    df = create_column_order_month(df,'order_date','order_month')

    # level 5

    create_column_high_value_order(df,'total_amount','high_value_order')
    df = sort_data_frame(df,'total_amount',asc=False)
