import os

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd


class Statistic():
    def __init__(self):
        super().__init__()

    def load_data(self, filepath):
        """Tải dữ liệu từ file CSV hoặc Excel"""
        if filepath:
            self.filepath = filepath
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Không tìm thấy file {self.filepath}")
        if self.filepath.endswith('.csv'):
            self.df = pd.read_csv(self.filepath)
        elif self.filepath.endswith('.xlsx'):
            self.df = pd.read_excel(self.filepath)
        else:
            raise ValueError("Định dạng file không hỗ trợ")

    def printHead(self,row):
        print(self.df.head(row))

    def printTail(self,row):
        print(self.df.tail(row))

    def printInfo(self):
        print(self.df.info())

    def printDescribe(self):
        print(self.df.describe())

    def visualizePieChart(self,df,columnLabel,columnStatistic,title,legend=True):
        explode=[0.1]
        for i in range(len(df[columnLabel])-1):
            explode.append(0)
        plt.figure(figsize=(8, 6))
        plt.pie(df[columnStatistic], labels=df[columnLabel], autopct='%1.2f%%',explode=explode)
        if legend:
            plt.legend(df[columnLabel])
        plt.title(title)
        plt.show()

    def visualizePlotChart(self,df,columnX,columnY,title):
        plt.figure(figsize=(8, 6))
        plt.plot(df[columnX], df[columnY])
        plt.legend([columnX,columnY])
        plt.title(title)
        plt.xlabel(columnX)
        plt.ylabel(columnY)
        plt.grid()
        plt.show()

    def visualizeCountPlot(self,df,columnX,columnY,hueColumn,title):
        plt.figure(figsize=(8, 6))
        ax=sns.countplot(x=columnX,hue=hueColumn,data=df)
        plt.title(title)
        plt.xlabel(columnX)
        plt.ylabel(columnY)
        plt.grid()
        plt.legend()
        plt.show()

    def visualizeBarPlot(self,df,columnX,columnY,hueColumn,title,alpha=0.8,width=0.6):
        plt.figure(figsize=(8, 6))
        plt.ticklabel_format(useOffset=False, style='plain')
        ax=sns.barplot(data=df,x=columnX,y=columnY,hue=hueColumn,alpha=alpha,width=width)
        plt.title(title)
        plt.xlabel(columnX)
        plt.ylabel(columnY)
        plt.grid()
        plt.legend()
        plt.show()

    def visualizeBarChart(self,df,columnX,columnY,title):
        plt.figure(figsize=(8, 6))
        plt.ticklabel_format(useOffset=False, style='plain')
        plt.bar(df[columnX],df[columnY])
        plt.title(title)
        plt.xlabel(columnX)
        plt.ylabel(columnY)
        plt.grid()
        plt.show()

    def visualizeScatterPlot(self,df,columnX,columnY,title):
        plt.figure(figsize=(8, 6))
        plt.ticklabel_format(useOffset=False, style='plain')
        sns.scatterplot(data=df,x= columnX,y=columnY)
        plt.title(title)
        plt.xlabel(columnX)
        plt.ylabel(columnY)
        plt.grid()
        plt.show()

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