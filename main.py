from employee.base_employee import BaseEmployee
from employee.sales_employee import SalesEmployee

# Python super

## Introduction to the Python super

## super().__init__()

## Delegating to other methods in the parent class

## Put it all together

if __name__ == "__main__":
  sales_employee = SalesEmployee("John", 5_000, 1_000, 2_000)
  print(sales_employee.get_pay())
