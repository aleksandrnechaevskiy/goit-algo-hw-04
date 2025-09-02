import timeit
import random

def insertion_sort(arr):
    """Сортування вставками."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """Сортування злиттям."""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def timsort_wrapper(arr):
    """Обгортка для вбудованої функції sorted()."""
    return sorted(arr)

#емпіричне тестування
def run_tests(size):
    """
    Проводить тести на різних наборах даних заданого розміру.
    
    :param size: Розмір масиву для тестування.
    :return: Словник з результатами часу виконання.
    """
    # Створення наборів даних
    random_data = [random.randint(0, 1000000) for _ in range(size)]
    sorted_data = list(range(size))
    reversed_data = list(range(size, 0, -1))

    test_cases = {
        "Випадкові дані": random_data,
        "Відсортовані дані": sorted_data,
        "Відсортовані у зворотньому порядку": reversed_data
    }

    results = {}
    algorithms = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Timsort (sorted)": timsort_wrapper
    }

    for case_name, data in test_cases.items():
        case_results = {}
        print(f"\nТестуємо набір даних: {case_name} (розмір {size})")
        
        for algo_name, algo_func in algorithms.items():
            # Створення копії масиву, щоб не змінювати вихідні дані
            data_copy = list(data)
            
            # Використання timeit для точного вимірювання часу
            setup_code = "from __main__ import " + algo_func.__name__
            stmt = f"{algo_func.__name__}(list({data}))"
            
            execution_time = timeit.timeit(stmt, globals=globals(), number=1)
            case_results[algo_name] = execution_time
            print(f"  Час виконання {algo_name}: {execution_time:.6f} сек")
        
        results[case_name] = case_results
    return results

if __name__ == "__main__":
    # Розміри масивів для тестування
    sizes = [1000, 10000]

    for size in sizes:
        run_tests(size)

"""Висновок
Timsort поєднує сильні сторони обох алгоритмів:

Сортування вставками: Використовується для сортування невеликих відрізків даних (run-ів), які є майже відсортованими. Це дуже ефективно, оскільки сортування вставками є швидким на малих, частково відсортованих масивах.

Сортування злиттям: Після того як невеликі run-и відсортовані, вони зливаються, використовуючи ефективний алгоритм злиття. Це забезпечує стабільну і швидку продуктивність O(n log n) для великих масивів.

Висновок:

Емпіричний аналіз підтверджує, що Timsort — це не просто гібрид, а розумний алгоритм, який адаптується до вхідних даних. Він демонструє високу продуктивність як на ідеальних (відсортованих), так і на випадкових наборах даних. Саме тому програмісти, які цінують ефективність та надійність, довіряють вбудованим в Python функціям сортування, замість того, щоб реалізовувати власні алгоритми. Ця оптимізація робить Python-програми швидшими без додаткових зусиль з боку розробника.
"""