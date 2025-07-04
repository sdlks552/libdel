![[html/第5章/img/5-1.png]]
边框为了都相等且互不干扰，所以拐角处会有等分线

根据边框拐角的等分线的原理
就可以把div的宽与高改成0像素
```css
.box1{
width:0px;
height:0px;
background-color:red;
border-top:10px solid black;
border-left:10px solid blue;
border-bottom:10px solid yellow;
border-right:10px solid pink;
}
```
如下图所示
![[html/第5章/img/6-1.png]]
再将边框的粗细像素值调大
```css
.box1{
width:0px;
height:0px;
background-color:red;
border-top:100px solid black;
border-left:100px solid blue;
border-bottom:100px solid yellow;
border-right:100px solid pink;
}
```
效果：![[html/第5章/img/6-2.png]]
这样就出现了4个三角形，例如想要黄色的那个三角形就可以
把上边框属性删除
```css
.box1{
width:0px;
height:0px;
background-color:red;
border-left:10px solid blue;
border-bottom:10px solid yellow;
border-right:10px solid pink;
}
```
效果：
![[html/第5章/img/6-3.png]]
这样下面的边框形成的三角形就表现出来，现在左右两边边框支撑着黄色三角形的高，所以只需要将左右两边的边框颜色变成透明就可以了，透明色 ： `transparent` 
```css
.box1{
width:0px;
height:0px;
background-color:red;
border-left:10px solid transparent;
border-bottom:10px solid yellow;
border-right:10px solid transparent;
}
```
效果：
![[html/第5章/img/6-4.png]]
这样左右两边就变成透明，黄色的三角形就显示出来了，如果不要红色的背景只要黄色的三角形可以删除背景色属性
```css
.box1{
width:0px;
height:0px;
border-left:10px solid transparent;
border-bottom:10px solid yellow;
border-right:10px solid transparent;
}
```
效果：
![[6-5.png]]
