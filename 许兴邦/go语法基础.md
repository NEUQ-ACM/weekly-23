# Go 语法基础

## 1. 结构体

Go语言中的结构体是一种用户定义的数据类型，可以用来表示一组相关字段的集合。在代码示例中，我们定义了一个名为"user"的结构体，用于表示用户的信息，包括姓名(name)和密码(password)。结构体可以拥有方法，这些方法可以对结构体进行操作。

### 方法1：checkPassword

`checkPassword`方法用于检查用户密码是否正确。它接收一个字符串参数password，并返回一个布尔值表示密码是否匹配。

### 方法2：resetPassword

`resetPassword`方法用于重置用户的密码。它接收一个字符串参数password，并将结构体中的密码字段更新为新密码。

### 主函数main

在主函数中，我们首先创建一个用户实例`a`，并通过调用`resetPassword`方法将其密码重置为"2048"。然后，我们调用`checkPassword`方法检查密码是否正确，并输出结果。


```go
// 定义一个用户结构体
type user struct{
    name string
    password string
}

// 定义一个检查密码是否正确的方法
func(u user) checkPassword(password string) bool{
    return u.password==password
}

// 定义一个重置密码的方法
func (u *user) resetPassword(password string){
    u.password=password
}

func main() {
    // 创建一个用户实例
    a:=user{name:"w",password: "1024"}
    // 重置密码
    a.resetPassword("2048")

    // 检查密码是否正确并输出结果
    fmt.Println(a.checkPassword("2048"))
}
```





## 2. JSON处理

JSON（JavaScript Object Notation）是一种常用的数据交换格式，Go语言提供了对JSON的编码和解码支持。在代码示例中，我们定义了一个用户结构体，其中年龄字段使用了`json`标签。

### json.Marshal

`json.Marshal`函数将用户结构体转换为JSON格式的字节切片。

### json.MarshalIndent

`json.MarshalIndent`函数将用户结构体转换为JSON格式的字节切片，并进行格式化，增加了可读性。

### json.Unmarshal

`json.Unmarshal`函数用于将JSON格式的数据解码为用户结构体。



```go
// 导入必要的包
package main

import (
	"encoding/json" // 导入json包
	"fmt" // 导入fmt包
)

// 定义用户结构体
type user struct {
	name     string // 用户名
	Age      int `json:"age"` // 年龄，使用json标签
	Password []string // 密码，使用字符串切片
}

// 主函数
func main() {
	// 创建用户实例
	a := user{name: "12w", Age: 18, Password: []string{"q421"}}
	// 将用户实例转换为json格式
	buf, err1 := json.Marshal(a)
	if err1 != nil {
		panic(err1)
	}
	// 输出json格式的用户实例
	fmt.Println(buf)
	// 输出json格式的用户实例，转换为字符串格式
	fmt.Println(string(buf))

	// 将用户实例转换为json格式，并进行格式化
	buf, err1 = json.MarshalIndent(a, "", "\t")
	if err1 != nil {
		panic(err1)
	}
	// 输出格式化后的json格式的用户实例，转换为字符串格式
	fmt.Println(string(buf))

	// 将json格式的用户实例转换为用户结构体
	var b user
	err1=json.Unmarshal(buf,&b)
	if err1!=nil{
		panic(err1)
	}
	// 输出转换后的用户结构体
	fmt.Printf("%#v",b)
}
```



## 3. 数字解析

在Go语言中，`strconv`包提供了字符串和基本数据类型之间的转换函数。在代码示例中，我们使用`strconv.ParseFloat`函数将字符串"1.1234"转换为浮点型数值。

> strconv是Go语言中的一个标准内置包，它提供了各种函数实现，用于将字符串转换为int, float, boolean等类型。


```go
func ParseT(inputstring string, bitSize int) (精度, error)  
```

```go
package main

import(
    "fmt"
    "strconv"
)
func main(){
    f,_:=strconv.ParseFloat("1.1234",64)//转化为浮点型
    //把Float替换为Int则是转化为整型
    n,_:=strconv.Atoi("123")//自动转化，反过来Rtoi
    
    
}
```





## 4. 进程信息

在Go语言中，`os`和`os/exec`包提供了与操作系统交互和执行外部命令的函数。在代码示例中，我们演示了如何获取命令行参数、获取和设置环境变量，以及执行外部命令并获取输出结果。

### os.Args

`os.Args`是一个字符串切片，包含了命令行传入的所有参数。

### os.Getenv

`os.Getenv`函数用于获取指定环境变量的值。

### os.Setenv

`os.Setenv`函数用于设置指定环境变量的值。

### exec.Command

`exec.Command`函数用于执行外部命令。它接收命令名和命令参数作为参数，并返回一个`*Cmd`类型的实例，代表了正在准备执行的命令。

### CombinedOutput

`CombinedOutput`方法用于执行命令，并返回命令的标准输出和标准错误合并后的输出结果。

```go
// 导入必要的包
package main
import(
    "fmt" // 格式化输入输出
    "os" // 提供了一些与操作系统交互的函数和变量
    "os/exec" // 执行外部命令
)
func main(){
    fmt.Println(os.Args) // 打印命令行参数
    fmt.Println(os.Getenv("PATH")) // 获取环境变量
    fmt.Println(os.Setenv("AA","BB")) // 设置环境变量
    buf,err:=exec.Command("grep","127.0.0.1","/etc/hosts").CombinedOutput() // 执行命令
    if err!=nil{
        panic(err) // 如果出错则抛出异常
    }
    fmt.Println(string(buf)) // 打印命令输出结果
}
```





## 总结

本文介绍了Go语言中结构体、JSON处理、数字解析和进程信息相关的基础知识。结构体是一种用于组织数据的数据类型，可以包含字段和方法。JSON处理是在Go语言中进行数据编码和解码的常见操作，用于数据交换和存储。数字解析是将字符串转换为数字类型的常见需求，Go语言中的`strconv`包提供了相应的函数支持。进程信息相关的操作允许我们与操作系统交互，获取命令行参数、环境变量，并执行外部命令。

在学习和使用这些知识点时，我们需要注意错误处理，避免程序运行过程中发生未处理的异常。同时，理解和熟练使用这些基础知识是编写更复杂、功能更强大的Go程序的基础。在实际项目中，可以根据需求扩展这些基础知识，实现更加复杂的功能和逻辑。

请注意，本文中的示例代码可能不完整或包含错误，建议在实际开发中结合文档和实践进行学习和调试。