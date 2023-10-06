
def mergesort_recursive(array, p, r, byfunc=None):
    if r - p > 0:
      q = (p + r) // 2
      mergesort_recursive(array, p, q, byfunc)
      mergesort_recursive(array, q + 1, r, byfunc)
      merge(array, p, q, r, byfunc)

def merge(array, p, q, r, byfunc=None):
  left_size = q - p + 1
  right_size = r - q
  left_array = array[p:q + 1]
  right_array = array[q + 1:r + 1]
  left = 0
  right = 0
  dest = p
  while left < left_size and right < right_size:
    if byfunc(left_array[left]) <= byfunc(right_array[right]):
      array[dest] = left_array[left]
      left += 1
    else:
      array[dest] = right_array[right]
      right += 1
    dest += 1
  while left < left_size:
    array[dest] = left_array[left]
    left += 1
    dest += 1
  while right < right_size:
    array[dest] = right_array[right]
    right += 1
    dest += 1

def mergesort(array, byfunc=None):
  end_index = len(array) - 1
  mergesort_recursive(array, 0, end_index, byfunc)

class Stack:
  def __init__(self):
    self.__items = []

  def push(self, item):
    self.__items.append(item)

  def pop(self):
    size_stack = len(self.__items)
    if size_stack == 0:
      return None
    else:
      return self.__items.pop()

  def peek(self):
    size_stack = len(self.__items)
    if size_stack == 0:
      return None
    else:
      return self.__items[-1]

  @property
  def is_empty(self):
    size_stack = len(self.__items)
    return size_stack == 0

  @property
  def size(self):
    return len(self.__items)

class Queue:
  def __init__(self):
    self.__items = []

  def enqueue(self, item):
    self.__items.append(item)

  def dequeue(self):
    return self.__items.pop(0)

  def peek(self):
    if len(self.__items) == 0:
      return None
    else:
      return self.__items[0]

  @property
  def is_empty(self):
    if len(self.__items) == 0:
      return True
    else:
      return False

  @property
  def size(self):
    return len(self.__items)


class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  operands = '0123456789'
  operators = "+-*/()"

  def __init__(self, string=""):
    self.__expression = string

  @property
  def expression(self):
    return self.__expression

  @expression.setter
  def expression(self, new_expr):
    for char in new_expr:
      if char not in self.valid_char:
        self.__expression = ''
        return
    self.__expression = new_expr
    return

  def insert_space(self):
    modified_expression = ''
    for char in self.__expression:
      if char in self.operators:
        modified_expression += ' ' + char + ' '
      else:
        modified_expression += char
    return modified_expression

  def process_operator(self, operand_stack, operator_stack):
    second_number = operand_stack.pop()
    first_number = operand_stack.pop()
    operator_string = operator_stack.pop()
    if operator_string == "+":
      operand_stack.push(int(first_number) + int(second_number))
    elif operator_string == "-":
      operand_stack.push(int(first_number) - int(second_number))
    elif operator_string == "*":
      operand_stack.push(int(first_number) * int(second_number))
    elif operator_string == "/":
      operand_stack.push(int(first_number) // int(second_number))

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    for token in tokens:
      if token in self.operands:
        operand_stack.push(token)
      elif token == '+' or token == '-':
        while not operator_stack.is_empty and operator_stack.peek() != '(' and operator_stack.peek() != ')':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(token)
      elif token == '*' or token == '/':
        if operator_stack.peek() == '*' or operator_stack.peek() == '/':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(token)
      elif token == '(':
        operator_stack.push(token)
      elif token == ')':
        while operator_stack.peek() != '(':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.pop()
    while not operator_stack.is_empty:
      self.process_operator(operand_stack, operator_stack)
    return operand_stack.peek()

def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





