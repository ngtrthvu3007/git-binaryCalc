def sum(A,B): 
        maxlen = max(len(A), len(B)) 
  
        A = A.zfill(maxlen) 
        B = B.zfill(maxlen) 
        #dùng zfill làm đầy chuỗi A, B
        
        result = ''
        carry = 0 # tạo số nhớ
  
       # duyệt chuỗi 
        for i in range(maxlen - 1, -1, -1): 
            r = carry # r là biến tạm của số nhớ
            r += 1 if A[i] == '1' else 0 # r tăng 1 nếu u qua 1 và ngược lại
            r += 1 if B[i] == '1' else 0 # r tăng 1 nếu i qua 1 và ngược lại
            
            result = ('1' if r % 2 == 1 else '0') + result # kết quả là '1' nếu r là số lẻ và ngược lại 
            carry = 0 if r < 2 else 1   #tính số nhớ, nếu r nhỏ hơn 2 thì số nhớ là 0 và ngược lại
          
        if carry !=0 : result = '1' + result 
  
        return result.zfill(maxlen) #làm đầy kết quả bằng zfill
	
def dif(A,B):
        max_len = max(len(A), len(B))

        A = A.zfill(max_len)
        B = B.zfill(max_len)

        result = ''
        carry = 0
    
        x = int(A, 2)      
        y = int(B, 2)
        
        if x < y:
            return("error")
    
        for i in range(max_len-1, -1, -1):
            r = 1 if A[i] == '1' else 0
            r -= 1 if B[i] == '1' else 0
            r -= carry
            result = ('1' if r % 2 == 1 else '0') + result
            carry = 1 if r < 0 else 0

        if carry !=0 : result = '1' + result

        r = result.lstrip("0")
        return(r)

def prod(A,B): 
        
        x = int(A, 2)# đổi binary string thành số nguyên gán cho x và y       
        y = int(B, 2)
        
        D = x * y # D mang kết quả hiệu x và y theo kiểu nguyên
        return(format(D, "b"))# xuất D dạng nhị phân
        
def bitwiseAnd(A, B): 
        maxlen = max(len(A), len(B)) 
        A = A.zfill(maxlen) 
        B = B.zfill(maxlen) 
        result = ''
        for i in range(maxlen -1,-1,-1):
            if A[i] == '1' and B[i] == '1':
                result = '1' + result
            else: 
                result = '0' + result
        r = result.lstrip("0")    
        return(r)

def bitwiseOr(A, B): 
        maxlen = max(len(A), len(B)) 
        A = A.zfill(maxlen) 
        B = B.zfill(maxlen) 
        result = ''
        for i in range(maxlen -1,-1,-1):
            if A[i] == '1' or B[i] == '1':
                result = '1' + result
            else: 
                result = '0' + result
        r = result.lstrip("0")    
        return(r)

def bitwiseXor(A, B): 
        maxlen = max(len(A), len(B)) 
        A = A.zfill(maxlen) 
        B = B.zfill(maxlen) 
        result = ''
        for i in range(maxlen -1,-1,-1):
            if A[i] == B[i]:
                result = '0' + result
            else: 
                result = '1' + result
        r = result.lstrip("0")    
        return(r)
    
def bitwiseNot(A):
        result = ''
        for i in A:
            if i == '0' :
                result += '1'
            else:
                result += '0'
            
        r = result.lstrip("0")
        return(r)
    
def bitwiseLeftShift(A):
        x = A[1:] + A[0]
        r = x.lstrip("0")
        return r
        
def bitwiseRightShift(A):
        x = A[-1]+ A[:-1]
        r = x.lstrip("0")
        return r
        
        
def bin2Hex(A):
        result = '' 
        x = A.zfill(64)
        cut = [int(x[i-4:i],2) for i in range(len(x), 0, -4)]
        
        for i in cut:
            result += hex(i)
        d = result.replace("0x","")
        res = (d[::-1])
        c = res.lstrip("0")
        return(c.upper())
        
        
A = '10001011'
B = '10101010101'
        
        
        
        







