# Списки Lists
#
# К каждому элементу можно обратиться по его индексу (отсчет идет с нуля)
# Синтаксис:
#	<Имя Списка> = [
#		<Первый элемент>,
#		<Второй элемент>,
#		<Третий элемент>
#	]

listic = [
	"Я нулевой элемент",
	"Я вот это второй да",
	"Третий на месте",
	"Четверный присутствует",
	"Пятерочка ага да",
	"А я вот последний"
]

for n in 0, 1, 2, 3, 4, 5:
	print(listic[n])