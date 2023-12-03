from collections import deque
import math
class calcuter():
    def __init__(self):
        self.nums_stack=deque()
        self.operator_stack=deque()
        self.houzhui=deque()
    def get_operand(self):
        num1=self.nums_stack.pop()
        num2=self.nums_stack.pop()
        return num1,num2
    def cal_value(self,operator):
        num1,num2=self.get_operand()
        #print("计算中")
        if (operator == '*'):
            self.nums_stack.append(num2 * num1)
        elif (operator == '/'):
            self.nums_stack.append(num2 / num1)
        elif (operator == '+'):
            self.nums_stack.append(num2 + num1)
        elif (operator == '-'):
            self.nums_stack.append(num2 - num1)

    def calculate(self,str):
        print("formula=",str)
        last_is_operator=True
        has_dot=False
        dot_num=1
        for i in range(len(str)):
            if (str[i] <= '9' and str[i] >= '0' and has_dot and not last_is_operator):
                self.nums_stack[-1] = self.nums_stack[-1] + eval(str[i])/math.pow(10,dot_num)
                self.houzhui[-1] = self.houzhui[-1]+ eval(str[i])/math.pow(10,dot_num)
                dot_num+=1

            if (str[i] <= '9' and str[i] >= '0' and not has_dot and not last_is_operator):
                self.nums_stack[-1] = self.nums_stack[-1] * 10 + eval(str[i])
                self.houzhui[-1] = self.houzhui[-1] * 10 + eval(str[i])
                last_is_operator = False

            if(str[i]<='9' and str[i]>='0' and last_is_operator and not has_dot):
                self.nums_stack.append(eval(str[i]))
                self.houzhui.append(eval(str[i]))
                last_is_operator=False

            repeat=True
            if(str[i]=='+' or str[i]=='-'):
                last_is_operator=True
                has_dot=False
                while(repeat):
                   if (self.operator_stack and self.operator_stack[-1] == '(' ):
                       self.operator_stack.append(str[i])
                       repeat=False
                   elif(not self.operator_stack):
                    self.operator_stack.append((str[i]))
                    repeat = False
                   else:
                     operator = self.operator_stack.pop()
                     self.houzhui.append(operator)
                     self.cal_value(operator)


            repeat=True
            if(str[i]=='*' or str[i]=='/'):
                last_is_operator=True
                has_dot = False
                while(repeat):
                   if (self.operator_stack and self.operator_stack[-1] == '('):
                        repeat = False
                        self.operator_stack.append(str[i])
                   elif (not self.operator_stack):
                      self.operator_stack.append((str[i]))
                      repeat=False
                   elif (self.operator_stack and (self.operator_stack[-1] == '+' or self.operator_stack[-1] == '-')):
                        self.operator_stack.append(str[i])
                        repeat=False
                   else:
                    operator=self.operator_stack.pop()
                    self.houzhui.append(operator)
                    self.cal_value(operator)

            if(str[i]=='('):
                last_is_operator=True
                has_dot = False
                self.operator_stack.append(str[i])

            if(str[i]==')'):
                last_is_operator=True
                has_dot = False
                operator=self.operator_stack.pop()
                while (not operator=='('):
                    self.houzhui.append(operator)
                    self.cal_value(operator)
                    operator=self.operator_stack.pop()

            if(str[i]=='.'):
                has_dot=True
                dot_num=1


        while(self.operator_stack):
            operator = self.operator_stack.pop()
            self.houzhui.append(operator)
            self.cal_value(operator)
        return self.nums_stack.pop()


if __name__ =='__main__':
  formula = input('请输入您的计算式：')
  cal=calcuter()
  result=cal.calculate(formula)
  print(cal.houzhui)
  print("result=",result)








