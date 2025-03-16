from MLinBA.Final_MLinBA.Model.Chart.Statistics.base_analyzer import BaseAnalyzer

class BehaviorAnalyzer(BaseAnalyzer):
    def __init__(self, file_path):
        super().__init__(file_path)

    def vehicle_age_distribution(self):
        self.check_data_empty()
        vehicle_age_counts = self.df['Vehicle_Age'].value_counts(normalize=True) * 100
        return {
            "Dưới 1 năm": round(float(vehicle_age_counts.get('< 1 Year', 0)), 2),
            "1-2 năm": round(float(vehicle_age_counts.get('1-2 Year', 0)), 2),
            "Trên 2 năm": round(float(vehicle_age_counts.get('> 2 Years', 0)), 2)
        }

    def vehicle_damage_ratio(self):
        self.check_data_empty()
        damage_ratio = self.df['Vehicle_Damage'].value_counts(normalize=True) * 100
        yes_ratio = float(damage_ratio.get('Yes', 0))
        no_ratio = float(damage_ratio.get('No', 0))
        return {"Từng gặp tổn thất": round(yes_ratio, 2), "Chưa gặp tổn thất": round(no_ratio, 2)}

    def response_ratio(self):
        self.check_data_empty()
        response_ratio = self.df['Response'].value_counts(normalize=True) * 100
        yes_ratio = float(response_ratio.get(1, 0))
        no_ratio = float(response_ratio.get(0, 0))
        return {"Đồng ý mua": round(yes_ratio, 2), "Không đồng ý": round(no_ratio, 2)}