# node.js

## cmd常用命令

<a href="https://imgse.com/i/pPVIcpF"><img src="https://s1.ax1x.com/2023/08/08/pPVIcpF.png" alt="pPVIcpF.png" border="0" /></a>

**注：dir /s查看文件夹所有程序 **
**CTRL+C停止输出**

## NodeJS编码注意事项

<a href="https://imgse.com/i/pPVoC9S"><img src="https://s1.ax1x.com/2023/08/08/pPVoC9S.png" alt="pPVoC9S.png" border="0" /></a>

<a href="https://imgse.com/i/pPVoeA0"><img src="https://s1.ax1x.com/2023/08/08/pPVoeA0.png" alt="pPVoeA0.png" border="0" /></a>

## Buffer（缓冲器）

<a href="https://imgse.com/i/pPVoQc4"><img src="https://s1.ax1x.com/2023/08/08/pPVoQc4.png" alt="pPVoQc4.png" border="0" /></a>

### 创建Buffer方法

1. alloc

   ```js
   let buf = Buffer.alloc(10);
   ```

2. allocUnsafe

   ```js
   let buf_2 = Buffer.allocUnsafe(10000);
   ```

3. from

   ```js
   let buf_3 = Buffer.from('hello');
   
   let buf_4 = Buffer.from([105,108,111,118,101,121,111,117]);
   ```

<a href="https://imgse.com/i/pPV7jB9"><img src="https://s1.ax1x.com/2023/08/08/pPV7jB9.png" alt="pPV7jB9.png" border="0" /></a>

*toString(2)可以查看二进制结果*

修改的数据超过255时，会舍弃高位的数字

## 计算机基本组成

### CPU

### 内存

读写速度较快，断电丢失数据

<a href="https://imgse.com/i/pPZPvHx"><img src="https://s1.ax1x.com/2023/08/08/pPZPvHx.png" alt="pPZPvHx.png" border="0" /></a>

### 硬盘

读写速度较慢，断电不丢失数据

![image-20230808212006915](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230808212006915.png)

<a href="https://imgse.com/i/pPZimUf"><img src="https://s1.ax1x.com/2023/08/08/pPZimUf.png" alt="pPZimUf.png" border="0" /></a>

### 主板

<a href="https://imgse.com/i/pPZFZQJ"><img src="https://s1.ax1x.com/2023/08/08/pPZFZQJ.png" alt="pPZFZQJ.png" border="0" /></a>

### 显卡

处理信号

### 计算机启动的基本过程

操作系统安装到硬盘，之后载入内存

<a href="https://imgse.com/i/pPZF5fU"><img src="https://s1.ax1x.com/2023/08/08/pPZF5fU.png" alt="pPZF5fU.png" border="0" /></a>

### 程序运行的基本过程

应用程序安装到硬盘，之后载入内存

<a href="https://imgse.com/i/pPZkp1e"><img src="https://s1.ax1x.com/2023/08/08/pPZkp1e.png" alt="pPZkp1e.png" border="0" /></a>

<a href="https://imgse.com/i/pPZk96H"><img src="https://s1.ax1x.com/2023/08/08/pPZk96H.png" alt="pPZk96H.png" border="0" /></a>

### 进程与线程

进程：进行中的程序（在任务管理器查看）

线程：一个进程可以包含多个线程

<a href="https://imgse.com/i/pPZkQns"><img src="https://s1.ax1x.com/2023/08/08/pPZkQns.png" alt="pPZkQns.png" border="0" /></a>

## fs模块（file system）

<a href="https://imgse.com/i/pPZkt9U"><img src="https://s1.ax1x.com/2023/08/08/pPZkt9U.png" alt="pPZkt9U.png" border="0" /></a>

### 写入文件

1. 异步写入（效率更高）

   ```js
   //导入fs模块
   const fs =require('fs');
   //写入文件
   fs.writeFile('./座右铭.txt', '三人行,则必有我师焉', err => {
       //err写入失败：错误对象  写入成功：null
       if(err){
           console.log('写入失败');
           return;
       }
       console.log('写入成功');
   });
   ```

   分为两个线程：JS（主线程，不会等其他线程）和I/O线程（等主线程执行完再执行）

2. 同步写入

   ```js
   fs.writeFileSync('./data.txt','test');
   ```


3. 追加写入

   ```js
   fs.appendFile('./座右铭.txt','择其善者而从之'）;
   ```

   ```js
   fs.writeFile('./座右铭.txt','择其善者而从之',{flag:'a'});
   ```


4. 文件流式写入
   <a href="https://imgse.com/i/pPmwWsU"><img src="https://s1.ax1x.com/2023/08/10/pPmwWsU.png" alt="pPmwWsU.png" border="0" /></a>

5. 写入文件的场景
   <a href="https://imgse.com/i/pPmw4Z4"><img src="https://s1.ax1x.com/2023/08/10/pPmw4Z4.png" alt="pPmw4Z4.png" border="0" /></a>

### 文件读取

<a href="https://imgse.com/i/pPmwOsO"><img src="https://s1.ax1x.com/2023/08/10/pPmwOsO.png" alt="pPmwOsO.png" border="0" /></a>

1. 异步读取

   ```js
   const fs=require('fs');
   
   fs.readFile('./静夜思.txt',(err,data)=>{
       if(err){
           console.log('读取失败');
           return;
       }
       console.log(data.toString());
   });
   
   ```

2. 同步读取

   ```js
   const fs=require('fs');
   
   let data =fs.readFileSync('./静夜思.txt');
   
   console.log(data.toString());
   ```

3. 读取文件的应用场景
   <a href="https://imgse.com/i/pPmBh59"><img src="https://s1.ax1x.com/2023/08/10/pPmBh59.png" alt="pPmBh59.png" border="0" /></a>

4. 文件流式读取（占用内存少）
   <a href="https://imgse.com/i/pPmDNxx"><img src="https://s1.ax1x.com/2023/08/10/pPmDNxx.png" alt="pPmDNxx.png" border="0" /></a>

### 文件重命名与移动

1. 文件重命名
   <a href="https://imgse.com/i/pPmrky6"><img src="https://s1.ax1x.com/2023/08/10/pPmrky6.png" alt="pPmrky6.png" border="0" /></a>

2. 文件的移动
   <a href="https://imgse.com/i/pPmreTe"><img src="https://s1.ax1x.com/2023/08/10/pPmreTe.png" alt="pPmreTe.png" border="0" /></a>

### 文件的删除

<a href="https://imgse.com/i/pPmrKfA"><img src="https://s1.ax1x.com/2023/08/10/pPmrKfA.png" alt="pPmrKfA.png" border="0" /></a>

还有一种rm方法：

<a href="https://imgse.com/i/pPmr3Of"><img src="https://s1.ax1x.com/2023/08/10/pPmr3Of.png" alt="pPmr3Of.png" border="0" /></a>

