#generics ở đây là giá trị "_" trong methodreturn_values tại sao nó là
#generics bởi nếu ng lập trình nào đó ko biết sẽ truyền cụ thẻ gì vào hàm này
#thì họ sẽ chỉ cần để "_" thì dù bạn có truyền vào kiểu string hay int hay double hay object lis...đều được
def  return_values(_):
    return _
print(return_values("hello Th Tuan"))
