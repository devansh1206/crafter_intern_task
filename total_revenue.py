import csv

def calculate_total_revenue(file_name):
    with open(file_name, 'r') as file:
        data = csv.reader(file)
        total_revenue=0
        next(data) # this will skip the first row
        for row in data:
            total_revenue+= float(row[6]) # here 4 indicates that the sales value lie in 5th column hence the index in 4
    return total_revenue
path = r"C:\Users\devan\OneDrive\Desktop\learnJS\vgsales.csv"
print(calculate_total_revenue(path))