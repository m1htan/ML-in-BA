from MLinBA.Final_MLinBA.Model.Chart.Statistics.base_analyzer import BaseAnalyzer

class OverviewAnalyzer(BaseAnalyzer):
    def __init__(self, file_path):
        super().__init__(file_path)

    def total_customers(self):
        self.check_data_empty()
        return len(self.df)

    def gender_ratio(self):
        self.check_data_empty()
        gender_counts = self.df['Gender'].value_counts(normalize=True) * 100
        male_ratio = float(gender_counts.get('Male', 0))
        female_ratio = float(gender_counts.get('Female', 0))
        return {"Nam": round(male_ratio, 2), "Nữ": round(female_ratio, 2)}

    def average_age(self):
        self.check_data_empty()
        return round(self.df['Age'].mean(), 2)

    def driving_license_ratio(self):
        self.check_data_empty()
        license_ratio = self.df['Driving_License'].value_counts(normalize=True) * 100
        yes_ratio = float(license_ratio.get(1, 0))
        no_ratio = float(license_ratio.get(0, 0))
        return {"Có bằng lái": round(yes_ratio, 2), "Không có bằng lái": round(no_ratio, 2)}

    def previously_insured_ratio(self):
        self.check_data_empty()
        insured_ratio = self.df['Previously_Insured'].value_counts(normalize=True) * 100
        yes_ratio = float(insured_ratio.get(1, 0))
        no_ratio = float(insured_ratio.get(0, 0))
        return {"Đã từng mua": round(yes_ratio, 2), "Chưa từng mua": round(no_ratio, 2)}