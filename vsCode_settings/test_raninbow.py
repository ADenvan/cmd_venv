def complex_example(data):
    # Вложенные структуры
    result = {
        'items': [
            {
                'id': i,
                'value': i * 2,
                'nested': {
                    'deep': [j for j in range(i) if (j % 2 == 0)]
                }
            } for i in range(10)
        ],
        'metadata': {
            'count': len(data),
            'processed': True
        }
    }

    # Сложные выражения
    calculation = (
        sum(result['items'][i]['value']
            for i in range(len(result['items']))
            if result['items'][i]['id'] > 5)
        * (2 if result['metadata']['processed'] else 1)
    )

    return calculation

# Вызов функции
test_data = [x for x in range(20) if (x > 5 and x < 15)]
print(complex_example(test_data))

def example():
    if True:
        for i in range(10):
            print(i)
            if i == 5:
                print("Found 5!")
    return "Done"

# Скобки тоже будут подсвечены
data = {
    "key1": "value1",
    "key2": [1, 2, 3, {
        "nested": "value"
    }]
}