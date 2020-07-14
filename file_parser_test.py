import unittest
from file_parser import CourseFileValidator, TableRow, RowCheckResult
from message_type import MessageType


class FileParserTest(unittest.TestCase):

	def test_validate_row__message__ok(self):
		# подготавливаем входные значения
		row = TableRow(number=1, fields=["0:0:1", "123", "msg", "пыщ", "", "VideoNoteMessage", "some_url"])

		# действие - проверяем функцию validate_row
		result = CourseFileValidator.validate_row(row=row)

		# ожидаемый результат
		expected_result = RowCheckResult(error=None, number=1)

		# проверка результата
		self.assertEqual(result, expected_result)

	# тесты на идентификатор элемента. Он подаётся на вход строкой, но должен приводиться к целому числу.

	def test_validate_row__message_no_id(self):
		# подготавливаем входные значения
		row = TableRow(number=1, fields=["0:0:1", "", "msg", "пыщ", "", "VideoNoteMessage", "some_url"])

		# действие - проверяем функцию validate_row
		result = CourseFileValidator.validate_row(row=row)

		# ожидаемый результат
		expected_result = RowCheckResult(error="Wrong item_id for row", number=1)

		# проверка результата
		self.assertEqual(result, expected_result)

	def test_validate_row__message_wrong_id(self):
		# подготавливаем входные значения
		row = TableRow(number=1, fields=["0:0:1", "saf", "msg", "пыщ", "", "VideoNoteMessage", "some_url"])

		# действие - проверяем функцию validate_row
		result = CourseFileValidator.validate_row(row=row)

		# ожидаемый результат
		expected_result = RowCheckResult(error="Wrong item_id for row", number=1)

		# проверка результата
		self.assertEqual(result, expected_result)

	# тесты на время от предыдущего элемента. Оно должно быть в формате с двумя двоеточиями

	def test_validate_row__no_timedelta(self):
		# подготавливаем входные значения
		row = TableRow(number=1, fields=["", "123", "msg", "пыщ", "", "VideoNoteMessage", "some_url"])

		# действие - проверяем функцию validate_row
		result = CourseFileValidator.validate_row(row=row)

		# ожидаемый результат
		expected_result = RowCheckResult(error="Problems with timedelta", number=1)

		# проверка результата
		self.assertEqual(result, expected_result)

	def test_validate_row__wrong_timedelta(self):
		# подготавливаем входные значения
		row = TableRow(number=1, fields=["мам я танцую", "123", "msg", "пыщ", "", "VideoNoteMessage", "some_url"])

		# действие - проверяем функцию validate_row
		result = CourseFileValidator.validate_row(row=row)

		# ожидаемый результат
		expected_result = RowCheckResult(error="Problems with timedelta", number=1)

		# проверка результата
		self.assertEqual(result, expected_result)

	# тесты на тип элемента. он должен быть либо 'msg', 'ex', 'block'

	# ... пишите тут

	# тесты на message_type.
	# 1) это должна быть непустая строка
	# 2) если тут что-то написано, то тип элемента должен быть 'msg'

	# ... пишите тут


if __name__ == '__main__':
	unittest.main()
