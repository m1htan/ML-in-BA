from MLinBA.Final_MLinBA.Model.Chart.Statistics.data_loader import DataLoader

class BaseAnalyzer(DataLoader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def check_data_empty(self):
        if self.df.empty:
            raise ValueError("Dữ liệu rỗng! Vui lòng kiểm tra lại file CSV.")