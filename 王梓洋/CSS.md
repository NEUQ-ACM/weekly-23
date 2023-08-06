# CSS

## 基础认知

1. css的介绍
   css：层叠样式表

   作用：
   ![image-20230720154236009](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230720154236009.png)

2. css语法规则
   ![image-20230720154410312](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230720154410312.png)

3. 引入方式

   ![image-20230727223800391](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230727223800391.png)

## 基础选择器

### 1.标签选择器

![image-20230727224940141](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230727224940141.png)

### 2.类选择器

![image-20230727225455775](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230727225455775.png)

### 3.id选择器

![image-20230727230214347](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230727230214347.png)

*虽然当id选择器选中两个标签时，CSS可以发挥作用，但是JS可能会出问题*

### 4.通配符选择器

![image-20230727231329721](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230727231329721.png)

## 字体和文本样式

### 字体

1. 字体大小

   ![image-20230727232841789](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230727232841789.png)

2. 字体粗细

   ![image-20230727232929616](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230727232929616.png)

3. 字体样式

   ![image-20230727233308659](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230727233308659.png)

4. 字体系列

   ![image-20230727233454836](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230727233454836.png)

   注：windows默认微软雅黑

   ![image-20230727234231414](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230727234231414.png)

5. 样式的层叠问题

    ![image-20230727234824070](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230727234824070.png)

   *注：后边覆盖前边*

6. font复合属性

   ![image-20230727235232860](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230727235232860.png)

   ![image-20230727235343978](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230727235343978.png)

   *一个冒号后面跟着多个值的写法被称为复合属性*

   *不能省略字号和字体（只能省略前两个）*

### 文本样式

1. 文本缩进

   ![image-20230727235929943](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230727235929943.png)

2. 水平对齐方式

   <a href="https://imgse.com/i/pP9kOaj"><img src="https://s1.ax1x.com/2023/07/31/pP9kOaj.png" alt="pP9kOaj.png" border="0" /></a>

   <u>***注：不仅可以让文本对齐，也可以让图片对齐，让图片对齐时，给body设置***</u>

3. 文本修饰

   <a href="https://imgse.com/i/pP9AyYn"><img src="https://s1.ax1x.com/2023/07/31/pP9AyYn.png" alt="pP9AyYn.png" border="0" /></a>

   ```css
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Document</title>
       <style>
           div{
               text-decoration: underline;
           }
           p{
               text-decoration: line-through;
           }
           h2{
               text-decoration: overline;
           }
           a{
               text-decoration: none;
           }
       </style>
   </head>
   <body>
       <div>div</div>
       <p>p</p>
       <h2>h2</h2>
       <a href="#">我是超链接</a>
   </body>
   ```

   *效果：*

   <a href="https://imgse.com/i/pP9Aql6"><img src="https://s1.ax1x.com/2023/07/31/pP9Aql6.png" alt="pP9Aql6.png" border="0" /></a>

4. 行高

   <a href="https://imgse.com/i/pP9EEnS"><img src="https://s1.ax1x.com/2023/07/31/pP9EEnS.png" alt="pP9EEnS.png" border="0" /></a>

   注：style（倾斜）weight（加粗）size（字体大小）line-height（行高）

   family（字体样式）

## Chrome调试工具

快捷键：F12/FN+F12

## 盒模型

### 内容区（content）

元素中所有子元素和文本内容都在内容区中排列
内容区大小有width和height两个属性来设置
用background-color设置背景颜色

### 内边距（padding）

```css
内容区和边框的距离是内边距
一共有四个方向的内边距：
padding-top
padding-right
padding-bottom
padding-left
内边距的设置会影响到盒子的大小
背景颜色会延伸到内边距上
一个盒子的可见框大小，有内容区你、内边距和边框共同决定，
所以在计算盒子大小时，需要将这三个区域加到一起计算
```

```css
padding内边距的简写属性，可以同时指定四个方向的内边距，规则与border一致
```

### 边框（border）

边框的宽度、颜色、样式
边框大小会影响整个盒子的大小

```css
border-width: 10px;
默认值，一般都是三个像素
border-width可以用来指定四个方向的边框宽度
值的情况:
四个值：上 右 下 左
三个值：上 左右 下
两个值：上下 左右
一个值：上下左右

除了border-width还有一组border-xxx-width
xxx可以是top right bottom left
用来单独指定某一个边的宽度
```

```css
border-color用来指定边框的颜色，同样可以分别制定四个边的边框
规则和border-width一样
border-color可以省略不写，如果省略则自动使用color的颜色值
```

```css
border-style指定边框的样式
默认值是none 表示没有边框
solid表示实线
dotted点状虚线
dashed虚线
double双线
```

```css
border简写属性，通过该属性可以同时设置边框所有的相关样式，并且没有顺序要求
除了border以外还有四个border-xxx
border-top
border-right
border-bottom
border-left
例：
border：solid 10px orange;
border-top:10px solid red;
```

### 外边距（margin）

```css
外边距不影响盒子大小，但影响盒子位置
一共四个方向外边距
margin-top 上外边距，设置一个正值，元素会向下移动
margin-right 右外边距，默认情况下设置margin-right不会产生任何效果
margin-bottom 下外边距，设置一个正值，其下边的元素会向下移动
margin-left 左外边距，设置一个正值，元素会向右移动

也可以设置负值，则向相反方向移动

元素在页面是按照自左向右的顺序排列的
所以默认情况下设置的左和上外边距会移动元素自身
而设置下和右外边距会移动其他元素
```

```css
margin简写属性与以上其他相同
margin会影响到盒子实际占用空间
```

### 盒子的水平布局

<a href="https://imgse.com/i/pPAVKRe"><img src="https://s1.ax1x.com/2023/08/05/pPAVKRe.png" alt="pPAVKRe.png" border="0" /></a>

如果某个值为auto，则会自动调整auto的那个值以使等式成立

## CSS浮动

通过浮动可以使一个元素向其父元素左侧或右侧移动

使用float属性来设置元素的浮动

可选值：

none 默认值，元素不浮动

left 元素向左浮动

right 元素向右浮动

注意：

1. 元素设置浮动以后，水平布局的等式便不需要强制成立
2. 元素设置浮动以后，会完全从文档流中脱离，不再占用文档流的位置，所以元素下边的还在文档流中的元素会自动向上移动，设置浮动的元素会覆盖向上移动的元素

## CSS定位

通过定位可以将元素摆放到页面的任意位置，使用position属性来设置定位

可选值：

**static** 默认值，元素是静止的，没有开启定位

**relative** 开启元素的相对定位

**absolute** 开启元素的绝对定位

**fixed** 开启元素的固定定位

**sticky** 开启元素的粘滞定位

