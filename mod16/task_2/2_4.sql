select "customer".full_name, "order".order_no
from "order","customer"
on "order".customer_id = customer.customer_id
where "order".manager_id is null
