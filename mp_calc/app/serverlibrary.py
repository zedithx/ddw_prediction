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
        tokens = expression.split()   # convert expression passed in into a list of tokens
        """Iterate through the tokens"""
        for token in tokens:
            if token in self.operands:   # check if token is an operand
                operand_stack.push(token)
            elif token == '+' or token == '-':  # if extracted character is + or - operator
                """process all the operators as long as the operator_stack is not empty
                and the top of the operator_stack is not ( or ) symbols. """
                while not operator_stack.is_empty and operator_stack.peek() != '(' and operator_stack.peek() != ')':
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(token)  # push token to stack after processing
            elif token == '*' or token == '/':  # if extracted character is * or / operator
                # process all the * or / operators at the top of the operator_stack
                if operator_stack.peek() == '*' or operator_stack.peek() == '/':
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(token)  # push extracted operator into stack
            elif token == '(':
                operator_stack.push(token)  # push extracted operator into stack
            elif token == ')':
                # process operators from top of operator stack until an open bracket
                while operator_stack.peek() != '(':
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.pop()
        # once finished, process operators from top of operator stack until empty
        while not operator_stack.is_empty:
            self.process_operator(operand_stack, operator_stack)
        return operand_stack.peek()


def get_smallest_three(challenge):
    records = challenge.records
    times = [r for r in records]
    mergesort(times, lambda x: x.elapsed_time)
    return times[:3]
def prepare_feature(df_feature):
    array_size = df_feature.shape[0]
    if isinstance(df_feature, pd.DataFrame):
        df_feature = np.array(df_feature)
    df_feature = df_feature.reshape(array_size, df_feature.shape[1])
    # column vector of 1s
    constant_vector = np.ones((array_size, 1))
    df_feature = np.concatenate((constant_vector, df_feature), 1)
    return df_feature
def normalize_z(variable_list: list, column_means, column_stds):
    res = []
    for item1, item2, item3 in zip(variable_list, column_means, column_stds):
        item = (item1 - item2) / item3
        res.append(item)
    return res
def get_predicted_value(var1, var2, var3):
    beta = [415.173533, 0.395997198, 32.3521125, 1.54418376, 10.9100142]
    column_means = [124.647460, 133.865238, 154.913651, 25828.950956]
    column_stds = [28.565058, 33.143529, 43.130492, 14034.861683]
    variables = [float(var1), float(var2), float(var3), float(var3)**2]
    variables_norm = normalize_z(variables, column_means, column_stds)
    pred = beta[0] + beta[1] * variables_norm[0] + beta[2] * variables_norm[1] + beta[3] * variables_norm[2] + beta[4] * variables_norm[3]
    return pred
