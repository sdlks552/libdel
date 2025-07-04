### 网页中引用css样式

  - 内联样式
    就是指在html文件中的head标签中的style标签中写的样式就是内联样式
  - 内部样式表
    就是在标签上写的样式
    比如： `<p style="font-size: 50px; color: rgb(0,0,0);">内容</a>` 
    内部优先级高于内联，且它的优先级最高，包括id等方法。
  - 外部样式表
    - 链接式
      链接式即 `link标签` ，它被广泛应用，推荐使用。与导入式一样都能连接到css但是有些link能做到import做不到。
    - 导入式
      导入式即 `@import rul` ，它只能导入css样式，且大多情况不兼容

  css文件的写法
    在css文件中不需要写style标签，直接写选择器的样式
    比如：
    `h1{`
    `   font-size: 70px;`
    `   color: #000000;`
    `}`

  第一种与html文件和css建立连接方法
  `<link rel="stylesheet" href="css文件文件/网页路径">` 
  第二种
  `<style>`
  `    @import url(css文件/网页路径);`
  `</style>` 
  这个写在html的head标签中
  推荐使用第一种，第二种不用了解即可

  优先级
  内部>内联=外联
  内联与外联平级，谁的样式起作用取决于html中两者代码的前后顺序