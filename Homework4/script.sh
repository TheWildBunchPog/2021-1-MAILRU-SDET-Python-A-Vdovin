exec 1>results.txt

echo 'Общее количество запросов'
cat $1 | wc -l
echo ''

echo 'Общее количество запросов по типу'
cat $1 | awk -F '[" ]' '{print $7}' | sort | uniq -c | sort -k1 -n -r | awk '{print $2,$1}'
echo ''

echo 'Топ 10 самых частых запросов'
cat $1 | awk -F '[" ]' '{print $8}' | sort | uniq -c | sort -k1 -n -r | awk '{print $2,$1}' | head -10
echo ''

echo 'Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой'
cat $1 | awk -F '[" ]' '$11>=400 && $11<500 {print $8,$11,$12,$1}' | sort -k3 -n -r | head -5
echo ''

echo 'Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой'
cat $1 | awk -F '[" ]' '$11>=500 {print $1}' | uniq -c | sort -k1 -n -r | awk '{print $2,$1}' | head -5