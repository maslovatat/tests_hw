# ДОМАШНЕЕ ЗАДАНИЕ по паре6 : Стек и его применение
**Выполнила:** Маслова Т.А.

## Часть 1. Valid Parentheses (LeetCode 20)

**Код решения:**
```
python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:                 
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()                     
            else:                               
                stack.append(char)              
                
        return not stack                        


```
**Результат на LeetCode:**
- Вердикт: Accepted (103/103 тестов)
- Runtime: 1 ms (Beats 45.30%)
- Memory: 19.10 MB (Beats 91.12%)

Стек выбран потому, что закрывающая скобка всегда относится к последней открытой — это принцип LIFO (Last In, First Out). Мы проходим строку один раз: открывающие скобки кладем в стек (push), а для каждой закрывающей сверяем с вершиной и удаляем её (pop). Временная сложность O(n), так как каждый символ обрабатывается ровно один раз

```
```
## Часть 2. Implement Queue using Stacks (LeetCode 232)


```
python
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _transfer(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack        

```
**Результат на LeetCode:**
- Вердикт: Accepted (23/23 тестов)
- Runtime: 0 ms (Beats 100.00%)
- Memory: 19.45 MB (Beats 54.54%)

Очередь работает по принципу FIFO (первым пришел — первым ушел), а стек — LIFO. Для реализации очереди были использованы два стека in_stack для добавления элементов и out_stack для извлечения. При перекладывании порядок меняется на противоположный, и на вершине out_stack оказывается самый первый добавленный элемент.
Сложность: push, empty — O(1). pop, peek — O(1).
```
```
## Часть 3. Работа с агентом
Агенту Perplexity (веб-версия) был задан такой промт:
"Реши задачу Valid Parentheses. Какую структуру данных выберешь и почему? Укажи временную и пространственную сложность"
Агент предложил использовать стек (Stack) основываясь на том, что скобки должны закрываться в порядке, обратном их открытию, что (принцип LIFO). Оценка сложности от агента: O(n) по времени и O(n) по памяти.
Решение задачки Valid Parentheses (LeetCode 20) агентом:
```
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in pairs:                 # закрывающая скобка
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:                             # открывающая скобка
                stack.append(char)

        return not stack

```
далее агент выдал решение задачи Queue using Stacks (LeetCode 232)
```
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _transfer(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
