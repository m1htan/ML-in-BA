from overview_analyzer import OverviewAnalyzer
from behavior_analyzer import BehaviorAnalyzer
from region_analyzer import RegionAnalyzer
from visualization import Visualization

file_path = "/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Dataset/train.csv"

overview_analyzer = OverviewAnalyzer(file_path)
behavior_analyzer = BehaviorAnalyzer(file_path)
region_analyzer = RegionAnalyzer(file_path)
visualizer = Visualization(file_path)

print("=== Trực quan hóa Thống kê tổng quan ===")
visualizer.plot_gender_ratio(overview_analyzer.gender_ratio())

print("\n=== Trực quan hóa Hành vi khách hàng ===")
visualizer.plot_vehicle_age_distribution(behavior_analyzer.vehicle_age_distribution())
visualizer.plot_vehicle_damage_ratio(behavior_analyzer.vehicle_damage_ratio())
visualizer.plot_response_ratio(behavior_analyzer.response_ratio())

print("\n=== Trực quan hóa Phân tích theo khu vực ===")
visualizer.plot_top_regions(region_analyzer.top_regions_by_customers())
visualizer.plot_highest_response_region(region_analyzer.region_with_highest_response())