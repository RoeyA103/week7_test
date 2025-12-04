import pandas as pd
import numpy as np
from utils import *

orders = pd.read_json("orders_simple.json")

orders = data_frame_conversion(orders)

orders.items_html = cleanhtml_column(orders.items_html)

orders.coupon_used = fill_empty_col(orders.coupon_used , "no coupon")

orders = create_ordermonth_col(orders)

orders = create_high_value_order(orders)

orders = sort_by_total_amount(orders)


orders = create_mean_rating_col(orders)


orders = filter_by_amount_rating(orders)

orders = create_delivery_status_col(orders)

orders.to_csv("clean_orders_[315329995].csv")

