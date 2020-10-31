from scoring.business import BusinessType


class GridLogic:
    def __init__(self, businessType: BusinessType):
        self.businessType = businessType

    def make_prediction(self):
        ...
