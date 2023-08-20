# HTML语义化案例分析

<a href="https://imgse.com/i/pP3aFk8"><img src="https://s1.ax1x.com/2023/08/18/pP3aFk8.png" alt="pP3aFk8.png" border="0" /></a>



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>青春不常在，抓紧谈恋爱</h1>
    <hr>
    <form action="">
        昵称：<input type="text" placeholder="请输入昵称">
        <br>
        <br>
        性别：
        <label><input type="radio" name="sex">男</label>
        <label><input type="radio" name="sex">女</label>
        <br>
        <br>
        所在城市：
        <select name="" id="">
            <option value="">北京</option>
            <option value="">上海</option>
            <option value="">广州</option>
            <option value="">深圳</option>
        </select>
        <br>
        <br>
        婚姻状况：
        <label><input type="radio" name="marry">未婚</label>
        <label><input type="radio" name="marry">已婚</label>
        <label><input type="radio" name="marry">保密</label>
        <br>
        <br>
        喜欢的类型：
        <label><input type="checkbox">可爱</label>
        <label><input type="checkbox">性感</label>
        <label><input type="checkbox">御姐</label>
        <label><input type="checkbox">萝莉</label>
        <label><input type="checkbox">小鲜肉</label>
        <label><input type="checkbox">大叔</label>
        <label><input type="checkbox">呆子</label>
        <br>
        <br>
        个人介绍：
        <br>
        <textarea name="" id="" cols="50" rows="20"></textarea>
        <br>
        <br>
        <strong>我承诺</strong>
        <ul>
            <li>年满18、单身</li>
            <li>抱着严肃的态度</li>
            <li>真诚寻找另一半</li>
        </ul>
        <br>
        <br>
        <input type="checkbox" checked>我同意所有条款
        <br>
        <br>
        <button type="submit">免费注册</button>
        <button type="reset">重置</button>
    </form>
</body>
</html>
```

这是典型的表单标签的例子，那表单标签是什么呢

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

   