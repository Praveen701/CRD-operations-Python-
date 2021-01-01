
import code as x 

x.create("tom",25)

x.create("src",70,3600) 

x.read("tom")

x.read("src")

x.create("tom",50)

x.modify("tom",55)
 
x.delete("tom")

#using multiple threads 
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()