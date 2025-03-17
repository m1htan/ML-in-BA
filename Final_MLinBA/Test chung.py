def load_data(self, table_name="insurance_data"):
    try:
        # Kiểm tra kết nối MySQL trước khi truy vấn
        if not self.db_connector.conn:
            self.db_connector.connect()

        query = f"SELECT * FROM {table_name}"
        self.df = self.db_connector.queryDataset(query)

        if self.df is None or self.df.empty:
            raise ValueError("Không có dữ liệu hoặc dữ liệu bị rỗng!")

        print("Dữ liệu đã tải thành công từ MySQL!")

    except Exception as e:
        print(f"Lỗi khi tải dữ liệu từ MySQL: {e}")
        self.df = None