from datetime import date
import datetime


process_group_list = ["Group1_ABC", "Group2_XYZ", "Group4_DEF"]
group_id = "Group2"

true_prefix = next((prefix for prefix in process_group_list if prefix.startswith(group_id)), None)

datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
