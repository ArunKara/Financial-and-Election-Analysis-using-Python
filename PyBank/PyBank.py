#PyBank!!

import os
import csv

budget_data_csv = os.path.join("Resources","budget_data.csv")
#tracking output
total_months = 0
net_total = 0
average_change_list = []
greatest_profit = ["", 0]
greatest_loss = ["", 0]
change_ofmonth = []

with open(budget_data_csv) as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    
    csv_header = next(csv_reader)
    print(csv_header)
    
    #we will extract the first row to avoid reading the header
    firstrow = next(csv_reader)
    total_months = total_months+1
    previousrow = int(firstrow[1])
    net_total = net_total+int(firstrow[1])
    for i in csv_reader:
        #track total number of months
        total_months = total_months+1
        net_total = net_total + int(i[1])
        #track the net change
        average_change = int(i[1]) - previousrow
        previousrow = int(i[1])
        average_change_list = average_change_list+[average_change]
        change_ofmonth = change_ofmonth + [i[0]]

        # Greaters Increase
        if average_change > greatest_profit[1]:
           greatest_profit[0] = i[0]
           greatest_profit[1] = average_change


        #Greates loss
        if average_change < greatest_loss[1]:
            greatest_loss[0] = i[0]
            greatest_loss[1] = average_change

# Calculate the average of the months
net_average_month = sum(average_change_list)/ len(average_change_list)        

# Output Results 
results = (f"total_months = {total_months}\n"
           f"Net_total: {net_total}\n"
           f"net_average_month = {net_average_month}\n"
           f"Greatest Increase in Profit : {greatest_profit[0]} and ({greatest_profit[1]})\n"
           f"Greatest Decrease in Loss: {greatest_loss[0]} and ({greatest_loss[1]})"
           )
print(results)

output_file = os.path.join("Analysis","Financial_Anlysis.txt")
with open(output_file,"w") as datafile:
    writer = csv.writer(datafile)

    datafile.write(results)