import csv
import pandas as pd

class House:
    def __init__(self, capacity: int = 100, lower: int = 0):
        self.capacity = capacity
        self.lower = lower
        self.battery: list[float] = [0]
        self.pv: list[float] = [0,0,0,0,0,0,0,0,0]
        self.load: list[float] = [0,0,5,5,3,1,9,0,3]
        self.grid_sell: list[float] = [0]
        self.grid_buy: list[float] = [0]
        self.state:int = 0
        self.step = [0]

    def update(self):
        self.battery.append(self.battery[-1] + self.pv[self.step[-1]] - self.load[self.step[-1]])
        self.step.append(self.step[-1] + 1)
		# バッテリー上限時の処理
        if self.battery[-1] > self.capacity:
            self.grid_sell.append(self.battery[-1] - self.capacity)
            self.battery[-1] = self.capacity
            self.grid_buy.append(0)
        elif self.battery[-1] < self.lower:
            self.grid_buy.append(self.battery[-1] * -1)
            self.battery[-1] = self.lower
            self.grid_sell.append(0)
        else:
            self.grid_buy.append(0)
            self.grid_sell.append(0)
        
        # print(a)
    def csvwrite(self, path = "result.csv"):
        self.data = {"step":self.step, "pv":self.pv, "load":self.load, "grid_sell":self.grid_sell, "grid_buy":self.grid_buy}
        df = pd.DataFrame(self.data)
        print(df)
        df.to_csv(path)
        # csvモジュールonlyで行う場合
        # self.step.insert(0,"step")
        # self.battery.insert(0,"battery")
        # self.pv.insert(0,"pv")
        # self.load.insert(0,"load")
        # self.grid_sell.insert(0,"grid_sell")
        # self.grid_buy.insert(0,"grid_buy")
        # f = open(path, 'w', newline='')
        # writer = csv.writer(f)
        # writer.writerows(self.data.values())
        # f.close()

h = House()
for i in range(8):
  h.update()
h.csvwrite()
# test


