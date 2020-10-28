import socketserver            #导入SocketServer，多线程并发由此类实现
import pymysql
import time



 
class MySockServer(socketserver.BaseRequestHandler):    #定义一个类
 
    def handle(self):      #handle(self)方法是必须要定义的，可以看上面的说明
        print ('Got a new connection from')
        print (self.client_address)
        
        while True:
            data = self.request.recv(1024)#需要通过self的方法调用数据接收函数
            
            if not data:break
            data1=data.decode("utf8")
            print ('recv:')
            print (data1)
            if data1[19]=='A' and data1[20]=='C':
                buf22=str(data1[0:19])
                buf33=str(data1[19:22])
                buf44=str(data1[22:23])
                buf55=str(data1[23:27])
                db = pymysql.connect('localhost','root','123456','userdb',charset='utf8')
                cursor = db.cursor()
                sql =( """INSERT INTO AC(YEAR,NODE,LE,ACGL)VALUES ('%s','%s','%s','%s')"""%(buf22,buf33,buf44,buf55))
            else:
                buf2=str(data1[0:19])
                buf3=str(data1[20:22])
                buf4=str(data1[22:27])
                buf5=str(data1[27:32])
                buf6=str(data1[19:20])
                buf7=str(data1[32:39])
                buf8=str(data1[39:43])
                db = pymysql.connect('localhost','root','123456','userdb',charset='utf8')
                cursor = db.cursor()
                sql =( """INSERT INTO TEM1(YEAR,NODE,TEMP,HUM,MQ,AREA,GL)VALUES ('%s','%s','%s','%s','%s','%s','%s')"""%(buf2,buf3,buf4,buf5,buf7,buf6,buf8))
                
            
            try:
               # 执行sql语句
               cursor.execute(sql)
               
               print (buf2)
               print (buf3)
               print (buf4)
               print (buf5)
               print (buf7)
               print (buf6)
               print (buf8)
               # 提交到数据库执行
               db.commit()
            except:
               # Rollback in case there is any error
               db.rollback()
               db.close()


            self.request.send(b"receive success")   #需要通过self的方法调用数据发送函数


        


if __name__ == '__main__':  
    HOST = '10.21.9.238'             #定义侦听本地地址口（多个IP地址情况下），这里表示侦听所有
    PORT = 50098          #Server端开放的服务端口


    s = socketserver.ThreadingTCPServer((HOST, PORT), MySockServer)
                              #调用SocketServer模块的多线程并发函数
    s.serve_forever()     #持续接受客户端的连接





