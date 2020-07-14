from enum import IntEnum
from typing import Optional, List

# import pandas as pd


# def read_file(file_name: str):
# 	table = pd.read_excel(file_name, skiprows=[0, 1])
# 	if table.get("caption") is not None:
# 		table["caption"].replace(to_replace=pd.np.nan, value='', inplace=True)
# 	if table.get("content") is not None:
# 		table["content"].replace(to_replace=pd.np.nan, value='', inplace=True)
# 	if table.get("name") is not None:
# 		table["name"].replace(to_replace=pd.np.nan, value='', inplace=True)
#
# 	rows: List[TableRow] = list()
# 	for row_index, row in table.iterrows():
# 		table_row = TableRow(number=row_index, fields=row)
# 		rows.append(table_row)
#
# 	table_data = TableData(table_name=file_name, rows=rows)
#
# 	# result - результат, это массив, состоящий из текстов ошибок, либо пустых элементов.
# 	result = CourseFileValidator.validate_table(table_data)
# 	# сейчас он выводится в консоль, но прикольно, если бы ребята видели результат в какой-то понятно форме.
# 	print(result)


# это таблица. она состоит из рядов и названия
class TableData:
	def __init__(self, table_name: str, rows: ['TableRow']):
		self.table_name = table_name
		self.rows = rows


# это собственно ряд таблицы
class TableRow:
	def __init__(self, number: int, fields: [str]):
		self.number = number
		self.fields = fields


# это результат проверки ряда
class RowCheckResult:
	def __init__(self, number: int, error: Optional[str]):
		self.number = number
		self.error = error

	def __repr__(self):
		return str(vars(self))

	def __eq__(self, other):
		return vars(self) == vars(other)


# тут названия колонок.
# это удобно, потому что можно получить пятый столбик в ряде row как row[Columns.MESSAGE_TYPE].
# Потому что Columns.MESSAGE_TYPE ==5
class Columns(IntEnum):
	ITEM_ID = 1
	NAME = 3
	TYPE = 2
	DESCRIPTION = 4
	TIMEDELTA = 0

	MESSAGE_TYPE = 5
	MESSAGE_CONTENT = 6
	MESSAGE_CAPTION = 7

	EXERCISE_TEXT = 8
	EXERCISE_ANSWERS_STARTING = 9


class CourseFileValidator:
	# этот метод принимает таблицу
	# и возвращает массив состоящий из результатов проверок рядов
	@staticmethod
	def validate_table(table_data: TableData) -> [RowCheckResult]:
		results: List[RowCheckResult] = list()
		for row in table_data.rows:
			row_validation_result = CourseFileValidator.validate_row(row=row)
			results.append(row_validation_result)
		return results

	# это проверка каждого ряда
	@staticmethod
	def validate_row(row: TableRow) -> RowCheckResult:
		# вот тут тебе надо попрограммировать!
		# формат ошибки: в ряде 23 у <сообщения/упражнения> с item_id 34 нет чего-то там
		# эту строчку тоже надо будет поменять
		check_result = RowCheckResult(number=row.number, error=None)

		if len(row.fields[Columns.ITEM_ID]) == 0:
			check_result = RowCheckResult(number=row.number, error="No item_id for row")
			return check_result

		return check_result


if __name__ == '__main__':
    # read_file(file_name="")
	pass
else:
    print('Not main')