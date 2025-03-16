from MLinBA.Final_MLinBA.Model.Chart.Statistics.base_analyzer import BaseAnalyzer

class RegionAnalyzer(BaseAnalyzer):
    def __init__(self, file_path):
        super().__init__(file_path)

    def top_regions_by_customers(self, top_n=5):
        self.check_data_empty()
        region_counts = self.df['Region_Code'].value_counts().head(top_n)
        total_customers = len(self.df)
        region_ratios = (region_counts / total_customers * 100).round(2)
        return {str(k): float(v) for k, v in region_ratios.to_dict().items()}

    def region_with_highest_response(self):
        self.check_data_empty()
        region_response = self.df.groupby('Region_Code')['Response'].mean() * 100
        highest_region = region_response.idxmax()
        highest_ratio = round(float(region_response[highest_region]), 2)
        return {str(highest_region): highest_ratio}