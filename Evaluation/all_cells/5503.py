#Parameter对象
    #保存在元组中，是只读的
    #name 参数的名字
    #annotation 参数的注解 可能没有定义
    #default 参数的缺省值，可能没有定义
    #empty 特殊的类 用来标记default属性或者注释annotation属性的空值
    #kind 实参如何绑定到形参，就是形参的类型
        #POSITIONAL_ONLY 值必须是位置参数提供
        #POSITIONAL_OR_KEYWORD 值可以作为关键字或者位置参数提供
        #VAR_POSITIONAL 可变位置参数 对应*args
        #KEYWORD_OLY keyword-only参数，对应*或者args之后的出现的非可变关键字参数
        #VAR_KEYWORD 可变关键字参数，对应**kwargs.
        
        