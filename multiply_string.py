class Solution:
    def multiply2(self, num1: str, num2: str) -> str:
        def replace_str_index(text,index=0,replacement=''):
            return '%s%s%s'%(text[:index],replacement,text[index+1:])

        def single_digit_multiply(num1:str, num2:str ) -> (int, int):
            ascii_zero = ord('0')
            int_num1 = ord(num1) - ascii_zero
            int_num2 = ord(num2) - ascii_zero

            result = int_num1 * int_num2

            return (result // 10, result % 10) 

        def add_lo_to_res(res:str, lo:int, base:int) -> str:
            # print(res, ', ', lo, ', ', base)
            if base >= len(res):
                zeros = res.zfill(base)
                return str(lo) + zeros 
            else:
                value = lo
                for i in range(len(res) - base - 1, -1, -1):
                    digit_in_res = res[i]
                    int_digit = ord(digit_in_res) - ord('0')
                    sum = int_digit + value 
                    if sum >= 10:
                        value = sum // 10
                        res = replace_str_index(res, i, sum-10)
                    else:
                        res = replace_str_index(res, i, sum)
                        value = 0
                        break
                        
                if value > 0:
                    res = str(value) + res
            
            #print(res)
            return res


        if num1 == '0' or num2 == '0':
            return '0'


        base = 0
        res = ''
        for digit_in_num2 in num2[::-1]:
            prev_hi = 0
            if digit_in_num2 == '0':
                pass 
            else:
                linebase = 0
                for digit_in_num1 in num1[::-1]:
                    (high, lo) = single_digit_multiply(digit_in_num1, digit_in_num2)
                    new_lo = lo + prev_hi
                    lo = new_lo % 10
                    prev_hi = high + new_lo // 10
                    res = add_lo_to_res(res, lo, base + linebase)
                    linebase += 1
            
            if prev_hi > 0:
                res = add_lo_to_res(res, prev_hi, base + linebase)
            base += 1
        


        return res 

    def multiply(self, num1: str, num2: str) -> str:


        def single_digit_multiply(num1:str, num2:str ) -> (int, int):
            ascii_zero = ord('0')
            int_num1 = ord(num1) - ascii_zero
            int_num2 = ord(num2) - ascii_zero

            result = int_num1 * int_num2

            return (result // 10, result % 10) 


        if num1 == '0' or num2 == '0':
            return '0'


        # base = 0
        res = ''
        order = ''
        line_results = []
        for digit_in_num2 in num2[::-1]:
            prev_hi = 0
            if digit_in_num2 == '0':
                order += '0'
                continue 
            else:
                line_result = ''
                for digit_in_num1 in num1[::-1]:
                    (high, lo) = single_digit_multiply(digit_in_num1, digit_in_num2)
                    new_lo = lo + prev_hi
                    lo = new_lo % 10
                    prev_hi = high + new_lo // 10
                    line_result = str(lo) + line_result
                
                if prev_hi > 0:
                    line_result = str(prev_hi) + line_result
            

            line_results.append(line_result + order)
            order += '0'
        
        if len(line_results) == 0:
            return '0'

        # print(line_results)

        i = -1
        res = ''
        carry = 0
        nostop = True
        while nostop:
            nostop = False
            sum = carry
            for line_result in line_results:
                
                if len(line_result) >= -i:
                    nostop = True
                    sum = sum + (ord(line_result[i]) - ord('0'))
            
            if nostop: 
                res = str(sum%10) + res
                carry = sum // 10

            i -= 1
        
        # print("res1", res)
        if carry > 0:
            res = str(carry) + res
        # print(res)
        return res 


if __name__ == '__main__':
    sol = Solution()
    # print(sol.multiply('23456', '22'))
    print(sol.multiply('999', '999'))
    print(sol.multiply('6', '501'))

