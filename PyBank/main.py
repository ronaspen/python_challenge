import os 
import csv 

budget_data_csv = os.path.join("..", "PyBank", "budget_data.csv")

date = []
profit_losses = []


with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        date.append(row[0])

        profit_losses.append(row[1])

       


def bank_stats(bank_data):
    total_months = max(bank_data[1] - 1)
    net_profit_loss = (sum(bank_data[1]))
    total_change = (bank_data[1].max_column - bank_data[1].min_column)

max = []
for i to end_row in row_difference: 
    if budget_data_df.loc[:, i + 1] > budget_data_df.loc[:, i]
    max = budget_data_df.loc[:, i + 1]

    print(max)

min = []
    for j to end_row in row_difference:
    if budget_data_df.loc[:, i + 1] < budget data df.loc[:, 1]
    min = budget_data_df.loc[:, i + 1]

    print(min)