class MinHeap:
    #Клас котрий реалізую власний тип данних Min-Heap
    _list = []  # Масив, котрий зберігає елементи піраміди

    def __init__(self):
        #Конструктор класу
        pass

    @property
    def heap_size(self):
        #Властивість(getter), що повертає розмір піраміди
        return len(self._list)

    def add(self, item):
        #Метод, що дозволяє додати новий елемент до піраміди та поставивши його у потрібне місце після цього
        self._list.append(item)  # додаємо елемент в кінець масиву
        i = self.heap_size - 1   # позначаємо його дочірнім
        parent = int((i - 1) / 2)  # знаходимо батьківський елемент для нього

        # будемо обмінювати в циклі елементи,тим самим підіймати його по піраміді вгору, доки не знайдеться елемент, що буде меншим за елемент, що ми додали
        while i > 0 and self._list[parent] > self._list[i]:
            self._list[i], self._list[parent] = self._list[parent], self._list[i]

            i = parent
            parent = int((i - 1) / 2)

    def heapify(self, i):
        #Метод, що перевіряє піраміду на властивість неспадної піраміди та повертає цю властивість якщо вона була втрачена

        # будемо опускатися вниз по піраміді, щоразу визначаючи найменший елемент та ставлячи його в правильну позицію доки властивість неспадної піраміди не буде виконана
        while True:
            left_child = 2 * i + 1  # індекс лівого дочірнього елемента
            right_child = 2 * i + 2  # індекс правого дочірнього елемента
            smallest_child = i  # індекс найменшого елемента

            if left_child < self.heap_size and self._list[left_child] < self._list[smallest_child]:
                smallest_child = left_child

            if right_child < self.heap_size and self._list[right_child] < self._list[smallest_child]:
                smallest_child = right_child

            if smallest_child == i:
                break

            self._list[i], self._list[smallest_child] = self._list[smallest_child], self._list[i]

            i = smallest_child

    def get_min(self, status_delete=False):
        #Метод, що повертає мінімальний елемент піраміди, при цьому його можна видалити з піраміди, передавши як аргумент status_delete=True
        if not status_delete:
            return self._list[0]

        # якщо елемент необхідно видалити з піраміди:
        # 1) обмінюємо місцями перший та останній елемент
        # 2) видаляємо останній(мінімальний) елемент записавши результат в
        #    змінну
        # 3) викликаємо метод heapify, що був описаний раніше в цьому класі
        self._list[0], self._list[self.heap_size-1] =\
            self._list[self.heap_size-1], self._list[0]

        min_item = self._list.pop(self.heap_size-1)
        self.heapify(0)

        return min_item


class MaxHeap:
    #Клас котрий реалізую власний тип данних Max-Heap
    _list = []  # Масив, котрий зберігає елементи піраміди

    def __init__(self):
        #Медод ініціалізатор
        pass

    @property
    def heap_size(self):
        #Властивість(getter), що повертає розмір піраміди
        return len(self._list)

    def add(self, item):
        #Метод, що дозволяє додати новий елемент до піраміди та поставивши його у потрібне місце після цього
        self._list.append(item)  # додаємо елемент в кінець масиву
        i = self.heap_size - 1  # позначаємо його дочірнім
        parent = int((i - 1) / 2)  # знаходимо батьківський елемент для нього

        # будемо обмінювати в циклі елементи,тим самим підіймати його по піраміді вгору, доки не знайдеться елемент, що буде меншим за елемент, що ми додали
        while i > 0 and self._list[parent] < self._list[i]:
            self._list[i], self._list[parent] = self._list[parent], self._list[i]

            i = parent
            parent = int((i - 1) / 2)

    def heapify(self, i):
        #Метод, що перевіряє піраміду на властивість незростаючої піраміди та повертає цю властивість якщо вона була втрачена"""

        # будемо опускатися вниз по піраміді, щоразу визначаючи найменший елемент та ставлячи його в правильну позицію доки властивість неспадної піраміди не буде виконана
        while True:
            left_child = 2 * i + 1  # індекс лівого дочірнього елемента
            right_child = 2 * i + 2  # індекс правого дочірнього елемента
            largest_child = i  # індекс найбільшого елемента

            if left_child < self.heap_size and self._list[left_child] > self._list[largest_child]:
                largest_child = left_child

            if right_child < self.heap_size and self._list[right_child] > self._list[largest_child]:
                largest_child = right_child

            if largest_child == i:
                break

            self._list[i], self._list[largest_child] = self._list[largest_child], self._list[i]
            i = largest_child

    def get_max(self, status_delete=False):
        #Метод, що повертає максимальний елемент піраміди, при цьому його можна видалити з піраміди, передавши як аргумент status_delete=True
        if not status_delete:
            return self._list[0]

        # якщо елемент необхідно видалити з піраміди:
        # 1) обмінюємо місцями перший та останній елемент
        # 2) видаляємо останній(максимальний) елемент записавши результат в
        #    змінну
        # 3) викликаємо метод heapify, що був описаний раніше в цьому класі
        self._list[0], self._list[self.heap_size - 1] = self._list[self.heap_size - 1], self._list[0]

        max_item = self._list.pop(self.heap_size - 1)
        self.heapify(0)

        return max_item


def check_count(low_heap: MaxHeap, high_heap: MinHeap):
    #Функція, що перевіряє умову різниці елементів між пірамідами(різниця в к-сті елементів має бути не більше одного)

    # якщо low_heap більше на два елементи, то видаляємо з неї найбільший та вставляємо до high_heap
    if (low_heap.heap_size - high_heap.heap_size) == 2:
        high_heap.add(low_heap.get_max(status_delete=True))

    # якщо high_heap більше на два елементи, то видаляємо з неї найменший та вставляємо до low_heap
    elif (high_heap.heap_size - low_heap.heap_size) == 2:
        low_heap.add(high_heap.get_min(status_delete=True))


def get_median(low_heap: MaxHeap, high_heap: MinHeap, count):
    #Функція, що повертає одну чи дві медіани в залежності від к-сті переданих елементів

    # якщо до програми було подано парну кількість елементів повертаємо дві медіани - найбільший з low_heap та найменший з high_heap
    if count % 2 == 0:
        return f"{low_heap.get_max()} {high_heap.get_min()}"

    # інакше медіана одна і зберігається в піраміді в якій на один елемент більше
    else:
        if low_heap.heap_size > high_heap.heap_size:
            return low_heap.get_max()
        else:
            return high_heap.get_min()


def program(filename, filename1):
    #Основна функція, де відбувається зчитування з файлу, виконання поставлених задач та запис результату до файлу

    file_name = filename  # ім'я файлу

    # зчитуємо дані з файлу до масиву
    with open(file_name, 'r') as file:
        data = (file.read()).split('\n')
        data = [int(elem) for elem in data]
        n, data = data[0], data[1:]

    # ініціалізуємо low_heap та high_heap
    low_heap = MaxHeap()
    high_heap = MinHeap()

    # первий елемент додаємо до low_heap
    low_heap.add(data[0])

    # записуємо результати виконання до файлу
    with open(filename1, 'w') as file:
        # перша медіана буде перший елемент, що був доданий до low_heap
        file.write(str(low_heap.get_max()) + "\n")

        # поступово опрацьовуємо всі вхідні елементи
        for i in range(1, n):
            num = data[i]  # беремо новий елемент з масиву

            # якщо елемент менший за максимальний елемент low_heap а отже у відсортованому масиві знаходився б у 1 половині то додаємо його до low_heap
            if num < low_heap.get_max():
                low_heap.add(num)
            # інакше до high_heap
            else:
                high_heap.add(num)

            # перевіряємо на різницю елементів між пірамідами
            check_count(low_heap, high_heap)
            # записуємо отриману медіану до файлу
            file.write(str(get_median(low_heap, high_heap, i + 1)) + "\n")



program('Inputs/input_16_10000.txt','Outputs/khmelinin_output_16_10000.txt') # вписуємо шляхи до файлів
