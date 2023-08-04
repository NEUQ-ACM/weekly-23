

# 学习Go的一些小结：反射机制和结构体标签应用

Go语言是一门简洁高效的编程语言，具有强大的标准库和高并发的特性，适用于各种应用场景。在学习Go的过程中，反射机制和结构体标签是一些重要且常用的特性，本文将对这两个主题进行一些讨论和实践。

## 反射机制

反射是指程序在运行时动态地获取变量的类型信息和值信息，以及动态调用方法。Go语言中的反射由`reflect`包提供支持。

### 反射的基本用法

在`reflect`包中，`ValueOf`用于获取输入参数接口中的数据的值，`TypeOf`用于动态获取输入参数接口中的值的类型。
> ValueOf 用来获取输入参数接口中的数据的值，如果接口为空则返回0
```go
func ValueOf(i interface{}) Value{...}
```
>TypeOf用来动态获取输入参数接口中的值的类型，如果接口为空则返回nil
```go
func TypeOf(i interface{}) Type{...}
```

```go
package main

import(
"reflect"
    "fmt"
)
func reflectNum(arg interface{}){
    fmt.Println("type:",reflect.TypeOf(arg))//type: float64
    fmt.Println("value:",reflect.ValueOf(arg))//value: 1.2356
}


func main() {
    var num float64=1.2356
    reflectNum(num)

}

```
>使用反射获取结构体数据
反射可以用于动态地获取结构体的字段和方法。下面我们定义一个`User`结构体，并使用反射机制获取其数据。



- User的定义
```go

type User struct {
	Id   int
	Name string
	Age  int
}

func (this User) Call() {//user的方法，注意要大写，不要传指针
	fmt.Println("user is called ..")
	fmt.Printf("%v\n", this)
}
```

- 反射机制获取User数据
```go

func DoFiledAndMethod(input interface{}) {
	//获取input的type
	inputType := reflect.TypeOf(input)
	fmt.Println("inputType is", inputType.Name())
	//获取input的value
	inputValue := reflect.ValueOf(input)

	fmt.Println("inputValue is", inputValue)
	//分别通过type 获取里面的字段
	//1.获取interface的reflect.Type，通过Type得到NumField，进行遍历
	//2.得到每个field，数据类型
	//3.通过filed有一个Interface()方法得到对应的value
	for i := 0; i < inputType.NumField(); i++ {
		field := inputType.Field(i)
		value := inputValue.Field(i).Interface()
		fmt.Printf("%s: %v = %v\n", field.Name, field.Type, value)
	}

	//分别通过type 获取里面的方法，调用
	for i := 0; i < inputType.NumMethod(); i++ {
		m := inputType.Method(i)
		fmt.Printf("%s: %v\n", m.Name, m.Type)
	}

}
```
- 定义User，将数据打印
```go
func main() {
	user := User{1, "me", 18}
	DoFiledAndMethod(user)

}
```

- 输出如下:
```
inputType is User
inputValue is {1 me 18}
Id: int = 1
Name: string = me
Age: int = 18
Call: func(main.User)
```

## golang 反射解析结构体标签Tag

> 结构体标签是结构体字段后面的元数据，可以通过反射机制获取。常用的应用场景是在JSON编解码时，可以指定字段的名称。

- 结构体标签的定义

```go
type resume struct{
    Name string `info:"name" doc:"我的名字"`//元数据，能够使用反射获取到的信息
    Sex string `info:"sex"`
}
```

- 获取结构体中每一个字段对应的标签数据
```go
func findTag(str interface{}){
    t:=reflect.TypeOf(str).Elem()
    for i:=0;i<t.NumField();i++{
        tagstring:=t.Field(i).Tag.Get("info")
        //如果要获取doc对应的数据，只需把info换成doc即可
        fmt.Println("info: ",tagstring)
    }
}
```

- 调用方法

```go
func main() {
    var re resume
    findTag(&re)
}
```

## 结构体标签在json中的应用(json编解码)

结构体标签在JSON编解码时特别有用，可以控制结构体字段在JSON中的名称。

- 导入包

```go
import (
	"encoding/json"
	"fmt"
)
```



- 定义结构体标签

```go
type Movie struct {
	Title  string   `json:"title"`
	Year   int      `json:"year"`
	Price  int      `json:"price"`
	Actors []string `json:"actors"`
}
```

- 在main中创建结构体变量

```go
movie := Movie{"喜剧之王", 2000, 10, []string{"xingye", "zhangbozhi"}}

```

> 编码的过程，结构体 &rarr; json

```go
	jsonStr, err := json.Marshal(movie)
	if err != nil {
        fmt.Println("json marshal error", err)
		return
	}
	fmt.Printf("jsonStr =%s\n", jsonStr)
```

> 解码的过程，jsonstr&rarr; 结构体

```
jsonStr ={"title":"喜剧之王","year":2000,"price":10,"actors":["xingye","zhangbozhi"]}
```

```go
	my_movie:=Movie{}
    err=json.Unmarshal(jsonStr,&my_movie)
    if err!=nil{
        fmt.Println("json unmarshal error",err)
        return
    }
    fmt.Printf("%v\n",my_movie)
```
## 总结

本文介绍了Go语言中的反射机制和结构体标签的用法。反射允许我们在运行时获取变量的类型信息和值信息，以及动态调用方法。结构体标签是结构体字段的元数据，可以通过反射机制获取，常用于控制字段在JSON编解码时的名称。反射和结构体标签在一些特定场景下非常实用，但过度使用反射可能导致代码复杂性增加，应该谨慎使用。希望本文对学习Go语言的反射和结构体标签有所帮助。

