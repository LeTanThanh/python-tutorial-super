from .base_employee import BaseEmployee

class SalesEmployee(BaseEmployee):
  def __init__(self, name, base_pay, bonus, sales_incentive) -> None:
    super().__init__(name, base_pay, bonus)
    self.sales_incentive = sales_incentive

  def get_pay(self):
    return super().get_pay() + self.sales_incentive
