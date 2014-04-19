#1最简单最直接的处理方式： 假定我们在写代码的时候，有的时候怕程序会出问题，就会在可能出问题的地方用上try exception来捕获程序出现的错误。
 
try:
    a = 1/0
except Exception,e:
    print e
#输出的结果是： integer division or modulo by zero
 
#2在其中加了个判断： 我们在写一断程序的时候，想如果有异常就输出异常，如果没异常就继续执行下面的语句那该怎么做呢？ 就要用到try exception else: 比如:
 
try:
    a = 1/2
except Exception,e:
    print e
else:
    print 'success'
#输出的结果是success，因为上面的a = 1/2没有报错，它会执行else后面的语句，就像python 控制语句的iif else的效果一样， 如果上面的程序有异常就执行except后面的语句,输出异常，如果没有异常的话，就会执行else后面的语句，
 
#3不管有没异常都要执行： 这个情况主要是如果你要操作什么的东西，比如文件或者网络等，不管它是否发生异常最后都要关闭资源，比如关闭文件等。
 
try:
    f = file('1.txt','w')
    f.write('fefe')
except Exception,e:
    print e
finally:
    f.close()
#上面假设我们在打开文件或者写内容的时候出错的话，会执行print e，接着会执行f.close()关闭文件，有点像类的析构方法 作最后的收尾工作，其实不一定是有异常才会执行finally后面的方法，就算语句没有出现异常的话，也会执行finally后面的语句，你可以自己实验下看下效果。 我一般写程序用到python exception的话，主要就是上面的3种解决方法了。
