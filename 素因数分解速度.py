import flet as ft
import math
import datetime
import time

def main(page:ft.Page):
    page.auto_scroll=True
    
    def fact(n):
        #global f_previous
        f = []
        original_f = []
        tmp = n
        for i in range(2,int(n**0.5)+1):
            if tmp%i ==0:
                cnt=0
                while tmp%i==0:
                    tmp//=i
                    cnt+=1
                if cnt==1:
                    f.append(f'{i}')
                    original_f.append(i)
                    original_f.append(1)
                else:
                    f.append(f'{i}^{cnt}')
                    original_f.append(i)
                    original_f.append(cnt)
        # if there was no factorials in the range and the number hasn't change, it is a prime
        if tmp!=1:
            f.append(str(tmp))
            original_f.append(tmp)
            original_f.append(1)
        # if there was no factorials in the range, it is a prime  
        if f==[]:
            f.append(str(n))
            original_f.append(n)
            original_f.append(1)
        #f_previous = f[:]
        return ' x '.join(f), original_f
    
    # whether if it's a prime or half prime
    def prime(n,f):
        if len(fact(n)[1])==1:
            return 'o'
        elif len(fact(n)[1])==2:
            return 'half prime'
        else:
            return 'x'
        
    # the number of factors
    def num_fact(fun_list):
        num=1
        for i in range(1,len(fun_list),2):
            num *= fun_list[i]+1
        return num
    
    # the sum of factors & whether if it's a perfect number
    def sum_fact(n,fun_list):
        sum=1
        for i in range(0,len(fun_list),2):
            tmp=1
            for j in range(1,fun_list[i+1]+1):
                tmp+=(fun_list[i]**j)
            sum*=tmp
        if sum==2*n:
            character="perfect number"
        elif sum>=2*n:
            character='abundant number'
        else:
            character='deficient number'
        return sum,character
    
    #factorial fanction
    def factorial(n):
        i=0
        while math.factorial(i)<n:
            i+=1
            if math.factorial(i)==n:
                return f'factorial number : o'
            elif math.factorial(i)>n:
                return f'factorial number : x', math.factorial(i-1),math.factorial(i),i
                 
    # binary oct hex expression
    def bin_oct_hex(n):
        return bin(n)[2:], oct(n)[2:], hex(n)[2:]
    
    def submit(e):
        n = int(textfield_number_input.value)
        factors_str = fact(n)
        binary_thing = bin_oct_hex(n)
        sum_of_factors = sum_fact(n,factors_str[1])
        factorial_thing = factorial(n)
        
        progress_ring=ft.ProgressRing(width=20,height=20,stroke_width=2)
        page.add(progress_ring)
        page.update
        for i in range(0,101):
            progress_ring.value=i*0.01
            time.sleep(0)
            page.update()
        page.remove(progress_ring)
        
        display_number.value = n
        fact_result_field.value = f'factorisation: {factors_str[0]}'
        fact_num_field.value = f'number of factors : {num_fact(factors_str[1])}'
        prime_field.value = f'prime number : {prime(n,factors_str[0])}'
        fact_sum_field.value = f'sum of factors : {sum_of_factors[0]}'
        whether_perfect.value = f'whether this number is a perfect number : {sum_of_factors[1]}'
        factorial_field.value = f'{factorial(n)[0]}'
        closest_factorial.value = f'the closest factorial number : {factorial_thing[1]} and {factorial_thing[2]} ({factorial_thing[3]-1}! and {factorial_thing[3]}!)'
        
        bin_field.value = f'binary expression : {binary_thing[0]}'
        oct_field.value = f'octal expression : {binary_thing[1]}'
        hex_field.value = f'hexadecimal expression : {binary_thing[2]}'
        
        history_field.controls.append(ft.ElevatedButton(text=f"{n}",on_click=history)) #ここsubmitで実装したかった
        page.update()
    
    def history(e):
        textfield_number_input.value = e.control.text
        page.update()
        
    def handle_change(e):
        select_view = ft.Column(controls=[
            ft.Row(controls=[
                ft.ElevatedButton(f"{e.control.value.strftime('%Y%m%d')}",
                                  on_click=date_selected),
                ft.ElevatedButton(text=f"{e.control.value.strftime('%Y')}",
                                  on_click=date_selected),
                ft.ElevatedButton(f"{e.control.value.strftime('%Y%m')}",
                                  on_click=date_selected),
                ft.ElevatedButton(f"{e.control.value.strftime('%Y%d')}",
                                  on_click=date_selected),
                ft.ElevatedButton(f"{e.control.value.strftime('%m%d')}",
                                  on_click=date_selected),
                ]),
                ft.ElevatedButton(text="cancel",icon=ft.icons.CANCEL,on_click=remove)
            ])
        page.controls.pop()
        page.add(select_view)
            
        textfield_number_input.value = e.control.value.strftime('%Y%m%d')
        page.update()
    
    def date_selected(e):
        textfield_number_input.value = e.control.text
        page.update()
        
    def remove(e):
        page.controls.pop() #これはpage内の一番上にあるものを削除するmethod
        page.add(date_picker)
        page.update()
    
    def handle_dismissal(e):
        pass
    
    
    textfield_number_input = ft.TextField(
        label="<type value that you want to factorise>",
        border_color=ft.colors.BLUE,
        autofocus=True,
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=submit
    )
    
    submit_button = ft.ElevatedButton(
        text="confirm",
        icon=ft.icons.SEND,
        on_click=submit
    )
    
    display_number = ft.Text(
        "number",
        theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM
    )
    
    fact_result_field = ft.Text(
        "factorisation", 
        size = 20,
        spans=[
            ft.TextSpan(text="  change this text")            
        ])
    
    fact_num_field = ft.Text("number of factors")
    prime_field = ft.Text("whether if this number is a prime or not")
    fact_sum_field = ft.Text("sum of factors")
    whether_perfect = ft.Text("wether this number is a perfect number")
    
    factorial_field = ft.Text("whether if this number is a factorial number or not")
    closest_factorial = ft.Text("the closest factorial numbers")
    
    bin_field = ft.Text("binary expression")
    oct_field = ft.Text("octal expression")
    hex_field = ft.Text("hexadecimal expression")
    
    #history
    history_field = ft.Row(
        controls=[
            ft.Row(controls=[])
        ],
        wrap=True
    )
    
    date_picker = ft.ElevatedButton(
        "pick date",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda e: page.open(
            ft.DatePicker(
        first_date=datetime.datetime(year=1900,month=1,day=1),
        last_date=datetime.datetime(year=2050,month=1,day=1),
        on_change=handle_change,
        on_dismiss=handle_dismissal,
        )))
    
    
    page.add(textfield_number_input, 
             submit_button,
             display_number,
             fact_result_field, 
             fact_num_field,
             prime_field,
             fact_sum_field,
             whether_perfect,
             factorial_field,
             closest_factorial,
             bin_field,
             oct_field,
             hex_field,
             history_field,
             date_picker
             )
    
ft.app(target=main)