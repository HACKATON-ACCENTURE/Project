from django.shortcuts import render
from .models import Workshop
import pandas as pd

class DataWorkshop:
	def __init__(self, ws_name, u_name, lst_dig):
		self.ws_name = ws_name
		self.u_name = u_name 
		self.lst_dig = lst_dig


	

def tables(request):
	df = pd.read_excel('C:/Users/Admin/Desktop/accenture/accenture/apps/loading/Лист Microsoft Excel.xlsx',3)
	df = pd.pivot_table(df, index=['Наименование цеха', 'Name'], values='OccupiedPercentage', columns='dStart')
	date = [i for i in pd.to_datetime(df.columns, format='%m%Y')]
	new_df = []
	for i in df.to_records():
		new_df.append(DataWorkshop(i[0], i[1], [int(i[j]) for j in range(2, len(i))]))
	
	return render(request, 'loading/loading.html', context = {'annual': new_df, 'date': date})

def index(request):
	return render(request, 'loading/index.html')

def kpi(request):
	return render(request, 'loading/trash.html')
