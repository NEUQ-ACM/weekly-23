# HTML

## 学习笔记

### 基础概念

1.网页由**文字、图片、音频、视频、超链接**组成

2.通过**浏览器**转化 前端的代码 为客户看到的网页

3.常见的五大浏览器：IE浏览器、火狐浏览器（Firefox）、谷歌浏览器(Chrome)、Safari浏览器、欧朋浏览器(Opera)

4.渲染引擎（浏览器内核）：浏览器中专门对代码进行解析渲染的部分
*注意：**渲染引擎不同，导致解析相同代码的速度、性能、效果也不同的*

5.Web标准的构成：

- 结构：HTML  **页面的元素和内容**
- 表现：CSS  **网页元素的外观和位置等页面样式（如颜色、大小）**
- 行为：JS (JavaScript)  **网页模型的定义与页面交互（让画面动起来）**

### HTML初体验

1.HTML（超文本标记语言）*遵循语法规则*

例：

`<strong>xxxxxx</strong>`

**标签标记用‘<>’,有开始有结束**

2.HTML页面固定结构

网页中的固定结构是要通过特点的**HTML标签**进行描述的

`<html>`

<head>
    <title>网页的标题</title>
</head>
`<body>`

`网页的主体内容`

`</body>`

`</html>`

3.开发工具

VS Code(Visual Studio Code)

新建的文件要加“.html”后缀

新建文件后，输入**！+ ENTER/TAB键**，html骨架自动出现

**CTRL+s** 存储文件，文件未保存的时候，文件名旁边会显示一个小圆点

**ALT+B** 跳转到网页

### 语法规范

1. 注释
   CTRL+/ 按一次有注释，再按一次注释取消

2. HTML标签的构成
   ![image-20230627231533215](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230627231533215.png)
   `<br>`换行
   `<hr>`分割线
   单标签：不需要确定开始结束，只有开始即可
   双标签：需要确定开始结束

3. 标签与标签之间的关系
   父子关系（嵌套关系）

   <head>
       <title></title>
   </head>


   兄弟关系（并列关系）

   <head></head>

   <body></body>

#### 排版标签

1. 标题标签
   ![image-20230627232916594](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230627232916594.png)

如果要复制n个同级标题，可以 h2*n + ENTER/TAB
*输入标题标签的简便方法：*
*例：h1+ENTER/TAB*
CTRL+F2 批量文本替换

2. 段落标签
   ![image-20230628090447540](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230628090447540.png)
   ALT+Z 自动换行（查看—自动换行)
   CSS可以改变段落中的间隙
   **HTML框架，CSS表达，JS行为**
3. 换行标签
   ![image-20230628091759714](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230628091759714.png)
   在想要换行的文字后加<br>
4. 水平线标签
   ![image-20230628091959251](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230628091959251.png)
   在想要加分割线的位置加<hr>

#### 文本格式化标签

![image-20230628092346586](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230628092346586.png)

**突出重要性的强调语境时，用右侧的标签**（方便程序员理解）
但是左右两侧标签显示的效果没有区别

#### 媒体标签

1. 图片标签

   ![image-20230628092938967](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230628092938967.png)
   ![image-20230628093940815](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230628093940815.png)
   引号里写"./"+图片的文件名（如果图片在当前文件夹)
   **属性：**

   1. src属性
   2. alt属性
      ![image-20230628094512898](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230628094512898.png)
   3. title属性
      ![image-20230628094634520](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230628094634520.png)
   4. width和height属性
      ![image-20230628094823523](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230628094823523.png)
      ***一般只需给出一个值***

2. 路径

   路径分为：
   绝对路径（了解）
   相对路径（常用）
   ![image-20230628095732124](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230628095732124.png)
   ![image-20230628100158506](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230628100158506.png)

   **同级目录：**当前文件和目标文件在同一目录中
   **下级目录：**目标文件在下级目录中
   ![image-20230628100818599](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230628100818599.png)
   *"/"表示image是文件夹*
   **上级目录：**目标文件在上级目录中
   ![image-20230628101245799](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230628101245799.png)
   
   3.音频标签 
   
   ![image-20230713173728065](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230713173728065.png)
   注：音频标签目前支持三种格式：MP3、Wav、Ogg
   
   4.视频标签
   ![image-20230713182527289](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230713182527289.png)
   
   ![image-20230713204242821](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230713204242821.png)

#### 链接标签

![image-20230714115910381](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230714115910381.png)
![image-20230714124352144](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230714124352144.png)

*href= 跳转地址*

![image-20230714125916521](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230714125916521.png)

index.html  首页

#### 列表标签

1. 应用场景：要求排列规整

2. 分类：
   ![image-20230714142611112](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230714142611112.png)

3. 无序列表
   ![image-20230714142838734](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230714142838734.png)

   ```
   <ul>
           <li>榴莲</li>
           <li>香蕉</li>
           <li>苹果</li>
       </ul>
   ```

   4.有序列表

   ![image-20230714143423786](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230714143423786.png)

   ```
   <ol>
           <li>张三：100</li>
           <li>李四:80</li>
           <li>王二麻子:75</li>
       </ol>
   ```

   5.自定义列表
   ![image-20230718121516769](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718121516769.png)
   注：
   
   1. dd前会默认显示缩进效果
   2. dl标签只允许包含dt/dd标签
   3. dt/dd标签可以包含任意内容

#### 表格标签

1. 表格的基本标签
   ![image-20230718122622232](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718122622232.png)
   
   ```html
   <table>
           <tr>
           <td>姓名</td>
           <td>成绩</td>
           <td>评语</td>
           </tr> 
           <tr>
               <td>A</td>
               <td>100分</td>
               <td>勤奋好学</td>
           </tr>
           <tr>
               <td>B</td>
               <td>80分</td>
               <td>聪明但不努力</td>
           </tr>
           <tr>
               <td>C</td>
               <td>95分</td>
               <td>未来可期</td>
           </tr>
       </table>
   ```
   
   ***效果：***
   ![image-20230718143220072](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718143220072.png)
   **没有横格线，为了添加横格线，需要给表格添加相关属性**

2. 表格相关属性
   ![image-20230718143602864](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718143602864.png)

   ```html
   <table border="1">
           <tr>
           <td>姓名</td>
           <td>成绩</td>
           <td>评语</td>
           </tr> 
           <tr>
               <td>A</td>
               <td>100分</td>
               <td>勤奋好学</td>
           </tr>
           <tr>
               <td>B</td>
               <td>80分</td>
               <td>聪明但不努力</td>
           </tr>
           <tr>
               <td>C</td>
               <td>95分</td>
               <td>未来可期</td>
           </tr>
       </table>
   ```

   ![image-20230718143736188](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718143736188.png)

3. 表格标题和表头单元格标签
   ![image-20230718145747021](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718145747021.png)

   ```html
   <table border="1">
           <caption><strong>学生成绩单</strong></caption>
           <tr>
           <th>姓名</th>
           <th>成绩</th>
           <th>评语</th>
           </tr> 
           <tr>
               <td>A</td>
               <td>100分</td>
               <td>勤奋好学</td>
           </tr>
           <tr>
               <td>B</td>
               <td>80分</td>
               <td>聪明但不努力</td>
           </tr>
           <tr>
               <td>C</td>
               <td>95分</td>
               <td>未来可期</td>
           </tr>
       </table>
   ```

   ***效果：***
   ![image-20230718150056176](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718150056176.png)

4. 表格的结构标签（了解）
   ![image-20230718150159006](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718150159006.png)

   **代码往后缩进用TAB，往前缩进用SHIFT+TAB**

   ```html
   <table border="1">
           <caption><strong>学生成绩单</strong></caption>
           <thead>
               <tr>
                   <th>姓名</th>
                   <th>成绩</th>
                   <th>评语</th>
               </tr> 
           </thead>
           <tbody>
               <tr>
                   <td>A</td>
                   <td>100分</td>
                   <td>勤奋好学</td>
               </tr>
               <tr>
                   <td>B</td>
                   <td>80分</td>
                   <td>聪明但不努力</td>
               </tr>
               <tr>
                   <td>C</td>
                   <td>95分</td>
                   <td>未来可期</td>
               </tr>
           </tbody>
           <tfoot>
               <tr>
                   <td>总结</td>
                   <td>教学成果取得阶段性胜利</td>
                   <td>教学成果取得阶段性胜利</td>
               </tr>
           </tfoot>
       </table>
   ```

​		**效果：与之前没有区别**

​		**作用：提高浏览器的执行效率**

5. 合并单元格
   ![image-20230718151731958](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718151731958.png)

   ```html
   <tbody>
               <tr>
                   <td>A</td>
                   <td rowspan="2">100分</td>
                   <td>勤奋好学</td>
               </tr>
               <tr>
                   <td>B</td>
                   <td>聪明但不努力</td>
               </tr>
               <tr>
                   <td>C</td>
                   <td>95分</td>
                   <td>未来可期</td>
               </tr>
           </tbody>
   ```

   ***效果：***

   ![image-20230718152259356](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718152259356.png)

#### 表单标签

1. input系列标签
   ![image-20230718152800539](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718152800539.png)

   ```html
   <body>
       <!-- 写什么就显示什么 -->
       文本框：<input type="text">
       <br>
       <br>
       <!-- 书写的内容都会变成点点显示 -->
       密码框：<input type="password">
       <br>
       <br>
       单选框：<input type="radio">
       <br>
       <br>
       多选框：<input type="checkbox">
       <br>
       <br>
       文件选择：<input type="file">
   </body>
   ```

   ***效果：***

   ![image-20230718154318037](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718154318037.png)
   ***注：***
   ***勾选同意此条款时所用的框是多选框***
   ![image-20230718154553386](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718154553386.png)

   ```html
       文本框：<input type="text" placeholder="请输入用户名">
       <br>
       <br>
       <!-- 书写的内容都会变成点点显示 -->
       密码框：<input type="password" placeholder="请输入密码">
   ```

   ***效果：***

   ![image-20230718154902945](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718154902945.png)
   ![image-20230718155421027](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718155421027.png)

   ```html
   <body>
       性别：<input type="radio" name="sex">男  <input type="radio" name="sex" checked>女
   </body>
   ```

   ***效果：***
   ![image-20230718155718505](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718155718505.png)
   （此时限定只能选一个)
   **默认选中用checked**（多选框也可以用)
   ![image-20230718160058575](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718160058575.png)

   ```html
   <body>
       <input type="file" multiple>
   </body>
   ```

   （CTRL+A 全选）

   ![image-20230718160945643](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718160945643.png)
   **value可以给按钮重命名**

   ```html
   <body>
       <form action="">
           用户名: <input type="text">
           <br>
           <br>
           密码：<input type="password">
           <br>
           <br>
           <!-- 按钮 -->
           <input type="submit">
           <input type="reset">
           <input type="button" value="普通按钮">
       </form>
   </body>
   ```

   ***效果：***
   ![image-20230718163020301](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718163020301.png)

   ```html
   <body>
       <form action="">
           用户名: <input type="text">
           <br>
           <br>
           密码：<input type="password">
           <br>
           <br>
           <!-- 按钮 -->
           <input type="submit" value="免费注册">
           <input type="reset">
           <input type="button" value="普通按钮">
       </form>
   </body>
   ```

   ***效果：***
   ![image-20230718163228438](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718163228438.png)

2. button按钮标签

   ![image-20230718163419600](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718163419600.png)

   ```html
   <body>
       <button>我是按钮</button>
       <button type="submit">提交按钮</button>
       <button type="reset">重置按钮</button>
       <button type="button">普通按钮，没有任何功能</button>
   </body>
   ```

   ***效果：***
   ![image-20230718164333467](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230718164333467.png)

3. select下拉菜单标签
   ![image-20230719111739104](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230719111739104.png)
   ***若不设置默认选中，那默认选中的就是第一个option标签里的内容***

   ```html
   <body>
       <select name="" id="">
           <option value="">北京</option>
           <option value="">上海</option>
           <option value="">广州</option>
       </select>
   </body>
   ```

   ***效果：***
   ![image-20230719112307445](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230719112307445.png)

   ```html
   <body>
       <select name="" id="">
           <option value="">北京</option>
           <option value="">上海</option>
           <option value="" selected>广州</option>
       </select>
   </body>
   ```

   效果：
   ![image-20230719112520690](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230719112520690.png)

4. textarea文本域标签
   ![image-20230719112708103](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230719112708103.png)

   ```html
   <body>
       <textarea name="" id="" cols="30" rows="10"></textarea>
   </body>
   ```

5. label标签
   ![image-20230719113257594](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230719113257594.png)
   法一：

   ```html
   <body>
       性别：
       <!-- id引号里的内容要和for引号里内容一致 -->
       <input type="radio" name="sex" id="nan"> <label for="nan">男</label>
       <input type="radio" name="sex" id="nv"> <label for="nv">女</label>
   </body>
   ```

   法二：

   ```html
   <body>
       性别：
       <label><input type="radio" name="sex">男</label>
       <label><input type="radio" name="sex">女</label>
   </body>
   ```
   
   ![image-20230719114638990](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230719114638990.png)
   ***当使用label标签时，不点单选文本框，点男或女也是可以选中的***

#### 语义化标签

1. 没有语义的布局标签
   ![image-20230720140541371](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230720140541371.png)

   ```html
   <body>
       <div>这是div标签</div>
       <div>这是div标签</div>
       <span>这是span标签</span>
       <span>这是span标签</span>
   </body>
   ```

   效果：

   ![image-20230720141000957](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230720141000957.png)

2. 有语义的布局标签（了解）

   **注：做手机端网页时用的标签**
   ![image-20230720141232846](C:\Users\bjwq_\AppData\Roaming\Typora\typora-user-images\image-20230720141232846.png)

#### 字符实体

1. HTML中的空格合并现象

   网页不认识多个空格

2. 常见字符实体

   ```
   空格 &nbsp;
   ```

   
