from matplotlib import pyplot as plt
import seaborn as sns

class Statistic:
    def __init__(self, connector=None):
        super().__init__()
        self.connector = connector

    def execPurchaseHistory(self,tableName=None):
        if tableName==None:
            sql="select * from purchasehistory"
        else:
            sql = "select * from %s"%tableName
        self.df=self.connector.queryDataset(sql)
        self.lasted_df=self.df
        return self.df

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
