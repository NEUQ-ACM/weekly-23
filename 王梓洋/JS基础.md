# JS基础

**JS代码需要编写在script标签中**

```javascript
<script>
        /*控制浏览器弹出一个警告框*/  
        alert("这是我的第一行JS代码");
        /*让计算机在页面中输出一个内容
        document.write()可以向body中输出一个内容
        */ 
        document.write("hello");
        /*向控制台输出一个内容
        console.log()向控制台输出
        */
        console.log("world");
</script>
```

**语法规则：**

1. 单行注释：//

2. 多行注释：/**/

3. JS严格**区分大小写**

4. JS每一条语句以分号结尾（;）如果不写分号，浏览器会自动添加，但是会消耗一些系统资源

5. JS会忽略多个空格和换行

6. 在JS中使用var来声明变量

   ```javascript
   var a;
   ```

7. 标识符可以含有字母、数字、_、$
   标识符不能是ES中的关键字或保留字
   <a href="https://imgse.com/i/pPAhO61"><img src="https://s1.ax1x.com/2023/08/06/pPAhO61.png" alt="pPAhO61.png" border="0" />

   </a>

   标识符一般采用驼峰命名法（首字母小写，每个单词开头字母大写，其余字母小写）

## JS数据类型

***基本数据类型六种，最基本数据类型五种（除object对象）***

### 检查一个变量的类型

```js
console.log(typeof a);
```

<a href="https://imgse.com/i/pPA4Dj1"><img src="https://s1.ax1x.com/2023/08/06/pPA4Dj1.png" alt="pPA4Dj1.png" border="0" /></a>

### String 字符串

***JS中字符串需要使用引号引起来***（双引号单引号都可，但是不能混着用）

引号不能嵌套，双引号不能放双引号，单引号不能放单引号，但可以外双内单或外单内双

```js
var str="hello";
```

***当表示一些特殊符号时可以使用\进行转义***

```js
\" 表示"
\' 表示'
\n 换行
\t 制表符(相当于TAB键)
\\表示\
\\\\表示\\
\\\\\\表示\\\
```

### Number  数值

1. 包括整数和浮点数
2. JS可以输出的最大值是Number.MAX_VALUE，约等于1.79769e+308
   最小值是Number.MIN_VALUE（大于0的最小值），约等于5e-324
3. 如果使用Number表示的数字超过了最大值，则会返回一个Infinity(表示正无穷)，
   -Infinity（表示负无穷）
4. 使用时不要加引号，直接a=Infinity
5. 使用 typeof 检查 Infinity 也会返回Number
6. NaN是一个特殊的数字，表示 not a number，使用 typeof 检查也会返回 Number

### Boolean 布尔值

布尔值只有两个，主要来做逻辑判断

true为真

false为假

```js
var bool=true;
```

### Null 空值

Null类型值只有一个，就是null

专门表示一个为空的对象

使用 typeof 检查会返回 object

### Undefined 未定义

类型值只有一个，就undefined

当声明一个变量，但未给变量赋值时，它的值就是undefined

使用 typeof 检查也会返回 undefined

### Object 对象

1. 内建对象：由ES标准中定义的对象，在任何的ES的实现中都可以使用
   如：Math String Number...
2. 宿主对象：由JS的运行环境提供的对象，目前来讲主要指由浏览器提供的对象
   如：BOM DOM
3. 自定义对象：由开发人员自己创建的对象

## 强制类型转换

主要是将其他数据类型转换为string、number 、boolean

### 转换为string

1. **调用**被转换数据类型的toString()方法
   *该方法不会影响到原变量,它会将转换的结果返回*
   注：以后提到调用就用"."

   ```js
   var a=123;
   var b=a.toString();
   ```

   null和undefined这两个值没有toString,如果转化为string时用法一，会报错

2. 调用String函数

   ```js
   a=123;
   a=String(a);
   ```

### 转换为Number

#### 分类

1. 使用Number()函数
   如果字符串中有非数字的内容，转数字时，转换为NaN
   如果字符串是一个空串或者是一个全是空格的字符串，则转换为0
   true转为1，false转为0
   null转为0
   undefined转为NaN
2. parseInt() 把一个字符串中有效的整数内容取出来（遇到除数字以外的字符，停止识别），转换为一个number整数
   parseFloat() 把一个字符串转换为一个浮点数
   对于非string使用parseInt() 和parseFloat()，会先将其转换为string再操作

#### 创建对象

```js
var obj=new Object();
```

```js
var obj ={};
//也可以用对象字面量创建对象，对象字面量的属性名可以加引号也可以不加
//语法：{属性名：属性值，属性名：属性值，，，}
```

*注：*
*用new调用的函数，是构造函数constructor*
*构造函数是专门用来创建对象的函数*
*使用typeof检查一个对象时，会返回object*

**在对象中保存的值被称为属性，属性也可以是对象
向对象添加属性
			语法：对象.属性名=属性值；**

**如果要使用特殊的属性名，不能采用.的方式来操作**
**需要使用另一种方式：**
			**语法：对象【“属性名”】=属性值**
**读取也要采用这种方式**

例：向a中添加一个name属性

```js
var a=new Object();
a.name="孙悟空"；
a.gender="男"；
a.age=18；
```

#### 读取对象中的属性

```js
console.log(a.gender);
console.log(a.hello);
```

如果读取对象中没有的属性，不会报错而是会返回undefined

#### 修改对象中的属性

语法：对象.属性名=新值

#### 删除对象的属性

语法：delete 对象.属性名

```js
delete a.name;
```

#### in运算符

可以检查一个对象中是否含有指定的属性
如果有返回true，没有返回false
语法：
“属性名”  in  对象

例：检查obj中是否含有test2属性

```js
console.log("test2" in obj);
```

### 转换为Boolean

**只有一种方式，使用boolean() 函数**

1. 数字转布尔
   0和NaN是false
   其他数字是true
2. 字符串转布尔
   空字符串是false
   其余都是true
3. null和undefined都会转换为false
4. 对象也会转换为true

## 函数

### 创造函数

创造一个函数对象

```js
var fun = new Function("console.log('Hello 这是我的第一个函数')；")
```

使用**函数声明**来创建一个函数

```js
function 函数名([形参1,形参2...形参N]){

}
```

函数内部可以再声明一个函数

使用**函数表达式**来创建一个函数

```js
var 函数名=function([形参1,形参2...形参N]){
    
}
```

### 返回值

在函数return后语句都不会执行

如果return后不跟值，或者不写return，都会返回undefined

例：

<a href="https://imgse.com/i/pPum8Cd"><img src="https://s1.ax1x.com/2023/08/12/pPum8Cd.png" alt="pPum8Cd.png" border="0" /></a>

如果该式成立，返回true，该式不成立，返回false

如果 return 10；那么返回值就是10

返回值可以是任意的数据类型，也可以是一个对象

### 实参

当我们的参数过多时，可以将参数封装到一个对象中，然后通过对象传递

```js
function sayHello(o){
    console.log("我是"+o.name+"，今年"+o.age+"岁，是一个"+o.gender+"人，我住在"+o.address)
}

var obj={
    name:"孙悟空",
    age:18,
    gender:"男",
    address:"花果山",
}

sayHello(obj);
```

```js
function fun(a){
console.log("a="+a);
}
fun(sayHello);
//把函数当作参数
```

### 立即执行函数

<a href="https://imgse.com/i/pPunFqf"><img src="https://s1.ax1x.com/2023/08/12/pPunFqf.png" alt="pPunFqf.png" border="0" /></a>

### this

<a href="https://imgse.com/i/pPuMEdK"><img src="https://s1.ax1x.com/2023/08/12/pPuMEdK.png" alt="pPuMEdK.png" border="0" /></a>

### 使用工厂方法创建对象

通过该方法可以**批量**的创建对象

```js
function createPerson(name ,age ,gender){
    //创建新的对象
    var obj=new Object();
    //向对象中添加属性
    obj.name =name;
    obj.gender=gender;
    obj.sayName=function(){
        alert(this.name);
    };
    //将新的对象返回
    return obj;
}
```

### 构造函数

<a href="https://imgse.com/i/pPu4CLQ"><img src="https://s1.ax1x.com/2023/08/13/pPu4CLQ.png" alt="pPu4CLQ.png" border="0" /></a>

<a href="https://imgse.com/i/pPu4kon"><img src="https://s1.ax1x.com/2023/08/13/pPu4kon.png" alt="pPu4kon.png" border="0" /></a>

<a href="https://imgse.com/i/pPu4VJ0"><img src="https://s1.ax1x.com/2023/08/13/pPu4VJ0.png" alt="pPu4VJ0.png" border="0" /></a>
