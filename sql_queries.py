
# Вывести топ 5 самых коротких по длительности перелетов.
# Duration - разница между scheduled_arrival и scheduled_departure.
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = """
SELECT 
    flight_no,
    EXTRACT(EPOCH FROM (scheduled_arrival - scheduled_departure)) AS duration
FROM 
    flights
ORDER BY 
    duration ASC
LIMIT 5;
"""



# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 50
# В ответе должно быть 2 колонки [flight_no, count]
TASK_2_QUERY = """
SELECT 
    flight_no,
    COUNT(*) AS count
FROM 
    flights
GROUP BY 
    flight_no
HAVING 
    COUNT(*) < 50
ORDER BY 
    count DESC
LIMIT 3;
"""


# Вывести число перелетов внутри одной таймзоны
# Нужно вывести 1 значение в колонке count
TASK_3_QUERY = """
SELECT COUNT(*) AS count FROM flights
WHERE 
    departure_timezone = arrival_timezone;
"""

