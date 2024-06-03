from .base_employee import BaseEmployee

class SalesEmployee(BaseEmployee):
  def __init__(self, name, base_pay, bonus, sales_incentive) -> None:
    self.name = name
    self.base_pay = base_pay
    self.bonus = bonus
    self.sales_incentive = sales_incentive

  def get_pay(self):
    return self.base_pay + self.bonus + self.sales_incentive
