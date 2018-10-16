onoff=False
def priority(fn):
    print("正在检查权限。。。。")
    def fx(name,x):
        if onoff:
            print('权限够')
            fn(name,x)
        else:
            print('权限不够')
            return False
    return fx

def send_info(fn):
    def fx(name,x):
        print(name,'正在存钱',x)
        fn(name,x)
        print(name,'已存',x)
    return fx

@priority
@send_info
def save_money(name,x):
    print(name,'存',x)

save_money('qmy',10000000)

help(sum)