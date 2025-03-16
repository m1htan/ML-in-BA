from base_analyzer import BaseAnalyzer
import seaborn as sns
import matplotlib.pyplot as plt

class Visualization(BaseAnalyzer):
    def __init__(self, file_path):
        super().__init__(file_path)

    def plot_gender_ratio(self, gender_data):
        self.check_data_empty()
        labels = list(gender_data.keys())
        sizes = list(gender_data.values())
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'])
        plt.title('Tỷ lệ Nam - Nữ')
        plt.show()

    def plot_vehicle_age_distribution(self, age_data):
        self.check_data_empty()
        labels = list(age_data.keys())
        sizes = list(age_data.values())
        plt.figure(figsize=(8, 6))
        sns.barplot(x=labels, y=sizes, palette='Blues')
        plt.title('Phân bố tuổi xe')
        plt.ylabel('Tỷ lệ (%)')
        plt.show()

    def plot_vehicle_damage_ratio(self, damage_data):
        self.check_data_empty()
        labels = list(damage_data.keys())
        sizes = list(damage_data.values())
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#ff9999', '#66b3ff'])
        plt.title('Tỷ lệ tổn thất xe')
        plt.show()

    def plot_response_ratio(self, response_data):
        self.check_data_empty()
        labels = list(response_data.keys())
        sizes = list(response_data.values())
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#ffcc99', '#99ff99'])
        plt.title('Tỷ lệ phản hồi đồng ý mua bảo hiểm')
        plt.show()

    def plot_top_regions(self, region_data):
        self.check_data_empty()
        labels = list(region_data.keys())
        sizes = list(region_data.values())
        plt.figure(figsize=(10, 6))
        sns.barplot(x=labels, y=sizes, palette='viridis')
        plt.title('Top khu vực có nhiều khách hàng nhất')
        plt.ylabel('Tỷ lệ (%)')
        plt.show()

    def plot_highest_response_region(self, region_data):
        self.check_data_empty()
        label = list(region_data.keys())[0]
        value = list(region_data.values())[0]
        plt.figure(figsize=(6, 6))
        plt.pie([value, 100 - value], labels=[f'Khu vực {label}', 'Khác'], autopct='%1.1f%%', colors=['#99ff99', '#ff9999'])
        plt.title(f'Khu vực có tỷ lệ phản hồi cao nhất ({label}: {value}%)')
        plt.show()
